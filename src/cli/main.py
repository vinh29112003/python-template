"""CLI module for the application."""

import typer

from . import __version__

# Project configuration - can be customized for different projects
PROJECT_NAME = "python-template"
PROJECT_DESCRIPTION = "A modern Python project template"


def version() -> None:
  """Show the version information."""
  typer.echo(f"{PROJECT_NAME} version {__version__}")


def info() -> None:
  """Show project information."""
  typer.echo(PROJECT_NAME)
  typer.echo(PROJECT_DESCRIPTION)
  typer.echo(f"Version: {__version__}")


def main() -> None:
  """Main CLI entry point with help information."""
  typer.echo(PROJECT_NAME)
  typer.echo(PROJECT_DESCRIPTION)
  typer.echo(f"Version: {__version__}")
  typer.echo()
  typer.echo("Available commands:")
  typer.echo("  version  - Show the version information")
  typer.echo("  info     - Show project information")


if __name__ == "__main__":
  typer.run(main)
