"""
YAML config validation with nested models and type enforcement.
- Parses an inline YAML string (requires `pip install pyyaml`).
- Validates fields/types with Pydantic.
- Intentional error: `server.port` is a string instead of an int.
Expected: Pydantic raises a ValidationError on `server.port`.
"""
from pydantic import BaseModel, ValidationError, Field
import yaml

class Server(BaseModel):
    host: str
    port: int = Field(ge=1, le=65535)
    debug: bool = False

class Database(BaseModel):
    url: str
    pool_size: int = Field(ge=1, le=100)

class AppConfig(BaseModel):
    server: Server
    database: Database

yaml_text = """
server:
  host: "0.0.0.0"
  port: "8000"   # <-- wrong type on purpose; should be an int
  debug: true
database:
  url: "postgresql://user:pass@localhost:5432/app"
  pool_size: 10
"""

data = yaml.safe_load(yaml_text)

try:
    AppConfig.model_validate(data)
except ValidationError as e:
    print("ValidationError for YAML config:")
    print(e)
