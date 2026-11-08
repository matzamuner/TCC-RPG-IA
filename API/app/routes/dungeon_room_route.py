from fastapi import APIRouter

from app.data.requests.dungeon_room_request import DungeonRoomRequest
from app.services.dungeon_room_service import generate_dungeon_room

dungeon_room_router = APIRouter()


@dungeon_room_router.post("/")
def dungeon_room(request: DungeonRoomRequest):
    return generate_dungeon_room(
        request.selected_model,
        request.context,
    )