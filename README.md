# README

![Build Status](https://github.com/lhayhurst/effectivepy/actions/workflows/python-app.yml/badge.svg)

This project is a make-friendly, Github Actions CI/CD [batteries included](.github/workflows/python-app.yml) starter Python project that combines [Poetry](https://python-poetry.org/docs/) and [Nox](https://nox.thea.codes/en/stable/). It is partially inspired by Claudio Jolowicz's [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) article series. 

I am using it to work through the second edition of Brett Slatkin's [Effective Python](https://effectivepython.com/) book.  See [the tests](tests), which contain pytest files broken out by chapter and item. 

## Useful docs

As documentation, four basic documents are provided: 
1. this [README.md](README.md), 
2. project [GUIDELINES.md](GUIDELINES.md) that all developers who work on the project agree to uphold, 
3. an [ARCHITECTURE.md](ARCHITECTURE.md) document helps developers load the project big picture into their mental model, and finally 
4. a [COOKBOOK.md](COOKBOOK.md) document that answers commonly asked questions/gives useful recipes. 

## Getting Started

1. Install python3. The [first article]((https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)) in the series linked above should get you started (he recommends `pyenv`).
2. Install `poetry`; see the project homepage or [this article](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
3. Clone this repo. 
4. Build the project. If you prefer make, you can run:

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

* The overall project is configured via a [PEP518](https://www.python.org/dev/peps/pep-0518/) [pyproject.toml](pyproject.toml) file. If you fork this repo, you should probably change it. It contains the [black](https://pypi.org/project/black/) settings, the project dependencies, a [pytest](https://docs.pytest.org/en/stable/index.html) configuration, and a 
* the [.gitignore](.gitignore) contains obvious gitignores. The `poetry.lock` file is intentionally not commited.
* the [noxfile.py](noxfile.py) contains nox targets for running `safety` and your `tests`. It uses the [nox-poetry](https://pypi.org/project/nox-poetry/) project for nox-poetry integration.
* The [.flake8](.flake8) has a minimal [flake8](https://flake8.pycqa.org/en/latest/) configuration.
* The [mypy.ini](mypy.ini) has a minimal [mypy](http://mypy-lang.org/) configuration.

## If Forking this project
Here's a checklist of things to change if you fork this project.

- [ ] Blow away `src/effectivepy`, or leave it in place if you find it useful, and make a new package, `src/yourpackage`.
- [ ] In the [.flake8](.flake8) file, swap out `effectivepy` for your project name.
- [ ] In [pyproject.toml](pyproject.toml), replace the project name with your project
- [ ] Replace the `repository` url
- [ ] Replace the `source` list, or add your own in leaving `src/effectivepy` around
- [ ] Re-wrote or updated the project's [README.md](README.md)
- [ ] Re-wrote or updated the project's [GUIDELINES.md](GUIDELINES.md)
- [ ] Re-wrote or updated the project's [COOKBOOK.md](COOKBOOK.md)
- [ ] Re-wrote or updated the project's [ARCHITECTURE.md](ARCHITECTURE.md)

