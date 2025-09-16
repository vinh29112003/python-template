"""Tests for the placeholder package."""

from pathlib import Path

from src.placeholder import __version__
from src.placeholder.utils import example_function, get_project_root


def test_version() -> None:
    """Test that the version is defined."""
    assert __version__ == "0.0.0"


def test_get_project_root() -> None:
    """Test that get_project_root returns a Path object."""
    result = get_project_root()
    assert isinstance(result, Path)
    assert result.name == "python-template"


def test_example_function() -> None:
    """Test that example_function returns expected greeting."""
    result = example_function("World")
    assert result == "Hello, World! This is an example function."


def test_example_function_with_different_name() -> None:
    """Test that example_function works with different names."""
    result = example_function("Python")
    assert result == "Hello, Python! This is an example function."
