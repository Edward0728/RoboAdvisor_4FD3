import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

communications = json.loads(open('communications.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for communication in communications['intents']:
    for pattern in communication['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, communication['tag']))
        if communication['tag'] not in classes:
            classes.append(communication['tag'])

print(documents)