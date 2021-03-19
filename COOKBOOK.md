# Cookbook

This file contains some snippets on things you might find yourself doing in this repo.

## Poetry things

Here's a nice [cheat sheet](https://gist.github.com/CarlosDomingues/b88df15749af23a463148bd2c2b9b3fb).

### Adding a module

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

### Removing a module

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