def my_generator():
    yield 1
    yield 16
    yield 0.0026075212862888024

# Using the generator function to yield values
for value in my_generator():
    print(value)
