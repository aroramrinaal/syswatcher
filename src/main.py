import typer
from src.metrics.cpu import display_cpu_usage
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