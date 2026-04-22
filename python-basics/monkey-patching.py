class Math:
    def add(self, x, y):
        return x + y

# Patching a new method at runtime
Math.subtract = lambda self, x, y: x - y