import psutil
import subprocess
import time
from datetime import datetime


class SystemCollector:
    def __init__(self):
        self._prev_net = psutil.net_io_counters()
        self._prev_time = time.time()
        self._prev_disk = {p.device: psutil.disk_io_counters(p.device) for p in psutil.disk_partitions() if hasattr(psutil, 'disk_io_counters')}
        self._gpu_available = self._check_gpu()

    def _check_gpu(self):
        try:
            result = subprocess.run(['nvidia-smi'], capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False

    def _get_cpu_temp(self):
        return None

    def _get_gpu_stats(self):
        if not self._gpu_available:
            return None
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=index,name,utilization.gpu,memory.used,memory.total,temperature.gpu,power.draw',
                 '--format=csv,noheader,nounits'],
                capture_output=True, text=True, timeout=3
            )
            if result.returncode == 0 and result.stdout.strip():
                parts = [p.strip() for p in result.stdout.strip().split(',')]
                return {
                    "使用率": float(parts[2]) if parts[2] else 0,
                    "显存已用": float(parts[3]) if parts[3] else 0,
                    "显存总量": float(parts[4]) if parts[4] else 0,
                    "温度": float(parts[5]) if parts[5] else 0,
                    "功耗": float(parts[6]) if parts[6] else 0,
                }
        except:
            pass
        return None

    def collect(self):
        data = {}

        data["timestamp"] = datetime.now().strftime("%H:%M:%S")

        cpu_percent = psutil.cpu_percent(interval=0.1)
        cpu_freq = psutil.cpu_freq()
        per_core = psutil.cpu_percent(interval=0.1, percpu=True)

        data["cpu"] = {
            "总使用率": cpu_percent,
            "频率": cpu_freq.current if cpu_freq else 0,
            "每核心": per_core,
            "进程数": len(psutil.pids()),
            "温度": self._get_cpu_temp(),
        }

        load = psutil.getloadavg() if hasattr(psutil, 'getloadavg') else (0, 0, 0)
        data["cpu"]["负载1/5/15"] = load

        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        data["memory"] = {
            "总量GB": mem.total / (1024**3),
            "已用GB": mem.used / (1024**3),
            "可用GB": mem.available / (1024**3),
            "使用率": mem.percent,
            "swap总量GB": swap.total / (1024**3),
            "swap已用GB": swap.used / (1024**3),
            "swap使用率": swap.percent,
        }

        data["disk"] = []
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                data["disk"].append({
                    "盘符": part.device,
                    "总GB": usage.total / (1024**3),
                    "已用GB": usage.used / (1024**3),
                    "可用GB": usage.free / (1024**3),
                    "使用率": usage.percent,
                })
            except:
                pass

        net = psutil.net_io_counters()
        elapsed = time.time() - self._prev_time
        if elapsed > 0:
            data["network"] = {
                "上传速率KB_s": (net.bytes_sent - self._prev_net.bytes_sent) / elapsed / 1024 if self._prev_net else 0,
                "下载速率KB_s": (net.bytes_recv - self._prev_net.bytes_recv) / elapsed / 1024 if self._prev_net else 0,
                "总上传GB": net.bytes_sent / (1024**3),
                "总下载GB": net.bytes_recv / (1024**3),
            }
            self._prev_net = net
            self._prev_time = time.time()
        else:
            data["network"] = {"上传速率KB_s": 0, "下载速率KB_s": 0, "总上传GB": 0, "总下载GB": 0}

        top_procs = []
        for proc in sorted(psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']),
                           key=lambda p: p.info.get('cpu_percent', 0) or 0, reverse=True)[:8]:
            try:
                top_procs.append({
                    "名称": proc.info["name"] or "Unknown",
                    "PID": proc.info["pid"],
                    "CPU%": proc.info["cpu_percent"] or 0,
                    "内存%": proc.info["memory_percent"] or 0,
                })
            except:
                pass
        data["top_processes"] = top_procs

        data["gpu"] = self._get_gpu_stats()

        return data