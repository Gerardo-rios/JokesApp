from fastapi.responses import JSONResponse

import core


async def get_joke(
    get_joke_use_case: core.GetJoke,
) -> JSONResponse:
    try:
        data = await get_joke_use_case.execute()
        return JSONResponse({"data": data}, status_code=200)
    except core.GetJokeException as error:
        return JSONResponse({"error": str(error)}, status_code=500)
