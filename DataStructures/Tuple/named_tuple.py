# Use namedtuple for lightweight, immutable data containers before you need the
# flexibility of a full class
# You can’t specify default argument values for namedtuple classes. This makes
# them unwieldy when your data may have many optional properties. If you find
# yourself using more than a handful of attributes, defining your own class may be a
# better choice.
# Avoid making long tuples.
import collections

Grade = collections.namedtuple("Grade", ("score", "weight"))
Grade(10, weight=3)
