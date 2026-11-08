from fastapi import APIRouter

from app.data.requests.story_request import StoryRequest
from app.services.story_service import generate_story

story_router = APIRouter()


@story_router.post("/")
def story(request: StoryRequest):
    return generate_story(
        request.selected_model,
        request.choice,
    )