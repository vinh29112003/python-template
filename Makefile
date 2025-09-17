.PHONY: help install test test-cov lint format type-check clean build publish docs serve-docs version bump bump-major bump-minor bump-patch

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install

test: ## Run tests
	poetry run pytest

test-cov: ## Run tests with coverage
	poetry run pytest --cov=src --cov-report=term-missing

lint: ## Run linting
	poetry run ruff check .

format: ## Format code
	poetry run ruff format .

type-check: ## Run type checking
	poetry run mypy src/

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
	poetry build

publish: ## Publish to PyPI
	poetry publish

docs: ## Build documentation
	poetry run mkdocs build

serve-docs: ## Serve documentation locally
	poetry run mkdocs serve

version: ## Show current version
	@poetry version --short

bump: ## Bump version based on conventional commits
	@poetry run cz bump --changelog
	@git add pyproject.toml src/placeholder/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell poetry version --short)"
	@git tag $(shell poetry version --short | sed 's/^/v/')
	@echo "Version bumped and committed. Don't forget to push with: git push --follow-tags"

bump-patch: ## Bump patch version (0.0.0 -> 0.0.1)
	@poetry run cz bump --increment PATCH --changelog
	@git add pyproject.toml src/placeholder/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell poetry version --short)"
	@git tag $(shell poetry version --short | sed 's/^/v/')
	@echo "Patch version bumped and committed. Don't forget to push with: git push --follow-tags"

bump-minor: ## Bump minor version (0.0.0 -> 0.1.0)
	@poetry run cz bump --increment MINOR --changelog
	@git add pyproject.toml src/placeholder/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell poetry version --short)"
	@git tag $(shell poetry version --short | sed 's/^/v/')
	@echo "Minor version bumped and committed. Don't forget to push with: git push --follow-tags"

bump-major: ## Bump major version (0.0.0 -> 1.0.0)
	@poetry run cz bump --increment MAJOR --changelog
	@git add pyproject.toml src/placeholder/__init__.py CHANGELOG.md
	@git commit -m "chore: bump version to $(shell poetry version --short)"
	@git tag $(shell poetry version --short | sed 's/^/v/')
	@echo "Major version bumped and committed. Don't forget to push with: git push --follow-tags"
