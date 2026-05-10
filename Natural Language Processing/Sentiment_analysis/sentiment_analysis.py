# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow import keras
from keras.datasets import imdb

VOCAB_SIZE = 88584

(train_data,train_labels) ,(test_data,test_labels) = imdb.load_data(num_words=VOCAB_SIZE)

train_data.shape

word_index = imdb.get_word_index()
vocab= list(word_index.items())[:10]
vocab.sort(key = lambda x:x[1])
print(vocab)

index2word = {}

indexes = word_index.values()
words  = word_index.keys()

for index,word in zip(indexes,words):
  index2word[index] = word

reversed_vocab = list(index2word.items())[:10]
reversed_vocab.sort()
print(reversed_vocab)

test_review = train_data[24555]
word_review = ""
for number in test_review:
  word = index2word[number]
  word_review += word + " "

print(word_review)

test_review = train_data[24555]
words_list = []
for number in test_review:
  word = index2word[number]
  words_list.append(word)
word_review = " ".join(words_list)
print(word_review)

index2word = {
    0: "<pad>",
    1: "<sos>",
    2: "<unk>"
}

word_index_original = imdb.get_word_index()

for word, index in word_index_original.items():
  index2word[index + 3] = word

print(list(index2word.items())[:10])

test_review = train_data[25]
words_list = []
for number in test_review:
  word = index2word[number]
  words_list.append(word)
word_review = " ".join(words_list)
print(word_review)

MAXLEN = 250

from keras.preprocessing import sequence

train_data = sequence.pad_sequences(train_data,MAXLEN,padding = 'post',truncating = 'post')
test_data = sequence.pad_sequences(test_data,MAXLEN,padding = 'post',truncating = 'post')

test_data.shape

maxlen = max(len(sent) for sent in train_data)
print(maxlen)

input_dim = len(imdb.get_word_index())
input_dim == VOCAB_SIZE

input_dim = len(imdb.get_word_index())
output_dim = 32
from tensorflow.keras.layers import Embedding,LSTM,Dense
from tensorflow.keras import Sequential

model = Sequential([Embedding(input_dim,output_dim, mask_zero=True),
                    LSTM(32),
                    Dense(1, activation = "sigmoid")])

model.build(input_shape=(None, MAXLEN))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(train_data, train_labels, epochs=10, validation_split=0.2)

model.evaluate(test_data, test_labels)

text = "that movie was just amazing, so amazing"
tokens = keras.preprocessing.text.text_to_word_sequence(text)
print(tokens)

word2index = {word:index for index,word in index2word.items()}
def encode(text):
  tokens = keras.preprocessing.text.text_to_word_sequence(text)
  tokens = [word2index[word] if word in word2index else 2 for word in tokens]
  return sequence.pad_sequences([tokens],maxlen,padding = 'post')

example_reviews = ["Bro this movie is boring","I love this movie","this movie is amazing","I hate this movie","That movie was just amazing, so amazing! I really loved it and would great watch it again because it was amazingly great","that movie really sucked. I hated it and wouldn't watch it again. Was one of the worst things I've ever watched"]

for review in example_reviews:
  encoded_review = encode(review)
  prediction = model.predict(encoded_review)
  prediction = prediction[0][0]
  if prediction >= 0.5:
    print(f"The review is {100*prediction:.2f}% positive")
    print(review)
  else:
    print(f"The review is only {100*prediction:.2f}% positive")
    print(review)

word_index['i']

print(index2word)

text = encode(('Bro'))
pred = model.predict(text)
print(pred)

def predict(text):
  encoded_text = encode(text)
  pred  = model.predict(encoded_text)
  pred = pred[0][0]

  if pred >= 0.5:
    return f" According to the models analysis the movie review is {100*pred:.2f}% positive"
  else:
    return f"According to the models analysis the movie review is only {100*pred:.2f}% positive"

user_input= input("Type your desired movie review(eg. I love Spiderman the movie):")
result = predict(user_input)

print("\n--- MODEL ANALYSIS ---")
print(f"REVIEW: {user_input}")
print(f"RESULT: {result}")
print("----------------------")

print(user_input)