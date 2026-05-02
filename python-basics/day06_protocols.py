from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self): print("Drawing Circle")

def render(shape: Drawable):
    shape.draw()

render(Circle())  # Works because Circle matches the Protocol