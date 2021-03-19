# Guidelines

This file has guidelines for contributing to this repo, which has an "opinionated" and "safety-first" view on Python code. 

* Opinonated: All code is run through [black](https://pypi.org/project/black/), an "uncompromising code formatter"
* All code is linted with [flake8](https://flake8.pycqa.org/en/latest/)
* Static type checking is done with [mypy](http://mypy-lang.org/)
* [Safety](https://pypi.org/project/safety/) is used to check for installed dependencies with security vulnerabilities.

Run `make thorough` to run your code against all of these tools.

# But, why?

If you are a lone dev on a project, maybe all of this isn't for you. But if someone else is reading or maintaining your code, these tools will provide a solid basis for good-code-hygiene-oriented development.  

# Write code, mostly functions, not too much 

Michael Pollan [famously authored](https://michaelpollan.com/books/the-omnivores-dilemma/) these three key rules for healthy eating:

* Eat food
* Not too much
* Mostly plants

This project is "vegetarian": Python classes are to be used sparingly. Composition is favored over inheritance, when used. 


