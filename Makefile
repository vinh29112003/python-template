# Package configuration
PACKAGE_NAME ?= python-template
SCRIPT_NAME ?= python-template
MAIN_MODULE ?= main
MAIN_FUNCTION ?= main

.PHONY: help install test test-cov run debug run-pkg debug-pkg lint format type-check clean build publish docs serve-docs version bump bump-major bump-minor bump-patch

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync

test: ## Run tests
	uv run pytest

test-cov: ## Run tests with coverage
	uv run pytest --cov=src --cov-report=term-missing

run: ## Run the application (usage: make run [package] [ARGS="--help"])
	@if [ -n "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		uv run python -c "from $(filter-out $@,$(MAKECMDGOALS)).$(MAIN_MODULE) import $(MAIN_FUNCTION); $(MAIN_FUNCTION)()" $(ARGS); \
	else \
		uv run $(SCRIPT_NAME) $(ARGS); \
	fi

debug: ## Run in debug mode (usage: make debug [package] [ARGS="--help"])
	@if [ -n "$(filter-out $@,$(MAKECMDGOALS))" ]; then \
		uv run python -c "from $(filter-out $@,$(MAKECMDGOALS)).$(MAIN_MODULE) import $(MAIN_FUNCTION); $(MAIN_FUNCTION)()" $(ARGS); \
	else \
		uv run python -c "from cli.$(MAIN_MODULE) import $(MAIN_FUNCTION); $(MAIN_FUNCTION)()" $(ARGS); \
	fi

%:
	@:

lint: ## Run linting
	uv run ruff check .

format: ## Format code
	uv run ruff format .

type-check: ## Run type checking
	uv run mypy src/

check: lint type-check test ## Run all checks

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

build: clean ## Build the package
	uv build

publish: ## Publish to PyPI
	uv publish

docs: ## Build documentation
	uv run mkdocs build

serve-docs: ## Serve documentation locally
	uv run mkdocs serve

version: ## Show current version
	@uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])"

bump: ## Bump version based on conventional commits
	@uv run cz bump --changelog
	@git add pyproject.toml src/cli/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])")"
	@git tag $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])" | sed 's/^/v/')
	@echo "Version bumped and committed. Don't forget to push with: git push --follow-tags"

bump-patch: ## Bump patch version (0.0.0 -> 0.0.1)
	@uv run cz bump --increment PATCH --changelog
	@git add pyproject.toml src/cli/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])")"
	@git tag $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])" | sed 's/^/v/')
	@echo "Patch version bumped and committed. Don't forget to push with: git push --follow-tags"

bump-minor: ## Bump minor version (0.0.0 -> 0.1.0)
	@uv run cz bump --increment MINOR --changelog
	@git add pyproject.toml src/cli/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])")"
	@git tag $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])" | sed 's/^/v/')
	@echo "Minor version bumped and committed. Don't forget to push with: git push --follow-tags"

bump-major: ## Bump major version (0.0.0 -> 1.0.0)
	@uv run cz bump --increment MAJOR --changelog
	@git add pyproject.toml src/cli/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])")"
	@git tag $(shell uv run python -c "import tomli; print(tomli.load(open('pyproject.toml', 'rb'))['project']['version'])" | sed 's/^/v/')
	@echo "Major version bumped and committed. Don't forget to push with: git push --follow-tags"
