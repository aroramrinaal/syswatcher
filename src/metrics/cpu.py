import psutil
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_cpu_usage(interval: float = 1.0) -> float:
    """Fetch the overall CPU usage percentage."""
    return psutil.cpu_percent(interval=interval)

def get_per_core_usage(interval: float = 1.0) -> list:
    """Fetch the CPU usage percentage for each core."""
    return psutil.cpu_percent(interval=interval, percpu=True)

def display_cpu_usage():
    """Display CPU usage with a progress bar and per-core usage table."""
    overall_usage = get_cpu_usage()
    per_core_usage = get_per_core_usage()

    with Progress(
        TextColumn("[bold cyan]Overall CPU Usage"),
        BarColumn(bar_width=40, style="bold green"),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("CPU Usage", total=100)
        progress.update(task, completed=overall_usage)
        progress.refresh()

    table = Table(title="Per-Core CPU Usage", show_header=True, header_style="bold magenta")
    table.add_column("Core", style="dim", width=6)
    table.add_column("Usage (%)", justify="right")

    for idx, usage in enumerate(per_core_usage, start=1):
        table.add_row(f"Core {idx}", f"{usage}%")

    panel = Panel(table, title="CPU Cores", border_style="green")
    console.print(panel)