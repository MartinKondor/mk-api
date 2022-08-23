from typing import Union


API_KEYS = [
    "0pfAOhvat2B5B2Z8",  # DigitRecognizer
    "9eL3IrQEu63Wa2uB"
]

async def auth(api_key: Union[str, None]):
    return True  # TODO
    if api_key is None:
        return False
    return api_key not in API_KEYS
