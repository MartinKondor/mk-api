from typing import Union

from fastapi import FastAPI

from src.auth import auth
from src.search import get_ai_model


app = FastAPI()


@app.get("/ai/{model_id}")
async def ai(model_id: str, api_key: str, input: str):
    
    # Authentication
    if not await auth(api_key):
        return {
            "s": 0,
            "msg": "Bad API key."
        }

    # Get needed model
    found_model = await get_ai_model(model_id)
    if found_model is None:
        return {
            "s": 0,
            "msg": "Model not found."
        }

    return {
        "s": 1,
        "model": found_model,
        "output": found_model.output(input)
    }


@app.get("/{path_name}")
async def any_path(api_key: Union[str, None]=None):
    return {
        "s": 0,
        "msg": "Bad request."
    }

