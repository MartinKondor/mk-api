import re


def clean_str(_text):
    text = _text.replace(".", ". ")
    text = text.replace("?", "? ")
    text = text.replace("!", "! ")
    text = text.replace(",", ", ")
    #text = text.lower()

    # Replace numbers with an x
    text = re.sub("[0-9]+", "x", text)

    # Remove characters
    text = re.sub("[^a-zA-Z0-9öüóőúéáűí\s]", "", text)

    # Remove multiple spaces
    text = " ".join([l for l in text.split(" ") if l])
    return text.strip()
