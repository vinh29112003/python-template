#!/usr/bin/env python3
"""
Project Initialization Script

Initializes a new project from the python-template.
Creates a clean git history and customizes project details.
"""

from pathlib import Path
import re
import shutil
import subprocess
import sys


def print_banner() -> None:
  """Print a welcome banner."""
  print("=" * 60)
  print("🚀 Python Template Project Initializer")
  print("=" * 60)
  print()


def validate_template() -> bool:
  """Validate that we're running from a template repository."""
  required_files = [
    "pyproject.toml",
    "src/cli/main.py",
    "Makefile",
    ".pre-commit-config.yaml",
  ]

  missing_files = [f for f in required_files if not Path(f).exists()]

  if missing_files:
    print("❌ Error: This doesn't appear to be a python-template repository.")
    print(f"Missing required files: {', '.join(missing_files)}")
    return False

  # Verify git repository exists
  if not Path(".git").exists():
    print("❌ Error: Not a git repository. Please clone the template first.")
    return False

  return True


def get_user_input() -> tuple[str, str, bool]:
  """Get user input for project customization."""
  print("Let's customize your new project!")
  print()

  # Collect project name
  while True:
    project_name = input(
      "📝 Enter your project name (e.g., 'my-awesome-project'): "
    ).strip()
    if not project_name:
      print("❌ Project name cannot be empty. Please try again.")
      continue

    # Validate project name format
    if not re.match(r"^[a-zA-Z0-9_-]+$", project_name):
      print(
        "❌ Project name can only contain letters, numbers, hyphens, and underscores."
      )
      continue

    break

  # Collect commit message
  default_commit = "chore: initialize repository"
  commit_msg = input(
    f"📝 Enter initial commit message (default: '{default_commit}'): "
  ).strip()
  if not commit_msg:
    commit_msg = default_commit

  # Prompt for cleanup preference
  print()
  print("🧹 Template cleanup options:")
  print("1. Remove template-specific files (recommended)")
  print("2. Keep all files")

  while True:
    cleanup_choice = input("Choose cleanup option (1 or 2): ").strip()
    if cleanup_choice in ["1", "2"]:
      cleanup_template = cleanup_choice == "1"
      break
    print("❌ Please enter 1 or 2.")

  return project_name, commit_msg, cleanup_template


def update_pyproject_toml(project_name: str) -> None:
  """Update pyproject.toml with new project name."""
  pyproject_path = Path("pyproject.toml")
  content = pyproject_path.read_text()

  # Replace package name
  content = re.sub(r'name = "python-template"', f'name = "{project_name}"', content)

  # Replace description
  content = re.sub(
    r'description = "A modern Python project template"',
    'description = "A modern Python project"',
    content,
  )

  # Replace author information
  print()
  author = input(
    "👤 Enter your name and email (e.g., 'John Doe <john@example.com>'): "
  ).strip()
  if author:
    content = re.sub(
      r'authors = \["Your Name <your\.email@example\.com>"\]',
      f'authors = ["{author}"]',
      content,
    )

  pyproject_path.write_text(content)
  print(f"✅ Updated pyproject.toml with project name: {project_name}")


def update_makefile(project_name: str) -> None:
  """Update Makefile with new project name."""
  makefile_path = Path("Makefile")
  content = makefile_path.read_text()

  # Replace package and script names
  content = re.sub(
    r"PACKAGE_NAME \?= python-template", f"PACKAGE_NAME ?= {project_name}", content
  )

  content = re.sub(
    r"SCRIPT_NAME \?= python-template", f"SCRIPT_NAME ?= {project_name}", content
  )

  makefile_path.write_text(content)
  print(f"✅ Updated Makefile with project name: {project_name}")


def update_readme(project_name: str) -> None:
  """Update README.md with new project name."""
  readme_path = Path("README.md")
  content = readme_path.read_text()

  # Replace title
  content = re.sub(
    r"# Python Project Template", f"# {project_name.replace('-', ' ').title()}", content
  )

  # Replace CLI usage examples
  content = re.sub(r"poetry run python-template", f"poetry run {project_name}", content)

  content = re.sub(
    r"make run\s+# Default package name", f"make run  # Run {project_name}", content
  )

  readme_path.write_text(content)
  print(f"✅ Updated README.md with project name: {project_name}")


def update_cli_script(project_name: str) -> None:
  """Update the CLI script name in pyproject.toml."""
  pyproject_path = Path("pyproject.toml")
  content = pyproject_path.read_text()

  # Replace script name
  content = re.sub(
    r'python-template = "src\.cli\.main:main"',
    f'{project_name} = "src.cli.main:main"',
    content,
  )

  pyproject_path.write_text(content)
  print(f"✅ Updated CLI script name to: {project_name}")


def cleanup_template_files() -> None:
  """Remove template-specific files."""
  files_to_remove = [
    "init_project.py",  # Script file
    "CHANGELOG.md",  # Template changelog
  ]

  for file_path in files_to_remove:
    if Path(file_path).exists():
      Path(file_path).unlink()
      print(f"🗑️  Removed template file: {file_path}")


def create_clean_git_history(commit_msg: str) -> None:
  """Create a clean git history with a single initial commit."""
  print()
  print("🔄 Creating clean git history...")

  # Remove existing git history
  shutil.rmtree(".git")
  print("✅ Removed existing git history")

  # Initialize git repository
  subprocess.run(["git", "init"], check=True)
  print("✅ Initialized new git repository")

  # Stage all files
  subprocess.run(["git", "add", "."], check=True)
  print("✅ Staged all files")

  # Create initial commit
  subprocess.run(["git", "commit", "-m", commit_msg], check=True)
  print(f"✅ Created initial commit: '{commit_msg}'")


def show_next_steps(project_name: str) -> None:
  """Show next steps to the user."""
  print()
  print("🎉 Project initialization complete!")
  print("=" * 60)
  print()
  print("Next steps:")
  print()
  print("1. 📦 Install dependencies:")
  print("   poetry install")
  print()
  print("2. 🔧 Set up pre-commit hooks:")
  print("   poetry run pre-commit install")
  print()
  print("3. 🧪 Run tests:")
  print("   poetry run pytest")
  print("   # or use: make test")
  print()
  print("4. 🚀 Run your application:")
  print(f"   poetry run {project_name}")
  print("   # or use: make run")
  print()
  print("5. 📚 Build documentation:")
  print("   make docs")
  print()
  print("6. 🔗 Add remote repository (optional):")
  print("   git remote add origin <your-repo-url>")
  print("   git push -u origin main")
  print()
  print("Happy coding! 🚀")


def main() -> None:
  """Main function."""
  print_banner()

  # Validate template repository
  if not validate_template():
    sys.exit(1)

  # Collect user input
  project_name, commit_msg, cleanup_template = get_user_input()

  print()
  print("🔄 Initializing project...")
  print()

  try:
    # Update configuration files
    update_pyproject_toml(project_name)
    update_makefile(project_name)
    update_readme(project_name)
    update_cli_script(project_name)

    # Remove template files if requested
    if cleanup_template:
      cleanup_template_files()

    # Create clean git history
    create_clean_git_history(commit_msg)

    # Display next steps
    show_next_steps(project_name)

  except Exception as e:
    print(f"❌ Error during initialization: {e}")
    sys.exit(1)


if __name__ == "__main__":
  main()
