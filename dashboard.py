import time
from rich.live import Live
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Group
from rich.progress import Progress, BarColumn, TextColumn, TaskProgressColumn
from rich.columns import Columns
from rich import box
from rich.align import Align
from collector import SystemCollector


class HardwareDashboard:
    def __init__(self):
        self.collector = SystemCollector()
        self.layout = Layout()
        self.setup_layout()
        self.running = True

    def setup_layout(self):
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main"),
        )
        self.layout["main"].split_row(
            Layout(name="left", ratio=2),
            Layout(name="right", ratio=2),
        )
        self.layout["left"].split(
            Layout(name="cpu", ratio=2),
            Layout(name="memory", ratio=1),
            Layout(name="disk", ratio=2),
        )
        self.layout["right"].split(
            Layout(name="gpu", ratio=2),
            Layout(name="network", ratio=1),
            Layout(name="processes", ratio=2),
        )

    def _progress_color(self, value):
        if value < 50:
            return "green"
        elif value < 80:
            return "yellow"
        elif value < 95:
            return "red"
        return "bold red"

    def _bar_chart(self, value, width=30, label=""):
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        filled = int(value / 100 * width)
        empty = width - filled
        bar = "█" * filled + "░" * empty
        color = self._progress_color(value)
        pct = f"{value:5.1f}%"
        return f"[{color}]{bar}[/{color}] [{color}]{pct}[/{color}]"

    def _make_header(self, data):
        cpu_info = data["cpu"]
        mem_info = data["memory"]
        net_info = data["network"]

        t = Table.grid(padding=(0, 2))
        t.add_column(justify="center")
        t.add_column(justify="center")
        t.add_column(justify="center")
        t.add_column(justify="center")

        t.add_row(
            f"[cyan]CPU[/cyan] [bold]{cpu_info['总使用率']:.1f}%[/bold]"
            f"  [dim]@{cpu_info['频率']:.0f}MHz[/dim]",
            f"[magenta]内存[/magenta] [bold]{mem_info['使用率']:.1f}%[/bold]"
            f"  [dim]{mem_info['已用GB']:.1f}/{mem_info['总量GB']:.1f}GB[/dim]",
            f"[green]⬇下载[/green] [bold]{net_info['下载速率KB_s']:.0f}KB/s[/bold]",
            f"[yellow]⬆上传[/yellow] [bold]{net_info['上传速率KB_s']:.0f}KB/s[/bold]",
        )

        return Panel(
            Align.center(t, vertical="middle"),
            title="[bold white]⚡ 硬件性能实时监控器 ⚡",
            title_align="center",
            border_style="bright_cyan",
            subtitle=f"[dim]{data['timestamp']}[/dim]",
            subtitle_align="right",
        )

    def _make_cpu_panel(self, data):
        cpu = data["cpu"]
        per_core = cpu.get("每核心", [])

        core_bars = []
        per_core_display = per_core if per_core else [cpu["总使用率"]]
        for i, pct in enumerate(per_core_display):
            color = self._progress_color(pct)
            bar = self._bar_chart(pct, width=35)
            core_bars.append(f"  #{i:2d}  {bar}")

        text_lines = [
            f"[bold cyan]CPU 使用率:[/bold cyan] [bold]{cpu['总使用率']:.1f}%[/bold]",
            f"[dim]频率: {cpu['频率']:.0f}MHz  |  进程数: {cpu['进程数']}[/dim]",
            "",
            "[bold]各核心状态:[/bold]",
        ] + core_bars

        return Panel(
            "\n".join(text_lines),
            title="[bold]🔲 CPU 处理器[/bold]",
            border_style="cyan",
        )

    def _make_memory_panel(self, data):
        mem = data["memory"]

        progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(complete_style=self._progress_color(mem["使用率"]), finished_style="dim"),
            TaskProgressColumn(),
        )
        progress.add_task("物理内存", total=100, completed=mem["使用率"])

        swap_progress = Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(complete_style=self._progress_color(mem["swap使用率"]), finished_style="dim"),
            TaskProgressColumn(),
        )
        swap_progress.add_task("SWAP", total=100, completed=mem["swap使用率"])

        info_text = f"""
[bold magenta]总内存:[/bold magenta] {mem['总量GB']:.1f}GB
[bold]已用:[/bold] {mem['已用GB']:.1f}GB  |  [bold]可用:[/bold] {mem['可用GB']:.1f}GB
        """

        return Panel(
            Group(Text.from_markup(info_text.strip()), progress, swap_progress),
            title="[bold]🧠 内存[/bold]",
            border_style="magenta",
        )

    def _make_disk_panel(self, data):
        table = Table(box=box.SIMPLE, expand=True)
        table.add_column("盘符", style="cyan")
        table.add_column("容量", justify="right")
        table.add_column("已用", justify="right")
        table.add_column("可用", justify="right")
        table.add_column("使用率", justify="right")

        for d in data["disk"]:
            color = self._progress_color(d["使用率"])
            table.add_row(
                d["盘符"],
                f"{d['总GB']:.1f}GB",
                f"{d['已用GB']:.1f}GB",
                f"{d['可用GB']:.1f}GB",
                f"[{color}]{d['使用率']:.1f}%[/{color}]",
            )

        return Panel(
            table,
            title="[bold]💾 磁盘[/bold]",
            border_style="yellow",
        )

    def _make_gpu_panel(self, data):
        gpu = data.get("gpu")
        if gpu is None:
            return Panel(
                "[dim]未检测到 NVIDIA GPU\n（可能使用集成显卡或AMD显卡）[/dim]",
                title="[bold]🎮 GPU 显卡[/bold]",
                border_style="green",
            )

        lines = [
            f"[bold green]GPU 使用率:[/bold green] [bold]{gpu['使用率']:.1f}%[/bold]",
            self._bar_chart(gpu["使用率"], width=30),
            "",
            f"[bold]显存:[/bold] {gpu['显存已用']:.0f}MB / {gpu['显存总量']:.0f}MB",
            self._bar_chart(gpu['显存已用'] / gpu['显存总量'] * 100 if gpu['显存总量'] > 0 else 0, width=30,
                            label=f"{gpu['显存已用']/gpu['显存总量']*100:.1f}%" if gpu['显存总量'] > 0 else "0%"),
            "",
            f"[bold]温度:[/bold] [{'red' if gpu['温度'] > 80 else 'green'}]{gpu['温度']:.0f}°C[/]",
            f"[bold]功耗:[/bold] {gpu['功耗']:.1f}W",
        ]

        return Panel(
            "\n".join(lines),
            title="[bold]🎮 GPU 显卡[/bold]",
            border_style="green",
        )

    def _make_network_panel(self, data):
        net = data["network"]

        down_mbps = net["下载速率KB_s"] * 8 / 1024
        up_mbps = net["上传速率KB_s"] * 8 / 1024

        lines = f"""
[bold green]▼ 下载速率[/bold green]
  {net['下载速率KB_s']:8.0f} KB/s  ({down_mbps:.2f} Mbps)
  {self._bar_chart(min(net['下载速率KB_s'] / 100, 100), width=25)}

[bold yellow]▲ 上传速率[/bold yellow]
  {net['上传速率KB_s']:8.0f} KB/s  ({up_mbps:.2f} Mbps)
  {self._bar_chart(min(net['上传速率KB_s'] / 50, 100), width=25)}

[dim]累计下载: {net['总下载GB']:.2f}GB[/dim]
[dim]累计上传: {net['总上传GB']:.2f}GB[/dim]
        """

        return Panel(
            Text.from_markup(lines.strip()),
            title="[bold]🌐 网络[/bold]",
            border_style="blue",
        )

    def _make_process_panel(self, data):
        procs = data.get("top_processes", [])

        table = Table(box=box.SIMPLE, expand=True)
        table.add_column("进程", style="cyan", no_wrap=True, max_width=20)
        table.add_column("PID", justify="right", style="dim")
        table.add_column("CPU%", justify="right")
        table.add_column("内存%", justify="right")

        for p in procs:
            cpu_color = self._progress_color(p["CPU%"] * 20)
            mem_color = self._progress_color(p["内存%"])
            name = p["名称"][:18] if len(p["名称"]) > 18 else p["名称"]
            table.add_row(
                name,
                str(p["PID"]),
                f"[{cpu_color}]{p['CPU%']:.1f}[/{cpu_color}]",
                f"[{mem_color}]{p['内存%']:.1f}[/{mem_color}]",
            )

        return Panel(
            table,
            title="[bold]📊 进程 Top 8（按CPU）[/bold]",
            border_style="red",
        )

    def render(self, data):
        self.layout["header"].update(self._make_header(data))
        self.layout["cpu"].update(self._make_cpu_panel(data))
        self.layout["memory"].update(self._make_memory_panel(data))
        self.layout["disk"].update(self._make_disk_panel(data))
        self.layout["gpu"].update(self._make_gpu_panel(data))
        self.layout["network"].update(self._make_network_panel(data))
        self.layout["processes"].update(self._make_process_panel(data))
        return self.layout

    def run(self):
        print("\n" * 3)
        with Live(self.render(self.collector.collect()), refresh_per_second=4, screen=False) as live:
            while self.running:
                try:
                    data = self.collector.collect()
                    live.update(self.render(data))
                    time.sleep(0.5)
                except KeyboardInterrupt:
                    self.running = False
                    break

        print("\n[监控已停止]\n")