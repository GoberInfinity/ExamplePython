# The with statement allows you to reuse logic from try/finally blocks and
# reduce visual noise.
# The contextlib built-in module provides a contextmanager decorator that
# makes it easy to use your own functions in with statements
# At the point where the generator yields, the block nested in the with statement is executed. The generator is then resumed after the block is exited.

from contextlib import contextmanager


@contextmanager
def tag(name):
    print(f"{name}")
    # At the point where the generator yields, the block nested in the with statement is executed.
    # The generator is then resumed after the block is exited.
    yield
    print(f"{name}")


with tag("h1"):
    print("foo")

# The context manager passed to a with statement may also return an object.
# This object is assigned to a local variable in the as part of the compound statement.


@contextmanager
def create_connection(connection):
    connection = "Connected"
    try:
        yield connection
    finally:
        print(f"Close connection")


with create_connection("database") as string:
    print(string)
