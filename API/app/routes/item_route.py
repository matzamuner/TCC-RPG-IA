from fastapi import APIRouter

from app.data.requests.item_request import ItemRequest
from app.services.item_service import generate_item

item_router = APIRouter()


@item_router.post("/")
def item(request: ItemRequest):
    return generate_item(
        request.selected_model,
        request.character,
        request.item_type,
    )