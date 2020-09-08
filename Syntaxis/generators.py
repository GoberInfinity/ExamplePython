# Generator expressions avoid memory issues by producing outputs one at a time
# When you’re looking for a way to compose functionality
# that’s operating on a large stream of input, generator
# expressions are the best tool for the job
generator = (x ** 2 for x in range(10))

# Consume 1 item of the generator
next(generator)

# Different ways to consume all the generator
list(generator)
[print(number) for number in generator]

# The problem when you store the generator in a list is that contents could be large.
# Copying the iterator could cause your program to run out of memory and crash.
# One way around this is to provide a new container class that implements the iterator protocol
# The iter built-in function calls the __iter__ . The __iter__ method must return an iterator object
# (which itself implements the __next__ method). Then the for loop repeatedly calls the
# next built-in function on the iterator object until it’s exhausted (raises a
# StopIteration exception).


class ReadIntFromFile(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


# sum method in normalize will call ReadVisits.__iter__ to allocate a new iterator object.
# The for loop will also call __iter__ to allocate a second iterator object.
# Each of those iterators will be advanced and exhausted independently.
# The only downside of this approach is that it reads the input data multiple times.


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = ReadIntFromFile("path")
percentages = normalize(visits)
