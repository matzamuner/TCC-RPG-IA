from fastapi import APIRouter

from app.data.requests.character_request import CharacterRequest
from app.services.character_service import generate_character

character_router = APIRouter()


@character_router.post("/")
def character(request: CharacterRequest):
    return generate_character(
        request.selected_model,
        request.level,
        request.context,
    )