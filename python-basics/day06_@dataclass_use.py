from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0  # Default value