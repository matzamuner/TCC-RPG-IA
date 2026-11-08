from fastapi import APIRouter

from app.data.requests.image_request import ImageRequest
from app.services.image_service import generate_image

image_router = APIRouter()


@image_router.post("/")
def image(request: ImageRequest):
    image_b64 = generate_image(request.image_context)
    return {"imageBase64": image_b64}