# Define new class interfaces using simple public attributes, and avoid set and get methods.
# if you decide you need special behavior when an attribute is set, you can migrate to
# the @property decorator and its corresponding setter attribute.
# In order to work properly the name of both the setter and getter
# methods must match the intended property name.
# Ensure that @property methods are fast; do slow or complex work using normal methods.
# The big problem with the @property attributes of the same class.
# They also can’t be reused by unrelated classes, use Descriptors for reusable @property methods


class BoundedResistance:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError("ohms must be > 0")
        self._ohms = ohms


resistance = BoundedResistance(0)  # >>> ohms must be > 0
