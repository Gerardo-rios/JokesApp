from fastapi import APIRouter

version = APIRouter()


@version.get("/")
async def index() -> dict:
    return {"Index Jokes App Standard Hexagonal Architecture": "0.1"}
