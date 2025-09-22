"""
CLI-args-like dict validation.
- Pretend we parsed CLI args into a dict.
- Intentional error: `age` provided as a non-numeric string.
Expected: ValidationError for `age` not being an int.
"""
from pydantic import BaseModel, ValidationError, Field

class Args(BaseModel):
    name: str
    age: int = Field(ge=0)
    verbose: bool = False

parsed = {
    "name": "PyreflyFan",
    "age": "not-a-number",   # <-- invalid
    "verbose": True
}

try:
    Args.model_validate(parsed)
except ValidationError as e:
    print("ValidationError for CLI-like args:")
    print(e)
