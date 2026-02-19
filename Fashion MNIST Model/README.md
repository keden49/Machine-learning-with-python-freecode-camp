# Project Overview 

 This project demonstrates how to build and train a simple neural network using TensorFlow and Keras to classify images from the Fashion MNIST dataset.

# Main Steps Involved 

*1. Data Loading and Exploration*

The Fashion MNIST dataset, consisting of 60,000 training images and 10,000 test images of clothing items, is loaded. Each image is 28x28 pixels. The dataset includes 10 classes of clothing, which are defined with human-readable names like 'T-shirt/top', 'Trouser', 'Pullover', etc.

*2. Data Preprocessing*

The pixel values of the images, originally ranging from 0 to 255, This indexes represent individual pixels on a grayscale, where 0 represents black and 255 represents white and indexes in between represents shades of grey, are scaled down to a range of 0 to 1. This normalization helps the neural network learn more efficiently.

*3. Building Model*

The model has 3 layers, 1 Flatten layer which converts 2D pixel arrays to 1D array for which is essential for the next layers, 2 Dense layers, where the layers are fully connected.

*4. Model Compiling*

 The model is configured for training using:
 
- The adam optimizer - algorithm used to adjust parameters
- sparse_categorical_crossentropy as the loss function, suitable for multi-class classification with integer labels.
- accuracy as the metric to monitor during training.

*5. Model Training*

- The model is trained on the train_images and train_labels for a specified number of epochs (10 in this case). 
- EarlyStopping is implemented as a callback to monitor training accuracy and prevent overfitting, stopping training if the accuracy doesn't improve significantly after a few epochs.

*6. Model Evaluation*

After training, the model's performance is evaluated on the unseen test_images and test_labels to determine its generalization accuracy and loss.

*7. Model Prediction*

The trained model makes predictions on individual test images. The results are then visualized by displaying the image, its true label, and the model's predicted label along with its confidence.

*8. Interactive User Interface*

User is prompted to enter an image number where they can be able to visualie the model's prediction compared to actual label. With helper functions get_number(), show_image(), and predict() facilitate an interactive experience.

# VISUALIZING MODEL ARCHITECTURE AND DATA FLOW


```
             INPUT IMAGE (28x28)
                   ↓
┌─────────────────────────────────────┐
│           FLATTEN LAYER             │
│  ┌──────────────────────────────┐   │
│  │ Takes the 2D image (28x28)   │   │
│  │ and unrolls it into a single │   │
│  │    line of 784 pixels        │   │
│  └──────────────────────────────┘   │
│         ↓                           │
│    Output: 784 numbers              │
│    (each 0-255 for pixel brightness)│
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│          HIDDEN LAYER               │
│  ┌──────────────────────────────┐   │
│  │    128 neurons working       │   │
│  │    together to detect        │   │
│  │  patterns like edges, shapes │   │
│  │                              │   │
│  │    "ReLU" activation:        │   │
│  │   Keeps positive signals,    │   │
│  │    zeros out negatives       │   │
│  └──────────────────────────────┘   │
│         ↓                           │
│    Output: 128 features             │
│    (what patterns were found?)      │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│          OUTPUT LAYER               │
│  ┌──────────────────────────────┐   │
│  │    10 neurons - one for      │   │
│  │    each clothing type:       │   │
│  │  T-shirt, Trouser, Dress, etc│   │
│  │                              │   │
│  │   "Softmax" activation:      │   │
│  │  Converts scores to % that   │   │
│  │   add up to 100% (0-1 each)  │   │
│  └──────────────────────────────┘   │
│         ↓                           │
│    Output: 10 probabilities         │
│    (e.g., 90% shirt, 10% shoe)      │
└─────────────────────────────────────┘
              ↓
           FINAL PREDICTION
         "This is a T-shirt!"
```

# Test the model 🎉

- Click the Colab Badge below

[![Open colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keden49/Machine-learning-with-python-freecode-camp/blob/main/Fashion%20MNIST%20Model/Fashion_Keras.ipynb)

- Click Runtime and then Run all to test out model


# Credits
1. Freecodecamp - For providing the foundational Machine Learning with Python curriculum and project prompts
2. Google Colab: Provided the cloud-based interactive environment for development and easy model testing.
3. TensorFlow: The core machine learning platform used for building and training the deep neural network.
4. Keras: Used for its high-level API to define the model architecture and layers with simplicity and speed.
5. AI Collaborators (Gemini & DeepSeek): Assisted in breaking down complex concepts and greatly helped me to understand the workflow
