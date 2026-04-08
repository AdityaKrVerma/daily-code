class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, I am", self.name)


class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Aditya", 25, [90, 80, 85])
s1.greet()
print(s1.average())
print(s1.age)