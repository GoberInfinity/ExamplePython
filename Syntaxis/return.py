# Functions that return None to indicate special meaning are error prone because
# None and other values (e.g., zero, the empty string) all evaluate to False in
# conditional expressions.
# Raise exceptions to indicate special situations instead of returning None. Expect the
# calling code to handle exceptions properly when they’re documented.


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Invalid inputs") from e


# Remember to NOT put an else after a return. PYL-R1705
# Only applies to non functional environments
# Info: https://stackoverflow.com/a/57539298/8425653
# if is_internal_link(link):
#   return check_internal_link(link)
# else:
#   return check_external_link(link)
