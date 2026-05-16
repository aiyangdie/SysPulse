import time
import random
import math
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

console = Console()


def cpu_single_core_score():
    start = time.perf_counter()
    n = 0
    target_time = 2.0
    while time.perf_counter() - start < target_time:
        for i in range(1000):
            n += math.sin(i * 0.001) + math.cos(i * 0.0013) * math.sqrt(i * 0.0001)
            n %= 1000000
    elapsed = time.perf_counter() - start
    return n / elapsed / 1000


def cpu_multi_core_score():
    import concurrent.futures
    import psutil

    cores = psutil.cpu_count(logical=True)

    def worker():
        start = time.perf_counter()
        n = 0
        while time.perf_counter() - start < 1.5:
            for i in range(500):
                n += math.sqrt(i * random.random())
                n %= 1000
        return n / (time.perf_counter() - start)

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
        results = list(executor.map(lambda _: worker(), range(cores)))
    elapsed = time.perf_counter() - start
    return sum(results)


def memory_benchmark():
    import psutil
    size_mb = min(256, int(psutil.virtual_memory().available * 0.3 / (1024 * 1024)))
    if size_mb < 10:
        size_mb = 10

    data = bytearray(size_mb * 1024 * 1024)
    start = time.perf_counter()
    for i in range(0, len(data), 1024):
        data[i] = (data[i] + 1) & 0xFF
    write_elapsed = time.perf_counter() - start

    data2 = bytearray(size_mb * 1024 * 1024)
    start = time.perf_counter()
    data2[:] = data[:]
    copy_elapsed = time.perf_counter() - start

    write_speed = size_mb / write_elapsed
    copy_speed = size_mb / copy_elapsed

    del data, data2
    return {"写入速度MB_s": write_speed, "拷贝速度MB_s": copy_speed, "测试大小MB": size_mb}


def disk_benchmark():
    import tempfile
    import os

    test_size = 50 * 1024 * 1024
    data = bytes([random.randint(0, 255) for _ in range(test_size)])

    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp_path = tmp.name
    tmp.close()

    try:
        start = time.perf_counter()
        with open(tmp_path, 'wb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        write_elapsed = time.perf_counter() - start

        start = time.perf_counter()
        with open(tmp_path, 'rb') as f:
            _ = f.read()
        read_elapsed = time.perf_counter() - start
    finally:
        try:
            os.unlink(tmp_path)
        except:
            pass

    return {
        "顺序写MB_s": 50 / write_elapsed,
        "顺序读MB_s": 50 / read_elapsed,
    }


def calculate_health_score(single, multi, mem, disk):
    score = 0.0
    score += min(single / 5, 40)
    score += min(multi / single / 6 * 30, 30)

    mem_write = mem.get("写入速度MB_s", 0)
    score += min(mem_write / 100 * 15, 15)

    disk_write = disk.get("顺序写MB_s", 0)
    score += min(disk_write / 50 * 15, 15)

    return min(score, 100)


def run_diagnostic():
    console.print()
    console.print(Panel.fit(
        "[bold cyan]🔬 电脑性能诊断系统[/bold cyan]\n"
        "[dim]正在运行多项基准测试，请稍候...[/dim]",
        border_style="cyan"
    ))
    console.print()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:

        task1 = progress.add_task("[cyan]测试CPU单核性能...", total=100)
        for i in range(101):
            time.sleep(0.005)
            progress.update(task1, advance=1)
        single_score = cpu_single_core_score()
        progress.update(task1, completed=100)

        task2 = progress.add_task("[cyan]测试CPU多核性能...", total=100)
        for i in range(101):
            time.sleep(0.002)
            progress.update(task2, advance=1)
        multi_score = cpu_multi_core_score()
        progress.update(task2, completed=100)

        task3 = progress.add_task("[magenta]测试内存带宽...", total=100)
        for i in range(101):
            time.sleep(0.005)
            progress.update(task3, advance=1)
        mem_result = memory_benchmark()
        progress.update(task3, completed=100)

        task4 = progress.add_task("[yellow]测试磁盘读写...", total=100)
        for i in range(101):
            time.sleep(0.003)
            progress.update(task4, advance=1)
        disk_result = disk_benchmark()
        progress.update(task4, completed=100)

    health = calculate_health_score(single_score, multi_score, mem_result, disk_result)

    console.print()
    console.print(Panel.fit(
        "[bold white]📊 诊断报告[/bold white]",
        border_style="bright_white"
    ))

    table = Table(title="CPU 性能", border_style="cyan")
    table.add_column("指标", style="cyan")
    table.add_column("结果", justify="right")
    table.add_row("单核性能得分", f"{single_score:.1f}")
    table.add_row("多核性能得分", f"{multi_score:.1f}")
    table.add_row("多核/单核比率", f"{multi_score/single_score:.1f}x" if single_score > 0 else "N/A")
    console.print(table)

    console.print()
    mem_table = Table(title="内存性能", border_style="magenta")
    mem_table.add_column("指标", style="magenta")
    mem_table.add_column("结果", justify="right")
    mem_table.add_row("写入速度", f"{mem_result['写入速度MB_s']:.0f} MB/s")
    mem_table.add_row("拷贝速度", f"{mem_result['拷贝速度MB_s']:.0f} MB/s")
    mem_table.add_row("测试大小", f"{mem_result['测试大小MB']} MB")
    console.print(mem_table)

    console.print()
    disk_table = Table(title="磁盘性能", border_style="yellow")
    disk_table.add_column("指标", style="yellow")
    disk_table.add_column("结果", justify="right")
    disk_table.add_row("顺序写入", f"{disk_result['顺序写MB_s']:.0f} MB/s")
    disk_table.add_row("顺序读取", f"{disk_result['顺序读MB_s']:.0f} MB/s")
    console.print(disk_table)

    score_color = "green" if health >= 70 else "yellow" if health >= 40 else "red"
    score_bar = "█" * int(health / 5) + "░" * (20 - int(health / 5))

    rating = "⚡ 性能卓越" if health >= 80 else "✅ 性能良好" if health >= 60 else "⚠️ 性能一般" if health >= 40 else "❌ 需要升级"
    detail = (
        "适合运行大型开发环境、编译代码、AI推理" if health >= 80
        else "流畅运行日常开发、中型项目、轻度游戏" if health >= 60
        else "适合办公、浏览网页、轻量开发" if health >= 40
        else "建议升级硬件以获得更好的开发体验"
    )

    console.print()
    console.print(Panel(
        f"\n[bold]综合评分:[/bold]\n"
        f"[{score_color}]{score_bar}[/{score_color}]  [{score_color} bold]{health:.1f}/100[/{score_color} bold]\n\n"
        f"[bold]评级:[/bold] [{score_color}]{rating}[/{score_color}]\n"
        f"[dim]{detail}[/dim]\n",
        title="[bold]🏆 电脑综合性能评分[/bold]",
        border_style=score_color,
    ))

    console.print()
    console.print("[dim]提示: 分数仅供参考，受当前系统负载影响。关闭其他程序后重新测试结果更准确。[/dim]")
    console.print()

    return {
        "cpu_single": single_score,
        "cpu_multi": multi_score,
        "memory": mem_result,
        "disk": disk_result,
        "health_score": health,
        "rating": rating,
    }


if __name__ == "__main__":
    run_diagnostic()