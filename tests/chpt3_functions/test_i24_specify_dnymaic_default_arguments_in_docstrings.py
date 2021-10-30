# this recipe points out a very important thing that can trip people up in python
# default arguments are evaluated only ONCE, at program interpret time
# the convention is to use docstring and None type for this
import dataclasses
import re
from datetime import datetime


def log(message, when=None):
    """
    :param message: message to print
    :param when: datetime of when the message occured. Defaults to present time
    :return: None
    """
    when = when or datetime.now()
    print(f"{when}: {message}")


def test_log_works_with_none_arg(capsys):
    log("hello, world")
    captured = capsys.readouterr()
    regex = re.compile(
        r"^\d{4}-\d{2}-\d{2}.*: hello, world",
    )
    assert regex.match(captured.out)


def test_log_works_with_provided_arg(capsys):
    log("hello, world", "foo")
    captured = capsys.readouterr()
    regex = re.compile(
        r"^foo: hello, world",
    )
    assert regex.match(captured.out)


# import dataclasses as dc
