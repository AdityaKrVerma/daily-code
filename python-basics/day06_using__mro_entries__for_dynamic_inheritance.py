class Parent:
    def greet(self):
        return "Hello from Parent!"

class DynamicBase:
    def __mro_entries__(self, bases):
        return (Parent,)

class Child(DynamicBase()):
    pass

c = Child()
print(c.greet())
print(Child.__mro__) 
# Output: (<class 'Child'>, <class 'Parent'>, <class 'object'>)