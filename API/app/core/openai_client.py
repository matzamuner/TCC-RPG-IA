from functools import lru_cache

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


@lru_cache
def get_openai_client() -> OpenAI:
    return OpenAI()