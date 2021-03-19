# README

This project is a make-friendly starter Python project that combines [Poetry](https://python-poetry.org/docs/) and [Nox](https://nox.thea.codes/en/stable/) inspired by Claudio Jolowicz's [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) article series. 

I am using it to work through the second edition of Brett Slatkin's [Effective Python](https://effectivepython.com/) book. The Python stack used here (python3, black, flake8, mypy, safety, pytest, and nox). The test folder contains pytest files broken out by chapter and item. See the project's [GUIDELINES.md](GUIDELINES.md) doc for more information about the toolchain, and its philosophy.

## Getting Started

1) Install python3. The [first article] in the series linked above should get you started (he recommends `pyenv`).

2) Install `poetry`; see the project homepage or [this article](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).

3) Clone this repo. 
   
4) Build the project. If you prefer make, you can run:

```bash
make deps
```

This will run `poetry install` and `poetry run nox --install-only`. You can run `make help` to see more make targets. Alternatively, you can just run `poetry`'s CLI; see [the Makefile](Makefile)'s make targets for inspiration. 

