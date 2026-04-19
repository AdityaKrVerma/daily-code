import sys

class Regular:
    def __init__(self, a, b):
        self.a, self.b = a, b

class Slotted:
    __slots__ = ('a', 'b')
    def __init__(self, a, b):
        self.a, self.b = a, b

reg = Regular(1, 2)
slo = Slotted(1, 2)

print(f"Regular size: {sys.getsizeof(reg) + sys.getsizeof(reg.__dict__)} bytes")
print(f"Slotted size: {sys.getsizeof(slo)} bytes")