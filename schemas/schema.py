from pydantic import BaseModel

class File(BaseModel):
    uuid: str
    name: str
    created_at: None