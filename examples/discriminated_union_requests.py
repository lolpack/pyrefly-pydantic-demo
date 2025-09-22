"""
Discriminated union for request bodies (e.g., /pay).
- Uses `kind` as a discriminator.
- Intentional error: `card` kind missing required `last4`.
Expected: ValidationError on card-specific field.
"""
from pydantic import BaseModel, ValidationError, Field
from typing import Literal, Union

class PayByCard(BaseModel):
    kind: Literal["card"]
    brand: Literal["visa", "mc", "amex"]
    last4: str = Field(min_length=4, max_length=4)

class PayByPaypal(BaseModel):
    kind: Literal["paypal"]
    email: str

Payment = Union[PayByCard, PayByPaypal]

bad = {"kind": "card", "brand": "visa"}  # <-- missing last4

try:
    Payment.__get_pydantic_core_schema__  # keeps IDEs happy; not used at runtime
    # v2 way to validate a union payload:
    from pydantic import TypeAdapter
    TypeAdapter(Payment).validate_python(bad)
except ValidationError as e:
    print("ValidationError for discriminated union:")
    print(e)
