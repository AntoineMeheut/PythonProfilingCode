"""Console script for PythonProfilingCode."""

import typer
from rich.console import Console
from src.modules.profilingCode.concatenation.methodejoin1 import methodejoin1
from src.modules.profilingCode.concatenation.methodejoin2 import methodejoin2
from src.modules.profilingCode.concatenation.methodejoin3 import methodejoin3

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for PythonProfilingCode."""
    console.print(methodejoin1(5))
    console.print(methodejoin2(5))
    console.print(methodejoin3(5))


if __name__ == "__main__":
    typer.run(main)
