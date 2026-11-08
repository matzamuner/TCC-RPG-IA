from pydantic import BaseModel


class ItemRequest(BaseModel):
    selected_model: str
    character: str
    item_type: str