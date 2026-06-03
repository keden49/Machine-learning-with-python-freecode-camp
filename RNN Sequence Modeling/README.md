# 🎭 Character-Based Play Generator (RNN)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keden49/Machine-learning-with-python-freecode-camp/blob/main/RNN%20Sequence%20Modeling/Play_Generator_RNN.ipynb)

##  Project Overview
This project explores how a reccurrent neural network can be used to generate human-like text. It focuses on training a model to predict the next character in a sequence, allowing it to produce new text that mimics the style and structure of the original data.

For this specific project the model is trained on a play by Shakespeare, instead of working with full words, the model learns from individual characters. This approach helps it capture subtle patterns in writing, such as punctuation, rhythm, and stylistic expression. By training on a Shakespearean play, the model learns to generate text that reflects the tone,voice and sentence structure of classical literature.

---

##  Training Data: *Coriolanus*
The model is trained on the text of Shakespeare’s *Coriolanus*, a play centered on themes of power, pride, and conflict.

**Plot Summary:**  
The story follows Caius Marcius, a respected Roman general whose strength in battle contrasts with his difficult relationship with the public. His pride leads to his exile, after which he joins opposing forces in an attempt to attack Rome. In the end, he chooses mercy over revenge, a decision that ultimately costs him his life.


---

##  Model Architecture

### 1. Embedding Layer
This layer converts each unique character into a dense vector numerical representation. This captures complex relationships between characters.

### 2. LSTM Layer
This is the core of the model. It processes sequences of characters while keeping track of context from earlier in the text in its hidden state memory. This allows the model to maintain consistency and generate more coherent sequences over time.

### 3. Dense Layer
The final layer uses the learned patterns to decide which character is most likely to come next. It produces a prediction based on everything the model has learned from the input sequence.

---

##  Data Flow 

1. **Character Encoding & Representation:**  
   Each character in the text is first mapped to a unique integer index. These indices are then passed through an embedding layer, which converts them into dense vector representations. This allows the model to capture relationships between characters in a continuous vector space rather than treating them as isolated symbols.

2. **Sequence Construction:**  
   The full text is segmented into fixed-length input sequences (e.g., 100 characters). For each input sequence, a corresponding target sequence is created by shifting the text one step forward. This structure enables the model to learn sequential dependencies.

3. **Pattern Learning (Training Phase):**  
   The model is trained to predict the probability distribution of the next character at each time step. Using backpropagation through time (BPTT), the LSTM updates its internal weights by minimizing prediction error, allowing it to learn both short-term and long-term dependencies in the text.

4. **Text Generation (Inference Phase):**  
   Once trained, the model generates text by taking an initial input (seed text) and iteratively predicting the next character. Each predicted character is fed back into the model as input, creating a continuous generation loop that produces coherent sequences.

   *Visual Implementation*


   <img width="810" height="285" alt="image" src="https://github.com/user-attachments/assets/3bef4eb6-6e41-49e1-aa51-f113350071d6" />


6. **Sampling & Creativity Control (Temperature Scaling):**  
   The output probabilities are adjusted using a temperature parameter before sampling the next character. Lower temperatures make the process of generating the next character random this allows the model to be creative when generating a play, while higher temperatures introduce more randomness, increasing diversity at the cost of coherence.

---

## Visual Model Architecture and Data flow 

*Source*: [Tensorflow](https://www.tensorflow.org/text/tutorials/text_generation)


<img width="838" height="679" alt="image" src="https://github.com/user-attachments/assets/f9dcd9d4-2538-46e6-9e7d-9c9d05abe567" />


##  How To Use

1. **Open the Notebook:** Click the **Open In Colab** badge above.
2. **Run the Code:** Select **Runtime → Run all** to execute the notebook.
3. **Train the Model:** The model will begin learning from the dataset. This may take a few minutes.
4. **Generate Text:** At the end of the notebook, enter a word or phrase as a starting point.
5. **View Results:** The model will generate a play based on your input.


> [!NOTE]  
> **On Text Coherence:** While the model mimics the structure, tone, and formatting of a play, the generated text may not always be fully coherent or logical. This is because the model is trained on a limited dataset (a single play) and learns character-by-character rather than by word or concept. Greater coherence would require a more robust and diverse training dataset.


---

## Credits
- **freeCodeCamp:** Machine Learning with Python Curriculum  
- **TensorFlow:** Deep learning framework used to build the model and comprehensive documentation
- **Andrej Karpathy:** Influential Researcher in Neural Networks [Vanilla RNN](https://gist.github.com/karpathy/d4dee566867f8291f086) 
