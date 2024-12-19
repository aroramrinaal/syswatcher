import typer

app = typer.Typer()

@app.command("hi")
def hi():
    """say hi to the world"""
    typer.echo("hi world")

@app.command("info")
def info():
    """show some info"""
    typer.echo("some info")

if __name__ == "__main__":
    app()