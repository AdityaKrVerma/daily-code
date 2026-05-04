class Multiplier:
    def __init__(self, value):
        self.value = value
    def __rmul__(self, other):
        # Handles: 5 * Multiplier(10)
        return self.value * other

m = Multiplier(10)
print(5 * m) # 50