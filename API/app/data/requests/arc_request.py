from pydantic import BaseModel


class ArcRequest(BaseModel):
    selected_model: str
    last_action: str
    current_arc: int
    is_ending: bool