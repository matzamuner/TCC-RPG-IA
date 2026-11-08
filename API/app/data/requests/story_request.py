from pydantic import BaseModel


class StoryRequest(BaseModel):
    selected_model: str
    choice: str