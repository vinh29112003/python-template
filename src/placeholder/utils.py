"""Utility functions for the placeholder package."""

from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        The project root directory as a Path object.
    """
    return Path(__file__).parent.parent.parent


def example_function(name: str) -> str:
    """Example function demonstrating basic functionality.

    Args:
        name: A name to greet.

    Returns:
        A greeting message.
    """
    return f"Hello, {name}! This is an example function."
