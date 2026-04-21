class Date:
    def __init__(self, day, month, year):
        self.day, self.month, self.year = day, month, year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

new_date = Date.from_string("20-04-2026")
print(f"{new_date.day}-{new_date.month}-{new_date.year}")