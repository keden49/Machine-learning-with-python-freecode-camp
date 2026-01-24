# Titanic Survival Prediction with TensorFlow Linear Classifier

## PROJECT OVERVIEW

The Titanic Survival Prediction project implements a linear classifier using TensorFlow's estimator API to predict passenger survival outcomes based on features such as their age, gender etc. This project demonstrates fundamental machine learning concepts including feature engineering, categorical data encoding, and binary classification using the classic Titanic dataset.

**Note:** This implementation uses TensorFlow 1.x patterns with the legacy estimator API, which has been replaced by TensorFlow 2.x with Keras as the primary high-level API.
 
 CAUTION: THIS MODEL IS OUTDATED (IT DOESNT WORK)
---

## WHAT IS TENSORFLOW

TensorFlow is an open-source machine learning framework developed by Google for building and training machine learning models. It provides a comprehensive ecosystem of tools, libraries, and community resources that enable developers to build and deploys models.

---

## TENSORS

Tensors are the fundamental data structure in TensorFlow, representing multi-dimensional arrays of numerical values. They can be thought of as generalized matrices with varying dimensions:

1. **Scalar**: Single number (0-dimensional tensor)
2. **Vector**: Array of numbers (1-dimensional tensor)
3. **Matrix**: 2-dimensional array of numbers (2-dimensional tensor)
4. **Higher-dimensional tensors**: 3D, 4D, etc., arrays

---

## VISUAL REPRESENTATION OF ARRAYS

**SCALAR (0D):**

[5] [3.14] [-2]



**VECTOR (1D):**
[1, 2, 3, 4, 5]



**MATRIX (2D):**
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

text

**3D TENSOR:**
[[[1, 2],
[3, 4]],
[[5, 6],
[7, 8]]]



---

## CORE OF MACHINE LEARNING

Machine Learning is a subset of artificial intelligence that enables computers to learn patterns from data without being explicitly programmed. Instead of following fixed rules, ML algorithms discover relationships and make predictions based on examples.

---
```
HUMAN APPROACH:                      MACHINE LEARNING APPROACH:
                                   
┌─────────────┐                     ┌─────────────┐
│   Features  │                     │   Features  │
│  (Inputs)   │                     │  (Inputs)   │
└──────┬──────┘                     └──────┬──────┘
       │                                   │
       ▼                                   ▼
┌─────────────┐                     ┌─────────────┐
│   HUMAN     │                     │   MYSTERY   │
│   BRAIN     │                     │   PROCESS   │
│ (Knows the  │                     │  (We don't  │
│   rules)    │                     │   know it)  │
└──────┬──────┘                     └──────┬──────┘
       │                                   │
       ▼                                   ▼
┌─────────────┐                     ┌─────────────┐
│   Answer    │                     │   Answers   │
│  (Output)   │                     │  (Outputs)  │
└─────────────┘                     └─────────────┘
```                                   
    We give:                            We give:
    • Features                          • Features
    • Rules                             • Answers
    → Get Answer                        → Find Rules



---

## UNDERSTANDING MODEL WEIGHTS

**What are Weights?**
Weights are numerical values that represent the importance or influence of each feature in making predictions. 


**How Weights are Learned:**
1. **Initialization**: Weights start as random small numbers
2. **Training**: Model adjusts weights based on prediction errors
3. **Optimization**: Weights move toward values that minimize mistakes
4. **Convergence**: Weights stabilize when model makes accurate predictions

## DATASET

The dataset used for this project comes from the [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data). It consists of the following files:

- `train.csv`: Training data with survival labels.
- `test.csv.xlsx`: Test data with survival labels (used for predictions).

**Note:** I made improvisations on the test data this is by splitting the training data and using a half of it as my testing data as the original test data from kaggle didn't have target labels (survival column).

---

## KEY FEATURES

- `PassengerId`: Unique identifier for each passenger.
- `Survived`: Survival indicator (0 = No, 1 = Yes).
- `Pclass`: Ticket class (1 = First, 2 = Second, 3 = Third).
- `Name`: Passenger name.
- `Sex`: Gender of the passenger.
- `Age`: Age of the passenger.
- `SibSp`: Number of siblings/spouses aboard.
- `Parch`: Number of parents/children aboard.
- `Ticket`: Ticket number.
- `Fare`: Ticket fare.
- `Cabin`: Cabin number.
- `Embarked`: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

---

## STEPS INVOLVED

### A. DATA LOADING
- Upload Titanic dataset files to Colab
- Load training data from CSV and testing data from Excel
- Separate features from target variable 'Survived'

### B. DATA PREPROCESSING

**Categorical Data:**
- Fill missing values: 'Embarked' with 'S', others with mode
- Convert pandas objects to numpy strings for TensorFlow compatibility

**Numeric Data:**
- Fill missing values with median
- Maintain int64/float64 types (TensorFlow compatible)

### C. FEATURE ENGINEERING
- Define categorical columns: 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked', 'Cabin'
- Define numeric columns: 'Age', 'Fare'
- Create TensorFlow feature columns for model input

### D. DATA PIPELINE
- Create input function generator `make_input_fn()`
- Convert DataFrames to TensorFlow datasets
- Add shuffling for training, batching (size 32), and epoch repetition
- Separate pipelines for training (shuffled) and evaluation (ordered)

### E. MODEL TRAINING
- Initialize TensorFlow LinearClassifier with feature columns
- Train model using training data pipeline
- Model learns feature weights through gradient optimization

### F. EVALUATION & PREDICTION
- Generate predictions on evaluation data
- Calculate model accuracy and performance metrics
- Extract survival probability scores
- Analyze results through evaluation statistics

---

## HOW TO RUN

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Titanic-Survival-Linear-Classifier

2.  Install dependencies:
   
```bash
pip install -r requirements.txt
```

3. Run the Colab Notebook:
```
Open Titanic_Estimator_TF2.ipynb
```

FUTURE IMPROVEMENTS

-Implement advanced feature selection techniques

-Experiment with new learning models

ACKNOWLEDGEMENTS

-Kaggle for providing the Titanic dataset

-Free Code Camp

-Open-source libraries and resources used in this project
