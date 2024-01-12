from fastapi.responses import JSONResponse

import core


async def get_joke(
    get_joke: core.GetJoke,
) -> JSONResponse:
    try:
        return JSONResponse({"data": get_joke()}, status_code=200)
    except core.GetJokeException as error:                        
        return JSONResponse({"error": str(error)}, status_code=500)
        
