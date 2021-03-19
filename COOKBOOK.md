# Cookbook

This file contains some snippets on things you might find yourself doing in this repo.

* [Cookbook](#cookbook)
  * [Poetry things](#poetry-things)
     * [How do I activate a virtualenv?](#how-do-i-activate-a-virtualenv)
     * [How do I use it from Pycharm?](#how-do-i-use-it-from-pycharm)
     * [How do I add a python module?](#how-do-i-add-a-python-module)
     * [How do I remove a Python module?](#how-do-i-remove-a-python-module)
     * [Building your module](#building-your-module)
  * [pylint](#pylint)
     * [The flake8-import-order is too strict, how do I turn it off?](#the-flake8-import-order-is-too-strict-how-do-i-turn-it-off)
  * [black](#black)
     * [How do I black my code so it passes the linter?](#how-do-i-black-my-code-so-it-passes-the-linter)
     * [My team is all using 64-inch curved monitors, where do I set the default black line length?](#my-team-is-all-using-64-inch-curved-monitors-where-do-i-set-the-default-black-line-length)
  * [pytest](#pytest)
     * [How do I pass custom arguments into the pytest?](#how-do-i-pass-custom-arguments-into-the-pytest)




## Poetry things
There are lots of good Poetry tutorials on the webs; [here's one I like](https://hackersandslackers.com/python-poetry-package-manager/). 

### How do I activate a virtualenv?
Run 

```
 poetry shell
```

### How do I use it from Pycharm?
Python has a third party [Poetry plugin](https://plugins.jetbrains.com/plugin/14307-poetry) in their marketplace which was, as of this writing (`2021-03-19`), unstable for me. My workaround was to make a `poetry shell` and use path it made is a `virtualenv` in Pycharm.

### How do I add a python module?

[typer](https://github.com/tiangolo/typer) is a type-hint driven CLI builder. It's really nice.

```shell
 poetry add typer
Using version ^0.3.2 for typer

Updating dependencies
Resolving dependencies... (0.4s)

Writing lock file

Package operations: 1 install, 0 updates, 0 removals

  • Installing typer (0.3.2)
```

Some variations on add:

```shell
 poetry add typer@latest  # get the latest version of an already installed dependency
 poetry add "typer>=0.3.1" # get at least version 0.3.1
 poetry add ../my-package/dist/my-package-0.1.0.tar.gz  # add a local package
```

### How do I remove a Python module?

Or not!

```shell
 poetry remove typer        
Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file

Package operations: 0 installs, 0 updates, 1 removal

  • Removing typer (0.3.2)

```

### Building your module
```shell
  poetry build       
Building effectivepy (0.1.0)
  - Building sdist
  - Built effectivepy-0.1.0.tar.gz
  - Building wheel
  - Built effectivepy-0.1.0-py3-none-any.whl       
```

## pylint

### The flake8-import-order is too strict, how do I turn it off?
Remove the `I` in [pyproject.toml](pyproject.toml). For full cleanse, `poetry remove --dev pylint-import-order

## black

### How do I black my code so it passes the linter?
Run `make black` or `poetry run black`

### My team is all using 64-inch curved monitors, where do I set the default black line length?
Set it in the `[tool.black]` section of the [pyproject.toml](pyproject.toml) file. 

## pytest

### How do I pass custom arguments into the pytest?
Run `poetry run pytest ARGS`; for example:

```shell
  poetry run pytest --cov tests
```
