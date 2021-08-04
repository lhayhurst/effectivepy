PYTHONFILES := $(shell find . -name '*.py' -type f -not -path './.nox/*')

EXECUTABLES = python3 poetry
K := $(foreach exec,$(EXECUTABLES),\
        $(if $(shell which $(exec)),some string,$(error "No $(exec) in PATH")))

.PHONY: help
help: ## me
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: deps  ## do a full install
deps:
	poetry install
	poetry run nox --install-only

.PHONY: black
black:  ## reformat all files for black. good for when someone else needs to read your code.
	poetry run black $(PYTHONFILES)

.PHONY: lint
lint:  ## run flake8 linter
	poetry run flake8 $(PYTHONFILES)

.PHONY: mypy
mypy:
	poetry run mypy $(PYTHONFILES)

.PHONY: safety
safety:  ## check for open source vulnerabilities with safety
	poetry run nox -rs safety

.PHONY: thorough
thorough: lint mypy  ## the full treatment: black check, flake8, mypy, and safety

.PHONY: test
test: mypy  ## run tests after running black check, flake8, and mypy
	poetry run nox -rs tests

.PHONY: cov
cov:  ## run test coverage report
	poetry run pytest tests --cov

.PHONY: clean
clean:  ## clean up project
	rm -rf dist .nox .coverage .mypy_cache .pytest_cache .coverage src/effectivepy.egg-info




