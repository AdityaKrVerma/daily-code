DynamicClass = type('DynamicClass', (object,), {'greet': lambda self: "Hello!"})
obj = DynamicClass()
print(obj.greet())