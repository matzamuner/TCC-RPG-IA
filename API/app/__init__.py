from fastapi import FastAPI

from app.routes.character_route import character_router
from app.routes.arc_route import arc_router
from app.routes.dungeon_room_route import dungeon_room_router
from app.routes.item_route import item_router
from app.routes.story_route import story_router
from app.routes.main_story_route import main_story_router
from app.routes.image_route import image_router

def create_app():
    app = FastAPI()

    app.include_router(
        character_router,
        prefix="/generate/character",
        tags=["Character"],
    )

    app.include_router(
        arc_router,
        prefix="/generate/arc",
        tags=["Arc"],
    )

    app.include_router(
        dungeon_room_router,
        prefix="/generate/dungeon_room",
        tags=["Dungeon Room"],
    )

    app.include_router(
        item_router,
        prefix="/generate/item",
        tags=["Item"],
    )

    app.include_router(
        story_router,
        prefix="/generate/story",
        tags=["Story"],
    )

    app.include_router(
        main_story_router,
        prefix="/generate/main_story",
        tags=["Main Story"],
    )

    app.include_router(
        image_router,
        prefix="/generate/image",
        tags=["Image"],
    )

    return app