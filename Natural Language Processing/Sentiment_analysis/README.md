# Project overview 

This project involves a sentiment analysis model which classifies movie reviews as either positive or negative based on the context they hold. Using a dataset of real-world reviews, the model learns to identify patterns in language, tone, and context that reflect human opinions. The goal is to create a system that can automatically analyze feedback and extract meaningful insights, helping to understand customer experiences at scale.

# Model Functionality

This model is built using a TensorFlow Sequential framework. After the input text is converted into sequences of token indices, it is passed into an embedding layer, which transforms each word into a dense, trainable vector representation. These vectors capture semantic relationships, allowing words used in similar contexts to have similar representations. The sequence of embeddings is then processed by an LSTM (Long Short-Term Memory) network, which learns to retain important contextual information while discarding less relevant details through its internal memory states. This enables the model to understand patterns and dependencies across the text.
The learned contextual features are then passed to a dense layer, which interprets this information and produces the final classification. Together, the embedding, LSTM, and dense layers work in sequence to convert raw text into meaningful insights, allowing the model to accurately analyze and classify reviews based on their sentiment.


# IMDB MOVIE REVIEW DATASET 

The model was trained on this specific dataset which holds 25,000 movies reviews from IMDB, labeled by sentiment(positive/negative). Reviews have been preprocessed, and each review is
encoded as a list of word indexes (integers). For convenience, words are indexed by overall frequency in the dataset, so that for instance the integer "3" encodes the 3rd most frequent word in the data. This allows for quick filtering operations such as:"only consider the top 10,000 most common words, but eliminate the top 20 most common words".


# Model Architecture & Flow 

## Blueprint 

<img width="661" height="611" alt="Screenshot 2026-04-02 204423" src="https://github.com/user-attachments/assets/068c3780-8e76-41fe-a9fb-f475d90548e3" />










## Data Flow 

* **Input:** The model accepts a raw text review (e.g., *“That was a great movie”*).
* **Text Vectorization:** Text is tokenized and converted into a sequence of numerical indices, mapping each word to a unique integer.
* **Embedding Layer:** Numerical indices are transformed into dense vector representations, capturing semantic meanings and linguistic relationships.
* **LSTM Layer (Sequential Processing):** The sequence of word vectors is processed through an **LSTM** network to capture long-range dependencies and contextual information.
* **Dense Layer:** High-level features learned by the LSTM are passed to a fully connected (dense) layer for refinement and feature combination.
* **Classification Output:** The final layer produces a prediction, classifying the input as **Positive** or **Negative**.



# Future Aspirations

Moving forward, I aim to scale this project by training the model on larger and more diverse datasets, such as publicly available movie review datasets from platforms like Kaggle, to improve its accuracy and generalization. Expanding to datasets similar to those used in Rotten Tomatoes analysis will allow the model to better capture a wider range of opinions and writing styles.I also plan to develop a simple user interface that will enable users to input their own reviews and receive real-time sentiment classifications. This will enhance the model’s usability and demonstrate its practical application in analyzing feedback dynamically.


