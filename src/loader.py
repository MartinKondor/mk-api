import os

import pickle
import tensorflow as tf


def load_model(model_id, folder_name):
    if model_id == "alhir":
        return load_alhir(folder_name)
    return None


def load_alhir(folder_name):
    keras_trained_model = tf.keras.models.load_model(folder_name + "/keras_trained_model")

    with open(folder_name + "/tokenizer", "rb") as file:
        tokenizer = pickle.load(file)

    pipeline = lambda x: keras_trained_model.predict([tokenizer.texts_to_sequences([x])[0]])[0]
    return {"model": keras_trained_model, "pipeline": pipeline}
