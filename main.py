import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()


def show_menu():
    console.clear()
    console.print()

    title = """
[bold cyan]
╔══════════════════════════════════════════╗
║                                          ║
║   ⚡  硬 件 性 能 实 时 监 控 器  ⚡     ║
║                                          ║
║   CPU / GPU / 内存 / 磁盘 / 网络         ║
║   全硬件支持 · 实时监控 · 性能诊断        ║
║                                          ║
╚══════════════════════════════════════════╝
[/bold cyan]
    """

    console.print(title)
    console.print()

    menu_table = Table(show_header=False, box=box.ROUNDED, border_style="cyan")
    menu_table.add_column("", style="bold cyan", width=4, justify="center")
    menu_table.add_column("", width=30)
    menu_table.add_column("", style="dim", width=25)

    menu_table.add_row("1", "[bold]📊 实时性能监控[/bold]", "启动实时仪表盘，监控所有硬件")
    menu_table.add_row("2", "[bold]🔬 电脑性能诊断[/bold]", "跑分测试，评估电脑综合性能")
    menu_table.add_row("3", "[bold]📋 查看硬件信息[/bold]", "显示所有硬件详细参数")
    menu_table.add_row("4", "[bold]🔢 快速CPU测试[/bold]", "单独测试CPU单核/多核性能")
    menu_table.add_row("0", "[bold red]退出[/bold red]", "")

    console.print(menu_table)
    console.print()
    return Prompt.ask("[bold cyan]请选择功能[/bold cyan]", choices=["0", "1", "2", "3", "4"], default="1")


def show_hardware_info():
    from hardware_info import get_all_hardware_info
    import json

    console.print()
    console.print(Panel.fit("[bold]🔍 正在扫描硬件...[/bold]", border_style="cyan"))
    info = get_all_hardware_info()

    console.clear()
    console.print()
    console.print(Panel.fit("[bold cyan]📋 硬件详细信息[/bold cyan]", border_style="cyan"))

    sys_info = info["system"]
    console.print(Panel.fit(
        f"[bold]系统:[/bold] {sys_info['系统']}\n"
        f"[bold]主机名:[/bold] {sys_info['主机名']}\n"
        f"[bold]运行时长:[/bold] {sys_info['运行时长']}",
        title="💻 系统信息",
        border_style="blue"
    ))

    cpu = info["cpu"]
    cpu_lines = []
    for k, v in cpu.items():
        cpu_lines.append(f"[bold]{k}:[/bold] {v}")
    console.print(Panel.fit("\n".join(cpu_lines), title="🔲 CPU 处理器", border_style="cyan"))

    gpu_list = info.get("gpu", [])
    for i, gpu in enumerate(gpu_list):
        gpu_lines = []
        for k, v in gpu.items():
            gpu_lines.append(f"[bold]{k}:[/bold] {v}")
        console.print(Panel.fit("\n".join(gpu_lines), title=f"🎮 GPU #{i+1}", border_style="green"))

    mem = info["memory"]
    mem_lines = [f"[bold]{k}:[/bold] {v}" for k, v in mem.items()]
    console.print(Panel.fit("\n".join(mem_lines), title="🧠 内存", border_style="magenta"))

    disks = info.get("disk", [])
    disk_table = Table(title="💾 磁盘", border_style="yellow")
    for k in ["盘符", "文件系统", "总容量", "已用", "可用", "使用率"]:
        disk_table.add_column(k, justify="right" if k != "盘符" and k != "文件系统" else "left")
    for d in disks:
        disk_table.add_row(*[d.get(k, "N/A") for k in ["盘符", "文件系统", "总容量", "已用", "可用", "使用率"]])
    console.print(disk_table)

    nets = info.get("network", [])
    if nets:
        net_table = Table(title="🌐 网络", border_style="blue")
        for k in ["网卡", "IP", "子网掩码"]:
            net_table.add_column(k)
        for n in nets:
            net_table.add_row(*[n.get(k, "N/A") for k in ["网卡", "IP", "子网掩码"]])
        console.print(net_table)

    console.print()


def quick_cpu_test():
    from diagnostic import cpu_single_core_score, cpu_multi_core_score
    from rich.progress import Progress, SpinnerColumn, TextColumn

    console.print()
    console.print(Panel.fit("[bold cyan]🔢 CPU 性能快速测试[/bold cyan]", border_style="cyan"))

    with Progress(SpinnerColumn(), TextColumn("[cyan]测试中...[/cyan]"), console=console) as progress:
        task = progress.add_task("", total=None)
        single = cpu_single_core_score()
        multi = cpu_multi_core_score()

    ratio = multi / single if single > 0 else 0

    table = Table(title="CPU 测试结果", border_style="cyan")
    table.add_column("指标", style="cyan")
    table.add_column("分数", justify="right", style="bold")
    table.add_row("单核性能", f"{single:.1f}")
    table.add_row("多核性能", f"{multi:.1f}")
    table.add_row("多核倍率", f"{ratio:.1f}x")
    console.print()
    console.print(table)
    console.print()


def main():
    try:
        while True:
            choice = show_menu()

            if choice == "0":
                console.print()
                console.print("[dim]再见！[/dim]")
                break

            elif choice == "1":
                from dashboard import HardwareDashboard
                console.clear()
                dash = HardwareDashboard()
                dash.run()

            elif choice == "2":
                from diagnostic import run_diagnostic
                run_diagnostic()
                console.input("[dim]按 Enter 返回菜单...[/dim]")

            elif choice == "3":
                show_hardware_info()
                console.input("[dim]按 Enter 返回菜单...[/dim]")

            elif choice == "4":
                quick_cpu_test()
                console.input("[dim]按 Enter 返回菜单...[/dim]")

    except KeyboardInterrupt:
        console.print("\n[dim]已退出[/dim]")
    except Exception as e:
        console.print(f"\n[red]错误: {e}[/red]")
        console.input("[dim]按 Enter 继续...[/dim]")


if __name__ == "__main__":
    main()