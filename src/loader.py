import os
import re

from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle


def load_model(model_id, folder_name):
    if model_id == "alhir":
        return load_alhir(folder_name)
    return None


def load_alhir(folder_name):
    
    def clean_str(x):
        text = x.strip()
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
        text = re.sub("[^a-zA-Z0-9öüóőúéáűíÖÜÓŐÚÉÁŰÍ\s]", "", text)
        text = " ".join([l for l in text.split(" ") if l])
        return text.strip()

    keras_trained_model = tf.keras.models.load_model(folder_name + "/keras_trained_model")

    with open(folder_name + "/tokenizer", "rb") as file:
        tokenizer = pickle.load(file)


    def pipeline(x):
        x = clean_str(x)
        x = tokenizer.texts_to_sequences([x])[0]
        x = pad_sequences([x], padding="post", maxlen=21)[0]
        return keras_trained_model.predict([x])[0]

    return {"model": keras_trained_model, "pipeline": pipeline}
