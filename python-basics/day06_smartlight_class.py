class SmartLight:
    def __init__(self, room_name):
        self.room = room_name
        self.is_on = False
        self.brightness = 0

    def toggle(self):
        self.is_on = not self.is_on
        self.brightness = 100 if self.is_on else 0
        state = "shining bright" if self.is_on else "off"
        return f"The {self.room} light is now {state}."

kitchen_light = SmartLight("Kitchen")
print(kitchen_light.toggle())