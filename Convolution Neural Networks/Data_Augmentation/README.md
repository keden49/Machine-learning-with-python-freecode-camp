# Folder Overview

## Overview
This folder presents a comparative analysis of eight Convolutional Neural Network (CNN) models trained for CIFAR-10 image classification. The primary objective is to evaluate the impact of data augmentation and increased model complexity on classification performance and generalization capabilities. On each test one model is trained on a non-augmented dataset, while the other utilizes a data-augmented dataset and a more complex architecture.

## Non-Augmented Model

### Model Setup
The non-augmented model, this model is trained on the orginal training data. The model was trained for 50 epochs, with 1000 steps per epoch. The architecture consists of three `Conv2D` layers (all with 64 filters), interleaved with `MaxPooling2D` layers. This is followed by a `Flatten` layer and two `Dense` layers, with 64 and 10 neurons respectively. ReLU activation functions were used for hidden layers, and a softmax activation function for the output layer. The total number of trainable parameters for this model was 141,998.
Its acted as a control experiment to evaluate if data augmentation actually has an effect on the model's overall perfomance.

### Performance
Upon completion of training, the non-augmented models achieved higher training accuracy. However, performance on the unseen test dataset was significantly lower, yielding a final validation/test accuracy of approximately 68.31% and a final test loss of 2.193. This substantial discrepancy between training and test accuracy indicates a clear instance of overfitting, where the model learned the training data too well but struggled to generalize to new data. This can be observed in the following line graph below. The models accuracy does very well on training accuracy but perfomance declines on validation accuracy with increase in epochs.


<img width="1159" height="454" alt="image" src="https://github.com/user-attachments/assets/f36e7b3a-82a8-4b26-a6cf-f97d05e80b24" />


## Augmented Model

### Model Setup
The augmented models were trained on 50 t0 75 epochs, with 1000 steps per epoch. To enhance its generalization capabilities, data augmentation was applied using `ImageDataGenerator` with the following parameters:
*   `rotation_range=15`: Images were randomly rotated by up to 15 degrees.
*   `width_shift_range=0.1`: Images were randomly shifted horizontally by up to 10% of their total width.
*   `height_shift_range=0.1`: Images were randomly shifted vertically by up to 10% of their total height.
*   `shear_range=0.1`: Images were randomly sheared by up to 10 degrees.
*   `zoom_range=0.1`: Images were randomly zoomed in by up to 10%.
*   `horizontal_flip=True`: Images were randomly flipped horizontally.
*   `fill_mode='nearest'`: Newly created pixels after transformations were filled with the nearest pixel value.

For better perfomance on the augmented models, since they were generally trained on a more complex dataset. The augmented models featured an increased architectural complexity compared to its non-augmented counterpart. It incorporated `Conv2D` layers with 64, 128, and 128 filters respectively, and a `Dense` layer with 128 neurons before the final output layer. The total number of trainable parameters for this more complex model was 486,794. Also Normalization of the dataset had a great effect on the models perfomance

### Performance
After training, the augmented model demonstrated an increase in perfomance on the validation accuracy. Crucially, performance on the test dataset show significant improvement in generalization, achieving a final validation/test accuracy of approximately 80.% and a final test loss of 0.624. The closer alignment between training and test accuracy, despite a lower training accuracy, indicates better generalization and reduced overfitting due to data augmentation and increased model capacity as can be seen in the line graph below

<img width="1148" height="474" alt="image" src="https://github.com/user-attachments/assets/bf6d79cc-eb8c-44d5-a1f7-74304a873c5c" />


## Comparative Analysis

The table below summarizes the key differences and performance metrics between the two models:(specifically metrics on the last test)

| Feature                  | Non-Augmented Model                                      | Augmented Model                                                                                                                                                                                                                                                                                                  |
| :----------------------- | :------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Architecture Complexity** | Less complex (Conv2D filters: 64, 64, 64; Dense: 64 neurons) | More complex (Conv2D filters: 64, 128, 128; Dense: 128 neurons)                                                                                                                                                                                                                                                     |
| **Trainable Parameters** | 141,998                                                  | 486,794                                                                                                                                                                                                                                                                                                          |
| **Data Preprocessing**   | Normalization only                                       | Normalization + `ImageDataGenerator` (rotation, shifts, shear, zoom, flip)                                                                                                                                                                                                                                         |
| **Epochs**               | 50                                                       | 75                                                                                                                                                                                                                                                                                                               |
| **Training Accuracy**    | ~95.40%                                                  | ~83.55%                                                                                                                                                                                                                                                                                                          |
| **Test Accuracy**        | ~68.31%                                                  | ~80.25%                                                                                                                                                                                                                                                                                                          |
| **Test Loss**            | 2.193                                                    | 0.624                                                                                                                                                                                                                                                                                                            |
| **Generalization**       | Poor (significant overfitting)                           | Improved (reduced overfitting, better performance on unseen data)                                                                                                                                                                                                                                                |

### Implications
This comparison clearly demonstrates the profound impact of data augmentation on model generalization. While the non-augmented model achieved very high training accuracy, it failed to perform well on new, unseen data, a classic symptom of overfitting. The augmented model, despite a lower training accuracy, exhibited a significantly higher test accuracy and lower test loss, indicating its ability to learn more robust and generalizable features from the varied training data.

The increased architectural complexity in the augmented model was also a contributing factor. With a more diverse training set provided by augmentation, the larger model had the capacity to learn a richer representation of the data without succumbing to overfitting. This experiment underscores the importance of employing data augmentation techniques, especially when dealing with limited datasets, to build deep learning models that generalize effectively to real-world scenarios.

# CREDITS
This project served as a deep dive into the practical applications of Neural Networks. By building this, I’ve significantly strengthened my Machine Learning toolkit. I’m grateful to freeCodeCamp for the comprehensive curriculum that built my foundational knowledge in this space

