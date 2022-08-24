from importlib.util import module_for_loader
import os
from typing import Union

from src.loader import load_model


async def get_ai_model(model_id):
    model_ids = os.listdir("models")

    if model_id in model_ids:
        list_of_models = [m for m in os.listdir("models/{}".format(model_id)) if len(m) > 1 and m[0] != "."]
        return load_model(model_id, f"models/{model_id}/{list_of_models[0]}")

    return None
