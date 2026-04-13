class Student:
    def __init__(self, marks):
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student([90, 80, 85])
print(s1.average())