"""Console script for hr_at_salifort_motors."""
import hr_at_salifort_motors

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for hr_at_salifort_motors."""
    console.print("Replace this message by putting your code into "
               "hr_at_salifort_motors.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
