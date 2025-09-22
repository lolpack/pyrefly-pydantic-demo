"""
Custom field validator (password complexity).
- Enforces at least 8 chars and a digit.
- Intentional error: 'password' violates rules.
Expected: ValidationError from custom validator.
"""
from pydantic import BaseModel, ValidationError, field_validator

class Signup(BaseModel):
    username: str
    password: str

    @field_validator("password")
    @classmethod
    def check_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("password must be at least 8 characters")
        if not any(ch.isdigit() for ch in v):
            raise ValueError("password must include a digit")
        return v

bad = {"username": "Jethro", "password": "short"}  # <-- invalid

try:
    Signup.model_validate(bad)
except ValidationError as e:
    print("ValidationError from custom validator:")
    print(e)
