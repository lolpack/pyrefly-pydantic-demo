"""
Nested structures with business rules.
- Inventory items must have quantity >= 1.
- Intentional error: one item has negative quantity.
Expected: ValidationError pointing to items[1].quantity.
"""
from pydantic import BaseModel, ValidationError, Field

class Item(BaseModel):
    sku: str
    quantity: int = Field(ge=1)

class Inventory(BaseModel):
    items: list[Item]

bad = {
    "items": [
        {"sku": "A-100", "quantity": 5},
        {"sku": "B-200", "quantity": -3},  # <-- invalid
    ]
}

try:
    Inventory.model_validate(bad)
except ValidationError as e:
    print("ValidationError for nested list rules:")
    print(e)