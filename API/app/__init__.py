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
"""
from flask import Flask

from app.routes.image_route import image_blueprint
from app.routes.main_story_route import main_story_blueprint
from app.routes.arc_route_py import arc_blueprint
from app.routes.story_route import story_blueprint
from app.routes.dungeon_room_route import dungeon_room_blueprint
from app.routes.character_route import character_blueprint
from app.routes.item_route import item_blueprint

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_story_blueprint, url_prefix="/generate/main_story")
    app.register_blueprint(arc_blueprint, url_prefix="/generate/arc")
    app.register_blueprint(story_blueprint, url_prefix="/generate/story")
    app.register_blueprint(dungeon_room_blueprint, url_prefix="/generate/dungeon_room")
    app.register_blueprint(character_blueprint, url_prefix="/generate/character")
    app.register_blueprint(item_blueprint, url_prefix="/generate/item")
    app.register_blueprint(image_blueprint, url_prefix="/generate/image")

    return app"""