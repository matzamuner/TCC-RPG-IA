from pydantic import BaseModel


class MainStoryRequest(BaseModel):
    selected_model: str
    type: str
    name: str
    character_history: str
    context: str