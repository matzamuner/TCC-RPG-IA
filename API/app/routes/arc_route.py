from fastapi import APIRouter

from app.data.requests.arc_request import ArcRequest
from app.services.arc_service import generate_arc

arc_router = APIRouter()


@arc_router.post("/")
def arc(request: ArcRequest):
    return generate_arc(
        request.selected_model,
        request.last_action,
        request.current_arc,
        request.is_ending,
    )