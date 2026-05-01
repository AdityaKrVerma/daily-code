from functools import singledispatch

@singledispatch
def process(data):
    print(f"Generic processing: {data}")

@process.register(int)
def _(data):
    print(f"Processing an integer: {data}")

process("hello")  # Generic processing
process(10)       # Processing an integer