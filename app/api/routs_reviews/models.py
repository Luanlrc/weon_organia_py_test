from pydantic import BaseModel

class Review(BaseModel):
    id: int
    client_name: str
    avaliation_date: str
    avaliation: str
    avaliation_type: str