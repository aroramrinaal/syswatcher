import psutil
from rich.console import Console
from rich.progress import Progress

console = Console()

def get_cpu_usage():
    """Fetch the CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def display_cpu_usage():
    """Display CPU usage with a progress bar."""
    usage = get_cpu_usage()
    with Progress() as progress:
        task = progress.add_task("[cyan]CPU Usage", total=100)
        progress.update(task, completed=usage)
        console.print(f"Current CPU Usage: {usage}%", style="bold green")
