from pydantic import BaseModel


class DungeonRoomRequest(BaseModel):
    selected_model: str
    context: str