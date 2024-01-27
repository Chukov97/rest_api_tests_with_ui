from pydantic import BaseModel


class Credentials(BaseModel):
    Email: str
    Password: str
