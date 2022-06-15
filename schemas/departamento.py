from typing import Optional
from pydantic import BaseModel

class Departamento(BaseModel):
    id: Optional[str]
    name: str
    ref : int
