import tensorflow as tf
import numpy as np
import os
import cv2
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from numpy import argmax


def get_image(location):
    directory = os.listdir(location)
    
    path = os.path.join(location, directory[0])
    image = cv2.resize(cv2.imread(path, cv2.IMREAD_COLOR), (224, 224))

    return image


def get_features(image):
    model = VGG16(include_top=False)
    image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
    features = model.predict(image)

    return features


def get_caption(features):
    idx_to_word = np.load('website\static\machine_learning\idx_to_word.npy', allow_pickle=True)
    word_to_idx = np.load('website\static\machine_learning\word_to_idx.npy', allow_pickle=True)
    model = tf.keras.models.load_model('website\static\machine_learning\small_train_set')

    in_text = '<startseq>'
    max_len = 16

    for i in range(max_len):
        sequence = [word_to_idx[0][s] for s in in_text.split()]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='post')

        predicted = model.predict([features.reshape(1, -1), sequence.reshape(1, -1)])
        predicted = argmax(predicted)

        word = idx_to_word[0][predicted]

        if word == None:
            break
        if word == '<endseq>':
            break

        in_text += ' ' + word
    return in_text
        


    