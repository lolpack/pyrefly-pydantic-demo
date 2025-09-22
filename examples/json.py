"""
JSON payload validation (e.g., API input).
- Validates a list of users, each with id/email.
- Intentional error: one email is invalid.
Expected: ValidationError pointing to users[1].email.
"""
from pydantic import BaseModel, EmailStr, ValidationError

class User(BaseModel):
    id: int
    email: EmailStr

class BulkUsers(BaseModel):
    users: list[User]

incoming = {
    "users": [
        {"id": 1, "email": "alice@example.com"},
        {"id": 2, "email": "not-an-email"},  # <-- invalid
        {"id": "3", "email": "not-an-email"}  # <-- invalid
    ]
}

try:
    BulkUsers.model_validate(incoming)
except ValidationError as e:
    print("ValidationError for JSON payload:")
    print(e)
