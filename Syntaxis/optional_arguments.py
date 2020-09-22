# The best practice is to always specify optional
# arguments using the keyword names and never pass them as positional arguments (*args).
import json
import time
from datetime import datetime


def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period


weight_diff_eg = 0.5
time_diff_eg = 3
pounds_per_hour = flow_rate(weight_diff_eg, time_diff_eg, period=3600, units_per_kg=2.2)

# In Python 3, you can demand clarity by defining your functions with keywordonly
# arguments (*). These arguments can only be supplied by keyword, never by position.
# Here, I redefine the safe_division function to accept keyword-only arguments.


def flow_clarity(weight_diff, time_diff, *, period=1, units_per_kg=1):
    return ((weight_diff / units_per_kg) / time_diff) * period


# pounds_per_hour = flow_clarity(weight_diff, time_diff, 3600, 2.2) # Error
pounds_per_hour = flow_clarity(
    weight_diff_eg, time_diff_eg, period=3600, units_per_kg=2.2
)

# Default argument values are evaluated only once per module
# which usually happens when a program starts up.
# After the module containing this code is loaded,
# the datetime.now default argument will never be evaluated again.


def log(message, when=datetime.now()):
    print(f"{when}, {message}")


log("Hi there!")  # >>> 2020-11-15 21:10:10.371432: Hi there!
time.sleep(0.1)
log("Hi again!")  # >>> 2020-11-15 21:10:10.371432: Hi again!

# Default arguments are only evaluated once: during function definition at module
# load time. This can cause odd behaviors for dynamic values (like {} or []).
# Use None as the default value for keyword arguments that have a dynamic value.
# Document the actual default behavior in the function"s docstring.


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


foo = decode("bad data")
foo["stuff"] = 5
bar = decode("also bad")
bar["meep"] = 1
print(foo)  # {"stuff": 5, "meep": 1}
print(bar)  # {"stuff": 5, "meep": 1}
