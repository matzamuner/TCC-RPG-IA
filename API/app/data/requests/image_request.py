from pydantic import BaseModel


class ImageRequest(BaseModel):
    image_context: str