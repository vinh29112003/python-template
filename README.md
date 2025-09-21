# Python Project Template

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/Poetry-5037E9?logo=python&logoColor=fff)](https://python-poetry.org/)
[![Typer](https://img.shields.io/badge/Typer-FF6B6B?logo=python&logoColor=white)](https://typer.tiangolo.com/)
[![Ruff](https://img.shields.io/badge/Ruff-7C3AED?logo=ruff&logoColor=white)](https://docs.astral.sh/ruff/)
[![mypy](https://img.shields.io/badge/mypy-1976D2?logo=python&logoColor=white)](https://mypy.readthedocs.io/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=python&logoColor=white)](https://pytest.org/)
[![MkDocs](https://img.shields.io/badge/MkDocs-526CFE?logo=materialformkdocs&logoColor=fff)](https://www.mkdocs.org/)
[![Make](https://img.shields.io/badge/Make-FF8C00?logo=gnu&logoColor=white)](https://www.gnu.org/software/make/)
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative&logoColor=white)](LICENSE)

A Python project template with modern tooling, automated testing, security scanning, documentation generation, and CLI functionality.

## Includes

- **Ruff** - Linter and code formatter
- **Poetry** - Dependency management
- **mypy** - Static type checking
- **pytest** - Testing framework with coverage
- **Typer** - CLI framework with automatic help generation
- **Pre-commit hooks** - Code quality automation
- **MkDocs** - Documentation with API generation
- **Security tools** - Safety and Bandit for vulnerability scanning
- **Commitizen** - Automated versioning and changelog generation
- **IDE Support** - VS Code configuration and pyenv support

## Getting Started

### Option 1: Quick Start with Clean History (Recommended)

1. Clone the template:
   ```bash
   git clone https://github.com/madebyjake/python-template.git <project-name>
   cd <project-name>
   ```

2. Run the initialization script:
   ```bash
   python init_project.py
   ```
   
   The script will:
   - Ask for your project name and customize all files
   - Create a clean git history with a single initial commit
   - Optionally remove template-specific files
   - Show you the next steps

3. Follow the displayed next steps to install dependencies and start building.

### Option 2: Manual Setup

1. Clone and customize:
   ```bash
   git clone https://github.com/madebyjake/python-template.git <project-name>
   cd <project-name>
   # Update pyproject.toml with your project details
   ```

2. (Optional) Create clean git history:
   ```bash
   # Remove template history and start fresh
   rm -rf .git
   git init
   git add .
   git commit -m "chore: initialize repository"
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Set up pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

5. Run tests:
   ```bash
   poetry run pytest
   # Or use make commands:
   make test
   make check  # Run all checks
   ```

6. Run the application:
   ```bash
   poetry run python-template
   # Or use make commands:
   make run                    # Run with default package name
   make run ARGS="--help"      # Run with arguments
   make debug                  # Run in debug mode
   ```

## Requirements

- **Python**: 3.10, 3.11, 3.12, or 3.13
- **Poetry**: For dependency management

## Development

### Development Commands

Use `make help` to see all available commands, or run directly:

- **Install:** `make install` - Install dependencies
- **Test:** `make test` - Run tests
- **Test with coverage:** `make test-cov` - Run tests with coverage report
- **Run:** `make run` - Run the application
- **Debug:** `make debug` - Run in debug mode
- **Lint:** `make lint` - Run Ruff linter
- **Format:** `make format` - Format code with Ruff
- **Type check:** `make type-check` - Run mypy type checking
- **All checks:** `make check` - Run linting, type checking, and tests
- **Build:** `make build` - Build package for distribution
- **Publish:** `make publish` - Publish to PyPI
- **Documentation:** `make docs` - Build documentation
- **Serve docs:** `make serve-docs` - Serve documentation locally

### Project Structure
```
├── src/                        # Source code
│   └── cli/                    # CLI package
│       ├── __init__.py         # Package initialization with version
│       └── main.py             # CLI module with Typer
├── tests/                      # Test files
│   ├── __init__.py
│   └── test_cli.py             # CLI tests
├── docs/                       # Documentation
│   ├── index.md
│   └── api.md
├── init_project.py             # Project initialization script
├── .vscode/                    # VSCode configuration
│   ├── settings.json           # Editor settings
│   └── extensions.json         # Recommended extensions
├── pyproject.toml              # Project configuration
├── .pre-commit-config.yaml     # Pre-commit hooks
├── .editorconfig               # Editor configuration
├── .python-version             # Python version for pyenv
├── mkdocs.yml                  # Documentation configuration
├── Makefile                    # Development commands
├── CHANGELOG.md                # Version history
└── README.md
```

### CLI Usage

The template includes a CLI built with Typer:

```bash
# Show project information
poetry run python-template

# Show help
poetry run python-template --help

# Run application (multiple ways)
make run                           # Default package name
make run ARGS="--help"             # With arguments
make debug                         # Debug mode
```

### Makefile

The Makefile provides commands for installing dependencies, running tests, linting, formatting, building, publishing, and managing versioning.

- **Configurable**: Update `MAIN_MODULE` and `MAIN_FUNCTION` in Makefile for different entry points
- **Flexible**: Supports running any package with `make run <package-name>`
- **Consistent**: Same commands work regardless of application type
- **Extensible**: Easy to add new targets for different project needs

### Security

The project includes security scanning tools:

- **Safety:** `poetry run safety scan` - Check for known vulnerabilities
- **Bandit:** `poetry run bandit -r src/` - Security linting for Python code

## IDE Support

### VS Code
- **Settings**: Configuration in `.vscode/settings.json` with 2-space indentation, Ruff integration
- **Extensions**: Extension recommendations in `.vscode/extensions.json`
- **Python**: Uses Ruff for linting and formatting

### pyenv
- **Python Version**: Specified in `.python-version` (3.10)
- **Automatic**: pyenv will automatically use the correct Python version

## Configuration

All tools are configured in `pyproject.toml`. See the file for specific settings.

## Versioning and Changelog

The project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) for automated versioning and changelog generation.

- **Versioning**: Follows [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH)
- **Changelog**: Generated from commit messages
- **Commits**: Use [Conventional Commits](https://www.conventionalcommits.org/) format
- **Releases**: Independent of CI/CD platforms

### Versioning Commands
- `make version` - Show current version
- `make bump` - Bump version based on conventional commits
- `make bump-patch` - Patch version bump (0.0.0 → 0.0.1)
- `make bump-minor` - Minor version bump (0.0.0 → 0.1.0)
- `make bump-major` - Major version bump (0.0.0 → 1.0.0)

### Commit Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## License

MIT License - see [LICENSE](LICENSE) file for details.
