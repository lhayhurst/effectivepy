# README

![Build Status](https://github.com/lhayhurst/effectivepy/actions/workflows/python-app.yml/badge.svg)


This project is a make-friendly, Github Actions CI/CD [batteries included](.github/workflows/python-app.yml) starter Python project that combines [Poetry](https://python-poetry.org/docs/) and [Nox](https://nox.thea.codes/en/stable/). It is partially inspired by Claudio Jolowicz's [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) article series. 

I am using it to work through the second edition of Brett Slatkin's [Effective Python](https://effectivepython.com/) book. The Python stack used here (python3, black, flake8, mypy, safety, pytest, and nox). The test folder contains pytest files broken out by chapter and item. See the project's [GUIDELINES.md](GUIDELINES.md) doc for more information about the toolchain, and its philosophy.

## Getting Started

1) Install python3. The [first article]((https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)) in the series linked above should get you started (he recommends `pyenv`).

2) Install `poetry`; see the project homepage or [this article](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).

3) Clone this repo. 
   
4) Build the project. If you prefer make, you can run:

```bash
make deps
```

This will run `poetry install` and `poetry run nox --install-only`. You can run `make help` to see more make targets. Alternatively, you can just run `poetry`'s CLI; see [the Makefile](Makefile)'s make targets for inspiration. 

```bash
make clean
```

Will clean out your install. 

## Configuration

This file has some standard config files:

* The overall project is configured via a [PEP518](https://www.python.org/dev/peps/pep-0518/) [pyproject.toml](pyproject.toml) file. If you fork this repo, you should probably change it. It contains the [black](https://pypi.org/project/black/) settings, and the project dependencies.
* the [.gitignore](.gitignore) contains obvious gitignores. The `poetry.lock` file is intentionally not commited.
* the [noxfile.py][noxfile.py] contains nox targets for running `safety` and your `tests`. It uses the [nox-poetry](https://pypi.org/project/nox-poetry/) project for nox-poetry integration.
* The [.flake8](.flake8) has a minimal [flake8](https://flake8.pycqa.org/en/latest/) configuration.
* The [mypy.ini](mypy.ini) has a minimal [mypy](http://mypy-lang.org/) configuration.
* The [pytest.ini](pytest.ini) has a minimal [pytest](https://docs.pytest.org/en/stable/index.html) configuration.
