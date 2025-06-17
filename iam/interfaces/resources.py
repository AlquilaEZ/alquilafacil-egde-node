from pydantic import BaseModel

class TokenResource(BaseModel):
    id: int
    username: str
    token: str