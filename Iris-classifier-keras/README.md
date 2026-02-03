## DEEP NEURAL NETWORKS (TENSORFLOW 2.X)

A Deep Neural Network is an artificial intelligence architecture composed of multiple layers of interconnected processing units (neurons) that transform input data through successive non-linear transformations to learn hierarchical representations and patterns. This project implements a Deep Neural Network using TensorFlow's Keras API a modern shift from older frameworks that provides intuitive, layer-by-layer model building

## PROJECT OVERVIEW
This project is part of the FreeCodeCamp Machine Learning with Python Certification curriculum. It implements a Deep Neural Network (DNN) classifier using TensorFlow to predict iris flower species based on four physical measurements. The model classifies flowers into three species: Setosa, Versicolor, and Virginica.

## OBJECTIVE
Build a machine learning model that can accurately classify iris flowers into their correct species based on:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

  ## MODEL'S ARCHITECTURE
```
  INPUT DATA (Features)
      |
      v
┌─────────────────┐
│   LAYER 1       │
│   30 Neurons    │ ← Hidden Layer 1
│   (ReLU/etc.)   │
└─────────────────┘
      |
      v
┌─────────────────┐
│   LAYER 2       │
│   10 Neurons    │ ← Hidden Layer 2  
│   (ReLU/etc.)   │
└─────────────────┘
      |
      v
┌─────────────────┐
│   OUTPUT LAYER  │
│   3 Neurons     │ ← One for each class
│   (Softmax)     │
└─────────────────┘
      |
      v
[Class 0, Class 1,  Class 2]
      |    |         |
    Setosa Virginica Versicolor
```

## MODEL'S MECHANISM 

The model operates through a process called Forward Propagation, where data travels from the input through hidden transformations to the final output.

*1. The Input: Feature Injection*

The model collects the Iris Input Features this includes four dimensions: Sepal Length, Sepal Width, Petal Length, and Petal Width. These values are fed into the network as a numerical vectors(tensors).

*2. Layer 1: Feature Extraction (30 Neurons)*

- Weighted Sum: Each of the 30 neurons receives all input features. Every connection has an associated Weight ($w$) and Bias ($b$). The neuron calculates:

```
z = sum(input + w)+b
```
- Activation (ReLU): To allow the model to learn complex, non-linear patterns, the Rectified Linear Unit (ReLU) function is applied. It keeps positive values as-is and turns negative values to zero, helping the network decide which features are "firing" or relevant.

*3. Layer 2: Dimensionality Reduction (10 Neurons)*

The 30 signals from the first layer are compressed into 10 neurons. This layer acts as a bottleneck, forcing the network to keep only the most vital information. It refines the "high-level" patterns identified in Layer 1 before passing them to the final decision-maker.

*4. The Output Layer: Softmax Classification*

The final layer consists of 3 neurons—one for each Iris class (Setosa, Virginica, Versicolor).

Activation Softmax :

It takes raw numbers (logits) coming out of the last layer these numbers into probabilities which add up tp 1 

Example
```
[[0.02, 0.95, 0.03]]
```

## Weight Optimization: How the Model "Learns"

- Loss Calculation: The model makes a prediction, compares it to the actual label using a Loss Function for this case Categorical Cross-Entropy
- Backpropagation: The "error" is sent backward through the network.
- Optimizer (e.g., Adam or SGD): The optimizer nudges the weights in the direction that reduces the error. Over hundreds of iterations (epochs), the weights are tuned until the model can accurately map inputs to the correct flower species.

# DATASET INFORMATION
- Source: TensorFlow datasets (Google Cloud Storage)
- Training samples: 120 : "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
- Testing samples: 30 : "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"
- Features: 4 numerical features




# IRIS SPECIES CLASSIFIER BADGE
*Test the dnn classifier*:tada:
```
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keden49/Machine-learning-with-python-freecode-camp/blob/main/Iris-classifier-keras/Iris_Keras.ipynb)
```
## HOW TO TEST THE MODEL
1. Click the **Open in Colab** badge above.
2. Go to **Runtime > Run All**.
3. The first cell will automatically download the pre-trained weights from this repo.
4. Scroll to the bottom to use the **Interactive UI** and enter your own flower measurements!

## BUILT WITH 
Special thanks to the following platforms and tools that made this project possible:

1. Google Colab: Provided the cloud-based interactive environment for development and easy model testing.
2. TensorFlow: The core machine learning platform used for building and training the deep neural network.
3. Keras: Used for its high-level API to define the model architecture and layers with simplicity and speed.
4. AI Collaborators (Gemini & DeepSeek): Assisted in breaking down complex concepts and greatly helped me to understand the workflow
