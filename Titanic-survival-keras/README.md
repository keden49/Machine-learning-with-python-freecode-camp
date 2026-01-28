## PROJECT OVERVIEW 
This project implements a deep learning solution to predict passenger survival on the Titanic using Keras and TensorFlow. The model analyzes passenger features like age, gender, ticket class, and fare to determine their likelihood of survival with a 80% accuracy.

## KERAS 
Keras is an open-source, high-level neural network API written in Python. It's designed for fast experimentation with deep learning models, running on top of backend frameworks like TensorFlow.

## LAYERS
Layers in deep learning are the foundational, stacked modules of an artificial neural network that process, transform, and extract features from data to make predictions. They consist of nodes (neurons) connected by weights, organizing the network into input, multiple hidden, and output layers. Each layer transforms inputs via weighted sums and activation functions to learn complex representations.

```
TITANIC SURVIVAL PREDICTOR
══════════════════════════════════════════════

INPUT FEATURES (7)
┌─────────────────────────────────────────────┐
│ Age: 22      ──────────────┐                │
│ Sex: Female  ─────────────┐│                │
│ Pclass: 1    ────────────┐││                │
│ Fare: 150    ───────────┐│││                │
│ SibSp: 0     ──────────┐││││                │
│ Parch: 0     ─────────┐│││││                │
│ Embarked: S  ────────┐││││││                │
│ Title: Miss  ───────┐│││││││                │
│ FamilySize: 1 ─────┐││││││││                │
│ AgeGroup: Adult  ─┐│││││││││                │
│ HasCabin: Yes  ─┐│││││││││││                │
└─────────────────▼▼▼▼▼▼▼▼▼▼▼▼────────────────┘
                  ││││││││││││
                  ▼▼▼▼▼▼▼▼▼▼▼▼
           ┌─────────────────────┐
           │   HIDDEN LAYER 1    │
           │     64 Neurons      │
           │      ReLU + Dropout │
           └─────────────────────┘
                  ││││││││││
                  ▼▼▼▼▼▼▼▼▼▼
           ┌─────────────────────┐
           │   HIDDEN LAYER 2    │
           │     16 Neurons      │
           │      ReLU + Dropout │
           └─────────────────────┘
                 
                  ││││
                  ▼▼▼▼
           ┌─────────────────────┐
           │    OUTPUT LAYER     │
           │     1 Neuron        │
           │      Sigmoid        │
           └─────────────────────┘
                  │
                  ▼
           ┌──────────────┐
           │ Probability  │
           │    0.85      │
           │  (85% yes)   │
           └──────────────┘
                  │
                  ▼
           PREDICTION: SURVIVED
```

## NEURAL NETWORKS: THE BRAIN INSPIRED AI 

A neural network is a computer system designed to learn patterns like a brain does. It's made of interconnected "neurons" (mathematical functions) that work together to recognize patterns, make predictions, or classify data.

## NEURONS ARCHITECTURE 
```
TITANIC NEURAL NETWORK (7-64-16-1)
══════════════════════════════════════════════════════

INPUT (7 features)      HIDDEN 1 (64)     HIDDEN 2 (16)      OUTPUT (1)
○○○○○○○○○○○             ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○Age○Sex○Pclass○        ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○○○○○○○○○○○○○           ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○Fare○SibSp○Parch○      ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○○○○○○○○○○○○○           ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○Emb○Title○FamSize○     ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○○○○○○○○○○○○○           ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○AgeGr○HasCabin○        ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
○○○○○○○○○○○             ○○○○○○○○○○○○○○    ○○○○○○○○○○○○○○        ○
   │    │    │               │    │    │        │    │   │       │    │    │      
   ▽   ▽    ▽              ▽    ▽   ▽        ▽   ▽   ▽      ▽    ▽   ▽     
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             FULLY CONNECTED (DENSE LAYER)                        │
│  Each ○ in input connects to EVERY ○ in next layer                               │
│                                                                                  │
│  ○───────○───────○───────○───────○───────○───────○───────○───────○───────○       │
│  │\     ╱│\     ╱│\     ╱│\     ╱│\     ╱│\     ╱│\     ╱│\     ╱│\     ╱│       │
│  │ \   ╱ │ \   ╱ │ \   ╱ │ \   ╱ │ \   ╱ │ \   ╱ │ \   ╱ │ \   ╱ │ \   ╱ │       │
│  │  \ ╱  │  \ ╱  │  \ ╱  │  \ ╱  │  \ ╱  │  \ ╱  │  \ ╱  │  \ ╱  │  \ ╱  │       │
│  │   ╳   │   ╳   │   ╳   │   ╳   │   ╳   │   ╳   │   ╳   │   ╳   │   ╳   │       │
│  │  ╱ \  │  ╱ \  │  ╱ \  │  ╱ \  │  ╱ \  │  ╱ \  │  ╱ \  │  ╱ \  │  ╱ \  │       │
│  │ ╱   \ │ ╱   \ │ ╱   \ │ ╱   \ │ ╱   \ │ ╱   \ │ ╱   \ │ ╱   \ │ ╱   \ │       │
│  │╱     \│╱     \│╱     \│╱     \│╱     \│╱     \│╱     \│╱     \│╱     \│       │
│  ○───────○───────○───────○───────○───────○───────○───────○───────○───────○       │
│                                                                                  │
│  WEIGHTS: Lines between circles represent weights (w₁, w₂, w₃, ...)              │
│  BIAS: Each circle has a +b added to its calculation                             │
└──────────────────────────────────────────────────────────────────────────────────┘
```
## NEURONS 
In a Dense layer, a neuron is a simple function that does three things:
- Collects inputs: It takes all the data points from the previous step (like Age, Sex, and Fare).
  
- Multiplies by Weights: It gives each input a "volume" control. If "Sex" is important for survival, that input gets a high weight.
  
- Adds a Bias: This is an "offset" that allows the neuron to shift its decision-making threshold.
  
- Applies Activation: It runs the total through a function (like ReLU) to decide what to pass to the next layer.

## ReLU (Rectified Linear Unit)
Activation function in deep learning. It outputs the input directly if positive, and zero otherwise. Its important for adding non-linearity, hence recognizing more complex relationships between features

The "Expansion" (Wide layers): Early layers usually have more neurons (like 64 or 128) to capture every possible tiny detail and combination of your data.
Activation (ReLU): It filters out the "noise." If a specific combination of features doesn't look like a survival pattern, the ReLU turns that neuron off (outputs 0).

The "Compression" (Narrow layers): As you get deeper, you reduce the number of neurons. This forces the model to summarize its findings. You want it to stop looking at "raw numbers" and start looking at "concepts" 

## Sigmoid (Used in the final layer):
The Logic: "Take any number and squash it between 0 and 1."

## STEPS INVOLVED 
1. Data Loading

- loaded training data(train.csv)
- loaded testing data(test.csv)

2. Data Preprocessing

- Encoded Categorical columns(Sex,alone,Cabin)

3. Model Creation

- imported Keras Dense layers
- Created Sequential container
- Defined input,hidden and output layers

4. Compiled Model

The model.compile() method in Keras (part of the TensorFlow library) is used to configure the model for training by specifying essential components: an optimizer, a loss function, and optional metrics

**Key arguments**
- optimizer-defines algorithms of how model will adjusts its weights
- loss function- defines how far the models prediction is far from the actual
- metrics

5. Established Callbacks

In this model I implemented Callbacks specifically EarlyStopping and ModelCheckpoint. The former is responsible for stopping training when the models perfomance stops improving while the latter is responsible for saving the model only when it improves.

6. Model Training

The model is fitted with the training data and labels as well as no of epochs and validation data(evaluation data) to check models progress on unseen data.

7. Using Model

Saved model through model.save() and imported it through loaded model. Then tested the accuracy by creating a copy of the evaluation data. 

## MODEL'S ACCCURACY 

The model was able to achieve an accuracy of exactly 78.03%. I decided to settle on this accuracy level so as to prevent overfitting .

## ACKNOWLEGEMENTS

- **Kaggle** for the Titanic dataset
- **TensorFlow/Keras** for the deep learning framework
- **Open-source community** for invaluable tools and resources
- **Online learning platforms** that make data science education accessible

