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


def get_user_input() -> tuple[str, str, str, str, bool, bool]:
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

  # Collect project description
  default_description = "A modern Python project"
  project_description = input(
    f"📝 Enter project description (default: '{default_description}'): "
  ).strip()
  if not project_description:
    project_description = default_description

  # Collect author information
  print()
  while True:
    author = input(
      "👤 Enter your name and email (optional, press Enter to skip): "
    ).strip()

    if not author:
      break

    # Basic email validation if author is provided
    if "<" in author and ">" in author:
      email_part = author.split("<")[1].split(">")[0].strip()
      if "@" not in email_part or "." not in email_part.split("@")[1]:
        print(
          "❌ Invalid email format. Please use 'Name <email@domain.com>' or press Enter to skip."
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

  # Prompt for MkDocs preference
  print()
  print("📚 Documentation options:")
  print("1. Keep MkDocs (recommended for most projects)")
  print("2. Remove MkDocs (if you prefer other documentation tools)")

  while True:
    mkdocs_choice = input("Choose documentation option (1 or 2): ").strip()
    if mkdocs_choice in ["1", "2"]:
      keep_mkdocs = mkdocs_choice == "1"
      break
    print("❌ Please enter 1 or 2.")

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

  return (
    project_name,
    project_description,
    author,
    commit_msg,
    keep_mkdocs,
    cleanup_template,
  )


def confirm_changes(
  project_name: str,
  project_description: str,
  author: str,
  commit_msg: str,
  keep_mkdocs: bool,
  cleanup_template: bool,
) -> bool:
  """Display summary and confirm changes before proceeding."""
  print()
  print("📋 Summary of changes:")
  print("=" * 40)
  print(f"Project name: {project_name}")
  print(f"Description: {project_description}")
  print(f"Author: {author if author else 'Not specified'}")
  print(f"Commit message: {commit_msg}")
  print(f"Keep MkDocs: {'Yes' if keep_mkdocs else 'No'}")
  print(f"Cleanup template files: {'Yes' if cleanup_template else 'No'}")
  print("=" * 40)
  print()

  while True:
    confirm = input("Proceed with initialization? (y/N): ").strip().lower()
    if confirm in ["y", "yes"]:
      return True
    elif confirm in ["n", "no", ""]:
      return False
    print("❌ Please enter 'y' for yes or 'n' for no.")


def update_pyproject_toml(
  project_name: str, project_description: str, author: str
) -> None:
  """Update pyproject.toml with new project details."""
  pyproject_path = Path("pyproject.toml")
  content = pyproject_path.read_text()

  # Replace package name
  content = re.sub(r'name = "python-template"', f'name = "{project_name}"', content)

  # Replace description
  content = re.sub(
    r'description = "A modern Python project template"',
    f'description = "{project_description}"',
    content,
  )

  # Replace author information if provided
  if author:
    content = re.sub(
      r'authors = \["Your Name <your\.email@example\.com>"\]',
      f'authors = ["{author}"]',
      content,
    )

  pyproject_path.write_text(content)
  print("✅ Updated pyproject.toml with project details")


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


def update_cli_module(project_name: str, project_description: str) -> None:
  """Update the CLI module with project details."""
  cli_path = Path("src/cli/main.py")
  content = cli_path.read_text()

  # Replace project name
  content = re.sub(
    r'PROJECT_NAME = "python-template"',
    f'PROJECT_NAME = "{project_name}"',
    content,
  )

  # Replace project description
  content = re.sub(
    r'PROJECT_DESCRIPTION = "A modern Python project template"',
    f'PROJECT_DESCRIPTION = "{project_description}"',
    content,
  )

  cli_path.write_text(content)
  print("✅ Updated CLI module with project details")


def update_mkdocs_config(
  project_name: str, project_description: str, author: str
) -> None:
  """Update mkdocs.yml with project details."""
  mkdocs_path = Path("mkdocs.yml")
  content = mkdocs_path.read_text()

  # Replace site name
  content = re.sub(
    r"site_name: Python Project Template",
    f"site_name: {project_name.replace('-', ' ').title()}",
    content,
  )

  # Replace site description
  content = re.sub(
    r"site_description: A modern Python project template with best practices",
    f"site_description: {project_description} with best practices",
    content,
  )

  # Replace site author if provided
  if author:
    content = re.sub(
      r"site_author: Your Name",
      f"site_author: {author.split('<')[0].strip()}",
      content,
    )

  # Replace repo URLs
  content = re.sub(
    r"site_url: https://your-username\.github\.io/python-template",
    f"site_url: https://your-username.github.io/{project_name}",
    content,
  )

  content = re.sub(
    r"repo_name: your-username/python-template",
    f"repo_name: your-username/{project_name}",
    content,
  )

  content = re.sub(
    r"repo_url: https://github\.com/your-username/python-template",
    f"repo_url: https://github.com/your-username/{project_name}",
    content,
  )

  mkdocs_path.write_text(content)
  print("✅ Updated MkDocs configuration")


def remove_mkdocs_files() -> None:
  """Remove MkDocs-related files."""
  mkdocs_files = [
    "mkdocs.yml",
    "docs/",
  ]

  for file_path in mkdocs_files:
    if Path(file_path).exists():
      if Path(file_path).is_dir():
        shutil.rmtree(file_path)
        print(f"🗑️  Removed directory: {file_path}")
      else:
        Path(file_path).unlink()
        print(f"🗑️  Removed file: {file_path}")


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


def show_next_steps(project_name: str, keep_mkdocs: bool) -> None:
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

  if keep_mkdocs:
    print("5. 📚 Build documentation:")
    print("   make docs")
    print()
    print("6. 🔗 Add remote repository (optional):")
  else:
    print("5. 🔗 Add remote repository (optional):")

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
  (
    project_name,
    project_description,
    author,
    commit_msg,
    keep_mkdocs,
    cleanup_template,
  ) = get_user_input()

  # Confirm changes before proceeding
  if not confirm_changes(
    project_name, project_description, author, commit_msg, keep_mkdocs, cleanup_template
  ):
    print("❌ Initialization cancelled.")
    sys.exit(0)

  print()
  print("🔄 Initializing project...")
  print()

  try:
    # Update configuration files
    update_pyproject_toml(project_name, project_description, author)
    update_makefile(project_name)
    update_readme(project_name)
    update_cli_script(project_name)
    update_cli_module(project_name, project_description)

    # Update or remove MkDocs based on user preference
    if keep_mkdocs:
      update_mkdocs_config(project_name, project_description, author)
    else:
      remove_mkdocs_files()

    # Remove template files if requested
    if cleanup_template:
      cleanup_template_files()

    # Create clean git history
    create_clean_git_history(commit_msg)

    # Display next steps
    show_next_steps(project_name, keep_mkdocs)

  except KeyboardInterrupt:
    print("\n❌ Initialization cancelled by user.")
    sys.exit(1)
  except subprocess.CalledProcessError as e:
    print(f"❌ Git command failed: {e}")
    print("💡 Make sure git is installed and you have write permissions.")
    sys.exit(1)
  except PermissionError as e:
    print(f"❌ Permission error: {e}")
    print("💡 Make sure you have write permissions to the current directory.")
    sys.exit(1)
  except Exception as e:
    print(f"❌ Unexpected error during initialization: {e}")
    print("💡 Please check the error message and try again.")
    sys.exit(1)


if __name__ == "__main__":
  main()
