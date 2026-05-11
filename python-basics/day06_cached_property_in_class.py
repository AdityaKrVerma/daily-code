from functools import cached_property


class Report:
    def __init__(self, numbers):
        self.numbers = tuple(numbers)

    @cached_property
    def total(self):
        print("Calculating...")
        return sum(self.numbers)


r = Report([10, 20, 30])

print(r.total)  # Calculating... 60
print(r.total)  # 60, no recalculation

del r.total
print(r.total)  # Calculating... 60