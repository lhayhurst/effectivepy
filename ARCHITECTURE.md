# ARCHITECTURE

This doc is meant to help the reader of this repo wrap their brain around the code inside it.

## Project Stacks

### Development/Test Stack

[Nox]
-----------------------------
[black, flake8, mypy, pytest]
-----------------------------
[Poetry]
-----------------------------
[Python3]
-----------------------------
[OS of choice]

### Deployed Stack

This repo isn't meant to be deployed, as it is just my [hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/#setting-up-a-python-project-using-poetry) exploration on the [Effective Python](https://effectivepython.com/) book. All interaction with the code is of the `make test` variety.