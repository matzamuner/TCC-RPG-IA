from pydantic import BaseModel


class CharacterRequest(BaseModel):
    selected_model: str
    level: int
    context: str