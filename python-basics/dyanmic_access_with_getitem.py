class CustomList:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, index):
        return f"Item {index}: {self.items[index]}"

cl = CustomList(['a', 'b'])
print(cl[0]) # Output: Item 0: a
