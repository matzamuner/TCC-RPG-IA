from fastapi import APIRouter

from app.data.requests.main_story_request import MainStoryRequest
from app.utils.context_helper import clear_context
from app.services.main_story_service import generate_main_story

main_story_router = APIRouter()


@main_story_router.post("/")
def main_story(request: MainStoryRequest):
    clear_context("context.txt")
    return generate_main_story(
        request.selected_model,
        request.type,
        request.name,
        request.character_history,
        request.context,
    )