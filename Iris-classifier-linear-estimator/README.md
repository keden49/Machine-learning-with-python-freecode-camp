# DEEP NEURAL NETWORK CLASSIFIER (TENSORFLOW 1.X)
A pre-built TensorFlow estimator for multi-class classification using deep neural networks.

## PROJECT OVERVIEW
This project is part of the FreeCodeCamp Machine Learning with Python Certification curriculum. It implements a Deep Neural Network (DNN) classifier using TensorFlow to predict iris flower species based on four physical measurements. The model classifies flowers into three species: Setosa, Versicolor, and Virginica.

## OBJECTIVE
Build a machine learning model that can accurately classify iris flowers into their correct species based on:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

*NOTE : This version of tensorflow is outdated, tensorflow has migrated to the new high perfomance API Keras. You can find the functional model in my next repository project*

## MODEL ARCHITECTURE 

 *The model has 2 hidden layers*
 
The classifier has 2 hidden layers
- Layer 1 has 30 neurons
- Layer 2 has 10 neurons
- Output layer has 3 neurons (responsible for classification)

*VISUAL REPRESENTATION*

```
Input Features
    │
    ▼
[ • • • • • • • • • • ]  ← 30 neurons (Layer 1)
    │
    ▼
[ • • • • • • • ]  ← 10 neurons (Layer 2)  
    │
    ▼
[ • • • ]               ← 3 neurons (Output Layer)
   ↓  ↓  ↓
 Class0 Class1 Class2
```

## DATASET INFORMATION
- Source: TensorFlow datasets (Google Cloud Storage)
- Training samples: 120 : "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
- Testing samples: 30 : "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"
- Features: 4 numerical features

## DATA PIPELINE CREATION 

To feed data to the model, the data needs to be in a particular format neccessiating the need of a pipeline that converts it to the desired format. Using various tutorials I learnt how to build an Input Pipeline that converts raw tables into Tensors for mathematical processing. This involves Shuffling to prevent the model from memorizing the row order, Mini-Batching to speed up training through parallel processing, and defining Epochs to ensure the network sees the data multiple times to refine its learning.

*This line of code implements it*

```python
def input_fn(features,labels,training=True,batch_size=256):
  ds=tf.Data.Dataset.from_tensor_slices((dict(features),labels))
  if training:
    ds=ds.shuffle(1000).repeat() #repeat shuffling indefinitely
  return ds.batch(batch_size)
```

*Pipeline Architecture*

```
Training Mode:
[Raw Data] → [Convert] → [SHUFFLE] → [BATCH] → [REPEAT ∞] → Model

Testing Mode:
[Raw Data] → [Convert] → [BATCH] → Model
```
## ACKNOWLDGEMENTS

*Thanks To:*

- FreeCodeCamp - For the learning curriculum
- TensorFlow Team - For the ML tools
- GOOGLE Cloud - For the Iris flower data
- Open Source Community - For free tools and help

*Learning Resources:*

- FreeCodeCamp Machine Learning with python course
- TensorFlow documentation
- Online tutorials and guides

*Inspiration:*

- Neural Networks and deep learning 
- Beginner-friendly ML projects


