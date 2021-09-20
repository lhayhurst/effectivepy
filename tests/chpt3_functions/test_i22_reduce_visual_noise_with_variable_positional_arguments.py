def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


def test_simple_log_example(capfd):
    log("Hi there", [])
    out, _ = capfd.readouterr()
    assert "Hi there" in out


def test_log_example_with_values(capfd):
    log("My numbers are", [1, 2])
    out, _ = capfd.readouterr()
    assert "My numbers are: 1, 2" in out


# but having to pass the empty list is cumbersome and noisy.
# its better to leave it out entirely.
# this can be done with prefixing the second argument with a *


def better_log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}: {values_str}")


def test_simple_better_log_example(capfd):
    better_log("Hi there")
    out, _ = capfd.readouterr()
    assert "Hi there" in out


def test_better_log_example_with_values(capfd):
    better_log("My numbers are", [1, 2])
    out, _ = capfd.readouterr()
    assert "My numbers are: 1, 2" in out


# but, there are a few problems. the first is that, because the vararg is converted to a
# tuple when its passed it, it will exhaust the generator when the function is called
# when could OOM kill your program

# the second issues with *args is that you can't add new positional arguments
# to a function in the future without migrating every caller. If you try to do this:

# def log(sequence, message, *values)

# existing clients will subtly break if they aren't updated
# to avoid this possibility, you should use keyword only arguments when you want to extend functions
# that accept *args
