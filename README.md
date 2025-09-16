# Python Project Template

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/Poetry-5037E9?logo=python&logoColor=fff)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/badge/Ruff-7C3AED?logo=ruff&logoColor=white)](https://docs.astral.sh/ruff/)
[![mypy](https://img.shields.io/badge/mypy-1976D2?logo=python&logoColor=white)](https://mypy.readthedocs.io/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=python&logoColor=white)](https://pytest.org/)
[![MkDocs](https://img.shields.io/badge/MkDocs-526CFE?logo=materialformkdocs&logoColor=fff)](https://www.mkdocs.org/)
[![Make](https://img.shields.io/badge/Make-FF8C00?logo=gnu&logoColor=white)](https://www.gnu.org/software/make/)
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative&logoColor=white)](LICENSE)

A production-ready Python project template with modern tooling, automated testing, security scanning, and documentation generation.

## Includes

- **Ruff** - Linter and code formatter
- **Poetry** - Dependency management
- **mypy** - Static type checking
- **pytest** - Testing framework with coverage
- **Pre-commit hooks** - Code quality automation
- **MkDocs** - Documentation with API generation
- **Security tools** - Safety and Bandit for vulnerability scanning
- **Commitizen** - Automated versioning and changelog generation
- **IDE Support** - VS Code configuration and pyenv support

## Getting Started

1. Clone and customize:
   ```bash
   git clone <this-repo> my-new-project
   cd my-new-project
   # Update pyproject.toml with your project details
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Set up pre-commit hooks:
   ```bash
   poetry run pre-commit install
   ```

4. Run tests:
   ```bash
   poetry run pytest
   # Or use make commands:
   make test
   make check  # Run all checks
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
│   └── placeholder/            # Placeholder package (rename as needed)
│       ├── __init__.py         # Package initialization
│       └── utils.py            # Example utility functions
├── tests/                      # Test files
│   ├── __init__.py
│   └── test_placeholder.py     # Placeholder test (replace with your tests)
├── docs/                       # Documentation
│   ├── index.md
│   └── api.md
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


### Security

The project includes security scanning tools:

- **Safety:** `poetry run safety scan` - Check for known vulnerabilities
- **Bandit:** `poetry run bandit -r src/` - Security linting for Python code

## IDE Support

### VS Code
- **Settings**: Pre-configured in `.vscode/settings.json` with 2-space indentation, Ruff integration
- **Extensions**: Recommended extensions in `.vscode/extensions.json`
- **Python**: Configured to use Ruff for linting and formatting

### pyenv
- **Python Version**: Specified in `.python-version` (3.10)
- **Automatic**: pyenv will automatically use the correct Python version

## Configuration

All tools are configured in `pyproject.toml`. See the file for specific settings.

## Versioning and Changelog

This project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) for automated versioning and changelog generation.

- **Versioning**: Follows [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH)
- **Changelog**: Automatically generated from commit messages
- **Commits**: Use [Conventional Commits](https://www.conventionalcommits.org/) format
- **Releases**: Independent of CI/CD platforms

### Versioning Commands
- `make version` - Show current version
- `make bump` - Auto-bump based on conventional commits
- `make patch` - Manual patch version bump (0.1.0 → 0.1.1)
- `make minor` - Manual minor version bump (0.1.0 → 0.2.0)
- `make major` - Manual major version bump (0.1.0 → 1.0.0)

### Commit Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## License

MIT License - see [LICENSE](LICENSE) file for details.
