# Guidelines

This file has guidelines for contributing to this repo 

## Being a hypermodern Pythonista builder

This repo has has an "opinionated" and "safety-first" view on Python code.

* Opinionated: All code is run through [black](https://pypi.org/project/black/), an "uncompromising code formatter"
* All code is linted with [flake8](https://flake8.pycqa.org/en/latest/). Multiple flake8 subpackages are used, including `flake8-black`, `flake8-bandit`, `flake8-bugbear`, and `flake8-import-order`. 
* Static type checking is done with [mypy](http://mypy-lang.org/)
* [Safety](https://pypi.org/project/safety/) is used to check for installed dependencies with security vulnerabilities.

Run `make thorough` to run your code against all of these tools.

## But, why?

If you are a lone dev on a project, maybe all of this isn't for you. But if someone else is reading or maintaining your code, these tools will provide a solid basis for good-code-hygiene-oriented development. 

![image](https://user-images.githubusercontent.com/216183/111777591-bcc9f980-8870-11eb-825c-8299c07bb49c.png)


##  Write code, mostly functions, not too much 

Michael Pollan [famously authored](https://michaelpollan.com/books/the-omnivores-dilemma/) these three key rules for healthy eating:

* Eat food
* Mostly plants
* Not too much

This project is "vegetarian": Python classes are to be used sparingly. Composition is favored over inheritance, when used. 


