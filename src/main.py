import typer
from src.metrics.cpu import display_cpu_usage, display_cpu_info
from src.metrics.memory import display_memory_usage
from src.metrics.disk import display_disk_usage, display_disk_io, display_disk_partitions

app = typer.Typer()

@app.command("cpu")
def cpu():
    """Display real-time CPU usage metrics:
    - Overall CPU utilization
    - Per-core activity with visual indicators
    - CPU time distribution across states
    - Active cores summary and load averages
    """
    display_cpu_usage()

@app.command("cpu-info")
def cpu_info():
    """Display comprehensive CPU information including:
    - Basic CPU details (processor, architecture, cores)
    - Frequency information (current, min, max)
    - CPU statistics (context switches, interrupts)
    - CPU times (user, system, idle)
    - System load averages
    """
    display_cpu_info()

@app.command("memory")
def memory():
    """Monitor memory usage."""
    display_memory_usage()

@app.command("disk-usage")
def disk_usage():
    """Show disk space usage for all mounted partitions.
    Displays total, used, and free space with visual usage indicators."""
    display_disk_usage()

@app.command("disk-io")
def disk_io():
    """Display real-time disk I/O statistics.
    Shows read/write speeds and operation counts for all disks.
    Press Ctrl+C to stop monitoring."""
    display_disk_io()

@app.command("disk-partitions")
def disk_partitions():
    """List all disk partitions and their details.
    Shows mount points, file systems, and partition options."""
    display_disk_partitions()

if __name__ == "__main__":
    app()
    