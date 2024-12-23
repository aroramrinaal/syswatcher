import typer
from src.metrics.cpu import display_cpu_usage, display_cpu_info
from src.metrics.memory import display_memory_usage
app = typer.Typer()

@app.command("hi")
def hi():
    """say hi to the world"""
    typer.echo("hi world")

@app.command("cpu")
def cpu():
    """show cpu usage"""
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

@app.command("info")
def info():
    """show some info"""
    typer.echo("some info")

@app.command("mrinaal")
def mrinaal():
    """say hi to mrinaal"""
    typer.echo("this cli app was made by mrinaal")

if __name__ == "__main__":
    app()