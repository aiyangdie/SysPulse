import platform
import psutil
import wmi
import subprocess
import json
from datetime import datetime

def get_cpu_info():
    freq = psutil.cpu_freq()
    info = {
        "名称": platform.processor(),
        "架构": platform.machine(),
        "物理核心": psutil.cpu_count(logical=False),
        "逻辑核心": psutil.cpu_count(logical=True),
        "当前频率": f"{freq.current:.0f}MHz" if freq else "N/A",
        "最高频率": f"{freq.max:.0f}MHz" if freq else "N/A",
        "使用率": f"{psutil.cpu_percent(interval=0.5)}%",
    }
    try:
        c = wmi.WMI()
        for cpu in c.Win32_Processor():
            info["型号"] = cpu.Name.strip()
            info["制造商"] = cpu.Manufacturer
            info["插槽"] = cpu.SocketDesignation
            info["L3缓存"] = f"{int(cpu.L3CacheSize / 1024)}MB" if cpu.L3CacheSize else "N/A"
    except:
        pass
    return info


def get_gpu_info():
    gpus = []
    try:
        c = wmi.WMI()
        for video in c.Win32_VideoController():
            if video.Name and "Microsoft" not in video.Name:
                gpus.append({
                    "名称": video.Name.strip(),
                    "驱动版本": video.DriverVersion or "N/A",
                    "显存": f"{int(video.AdapterRAM / (1024**3))}GB" if video.AdapterRAM else "N/A",
                    "当前分辨率": f"{video.CurrentHorizontalResolution}x{video.CurrentVerticalResolution}" if video.CurrentHorizontalResolution else "N/A",
                    "刷新率": f"{video.CurrentRefreshRate}Hz" if video.CurrentRefreshRate else "N/A",
                })
    except:
        pass

    if not gpus:
        try:
            result = subprocess.run(
                ['nvidia-smi', '--query-gpu=name,memory.total,driver_version', '--format=csv,noheader'],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    parts = [p.strip() for p in line.split(',')]
                    gpus.append({
                        "名称": parts[0],
                        "显存": parts[1] if len(parts) > 1 else "N/A",
                        "驱动版本": parts[2] if len(parts) > 2 else "N/A",
                    })
        except:
            pass

    return gpus if gpus else [{"名称": "未检测到独立显卡（使用集成显卡）"}]


def get_memory_info():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    info = {
        "总内存": f"{mem.total / (1024**3):.1f}GB",
        "已用": f"{mem.used / (1024**3):.1f}GB",
        "可用": f"{mem.available / (1024**3):.1f}GB",
        "使用率": f"{mem.percent}%",
        "虚拟内存总量": f"{swap.total / (1024**3):.1f}GB",
        "虚拟内存已用": f"{swap.used / (1024**3):.1f}GB",
    }
    try:
        c = wmi.WMI()
        for phys in c.Win32_PhysicalMemory():
            info["内存类型"] = phys.MemoryType if phys.MemoryType else "N/A"
            info["内存频率"] = f"{phys.Speed}MHz" if phys.Speed else "N/A"
            info["插槽数"] = f"{len(c.Win32_PhysicalMemory())}"
            break
    except:
        pass
    return info


def get_disk_info():
    disks = []
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks.append({
                "盘符": part.device,
                "文件系统": part.fstype,
                "总容量": f"{usage.total / (1024**3):.1f}GB",
                "已用": f"{usage.used / (1024**3):.1f}GB",
                "可用": f"{usage.free / (1024**3):.1f}GB",
                "使用率": f"{usage.percent}%",
            })
        except:
            pass
    return disks


def get_network_info():
    nets = []
    for name, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == 2:
                nets.append({
                    "网卡": name,
                    "IP": addr.address,
                    "子网掩码": addr.netmask or "N/A",
                })
    return nets


def get_system_info():
    boot = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot
    info = {
        "系统": f"{platform.system()} {platform.release()}",
        "版本": platform.version(),
        "主机名": platform.node(),
        "启动时间": boot.strftime("%Y-%m-%d %H:%M:%S"),
        "运行时长": f"{uptime.days}天 {uptime.seconds // 3600}小时 {(uptime.seconds % 3600) // 60}分钟",
        "Python版本": platform.python_version(),
    }
    return info


def get_gpu_usage():
    gpu_stats = []
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=index,name,temperature.gpu,utilization.gpu,memory.used,memory.total,power.draw',
             '--format=csv,noheader,nounits'],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            for line in result.stdout.strip().split('\n'):
                parts = [p.strip() for p in line.split(',')]
                gpu_stats.append({
                    "GPU温度": f"{parts[2]}°C" if len(parts) > 2 else "N/A",
                    "GPU使用率": f"{parts[3]}%" if len(parts) > 3 else "N/A",
                    "显存已用": f"{parts[4]}MB" if len(parts) > 4 else "N/A",
                    "显存总量": f"{parts[5]}MB" if len(parts) > 5 else "N/A",
                    "功耗": f"{parts[6]}W" if len(parts) > 6 else "N/A",
                })
    except:
        pass

    if not gpu_stats:
        try:
            c = wmi.WMI()
            for gpu in c.Win32_VideoController():
                if gpu.Name and "Microsoft" not in gpu.Name:
                    gpu_stats.append({
                        "GPU温度": "N/A（集显不支持）",
                        "GPU使用率": "N/A（无驱动接口）",
                        "显存已用": f"{int(gpu.AdapterRAM / (1024**3))}GB(共享)" if gpu.AdapterRAM else "N/A",
                    })
        except:
            pass

    return gpu_stats


def get_cpu_temperature():
    try:
        c = wmi.WMI(namespace="root\\wmi")
        temps = c.MSAcpi_ThermalZoneTemperature()
        if temps:
            kelvin = temps[0].CurrentTemperature / 10.0
            return f"{kelvin - 273.15:.1f}°C"
    except:
        pass
    try:
        c = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        for sensor in c.Sensor():
            if sensor.SensorType == "Temperature" and "CPU" in sensor.Name:
                return f"{sensor.Value:.1f}°C"
    except:
        pass
    try:
        c = wmi.WMI(namespace="root\\cimv2")
        for cpu in c.Win32_PerfFormattedData_Counters_ProcessorInformation():
            pass
    except:
        pass
    return "N/A"


def get_all_hardware_info():
    return {
        "system": get_system_info(),
        "cpu": get_cpu_info(),
        "gpu": get_gpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
    }


if __name__ == "__main__":
    info = get_all_hardware_info()
    print(json.dumps(info, ensure_ascii=False, indent=2))