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
