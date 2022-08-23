import os
from typing import Union


async def get_ai_model(model_id):
    model_ids = os.listdir("models")

    if model_id in model_ids:
        # TODO
        pass

    return None
