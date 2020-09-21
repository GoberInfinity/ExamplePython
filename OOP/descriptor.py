# The descriptor protocol defines how attribute access is interpreted by the language.
# A descriptor class can provide __get__ and __set__ methods that let you reuse
# the grade validation behavior without any boilerplate.
# For this purpose, descriptors are also better than mixins

# Grade class to keep track of its value for each unique Exam
# instance. I can do this by saving the per-instance state in a dictionary
# If not instance a single Grade instance is shared across all Exam instances
from weakref import WeakKeyDictionary


class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    # __get__(exam, Exam)
    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    # The _values dictionary will hold a reference to every instance of Exam ever
    # passed to __set__ over the lifetime of the program.
    # This causes instances to never have their reference count go to zero,
    # preventing cleanup by the garbage collector.
    # To fix this, I can use Python"s weakref built-in module.
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value


class Exam:
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print("First ", first_exam.writing_grade, "is right")
print("Second ", second_exam.writing_grade, "is right")
