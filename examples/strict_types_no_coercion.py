"""
Strict type validation (no coercion).
- Configure model to disallow coercing "123" -> 123.
- Intentional error: `count` passed as a string.
Expected: ValidationError for strict int.
"""
from pydantic import BaseModel, ValidationError, ConfigDict

class StrictNumbers(BaseModel):
    model_config = ConfigDict(strict=True)  # turn on strict validation
    count: int

bad = {"count": "123"}  # <-- invalid under strict mode

try:
    StrictNumbers.model_validate(bad)
except ValidationError as e:
    print("ValidationError with strict types (no coercion):")
    print(e)
