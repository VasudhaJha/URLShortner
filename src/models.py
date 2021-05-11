from pydantic import BaseModel

class URL(BaseModel):
    long_url: str

class ShortURL(BaseModel):
    short_url: str
    