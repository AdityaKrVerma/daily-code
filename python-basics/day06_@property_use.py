class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def pi(self):
        return 3.14159

c = Circle(5)
print(c.pi)  # 3.14159
# c.pi = 4   # Raises AttributeError: can't set attribute