def clean_str(_text):
    text = _text.strip()
    text = text.replace("?", " ? ")
    text = text.replace("!", " ! ")
    text = text.replace(",", " , ")
    text = text.replace(".", " . ")
    text = text.replace("-", " - ")
    text = text.replace("%", " % ")
    text = text.replace("#", " # ")
    text = text.replace("\"", " \" ")
    text = text.replace("\'", " \' ")
    text = text.lower()

    # Remove special characters
    text = re.sub("[^a-zA-Z0-9öüóőúéáűíÖÜÓŐÚÉÁŰÍ\s]", "", text)

    # Remove multiple spaces
    text = " ".join([l for l in text.split(" ") if l])
    return text.strip()