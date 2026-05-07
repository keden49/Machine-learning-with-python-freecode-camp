# Project Research & Implementation Analysis

This section documents the different experiments carried out while building the ConvNet image recognition model.  
Each test explored a different architectural or optimization approach to better understand how the model learned from the dataset and how performance changed over time.

---

## Test Implementation 1: Building the Initial ConvNet Foundation

The first version of the model used two convolution layers followed by dense layers. The main goal here was to create a simple baseline model capable of learning basic image features before making classifications.

Instead of making the network overly complex from the start, this implementation focused on helping the model first recognize simple patterns such as edges and shapes, then gradually combine them into more meaningful visual features.

* **Result:** Achieved **62%** test accuracy and **68.20%** validation accuracy.

### Model Architecture

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :--- |
| **Conv2D** (5x5, 32 filters) | (None, 146, 146, 32) | 2,432 |
| **MaxPooling2D** | (None, 73, 73, 32) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 71, 71, 64) | 18,496 |
| **MaxPooling2D** | (None, 35, 35, 64) | 0 |
| **Flatten** | (None, 78400) | 0 |
| **Dense** (ReLU) | (None, 128) | 10,035,328 |
| **Dense** (Sigmoid) | (None, 1) | 129 |

---

### Test 1: Results Visualization

<img width="683" height="632" alt="image" src="https://github.com/user-attachments/assets/8c39bf56-91b2-48cc-bbce-b11af0003764" />

---

## Test Implementation 2: Exploring Optimizer and Filter Adjustments

The second experiment focused more on how the model learned rather than changing the entire structure itself. RMSProp replaced Adam as the optimizer, the dense layer size was increased, and the early convolution setup was adjusted to test how selective feature extraction would affect performance.

This phase was mainly exploratory. The intention was to observe whether a different optimization strategy could improve learning consistency and whether reducing early complexity would force the model to focus on stronger features instead of memorizing patterns too quickly.

* **Result:** Accuracy improved slightly to **64%** on test data and **65%** on validation data.

### Model Architecture

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :--- |
| **Conv2D** (3x3, 32 filters) | (None, 148, 148, 32) | 896 |
| **MaxPooling2D** | (None, 74, 74, 32) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 72, 72, 64) | 18,496 |
| **MaxPooling2D** | (None, 36, 36, 64) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 34, 34, 64) | 36,928 |
| **Flatten** | (None, 73984) | 0 |
| **Dense** (ReLU) | (None, 256) | 18,940,160 |
| **Dense** (Sigmoid) | (None, 1) | 257 |

---

### Test 2: Results Visualization

<img width="689" height="581" alt="image" src="https://github.com/user-attachments/assets/11b82c4e-61a4-4c7a-901e-7035c16a29d6" />

---

## Test Implementation 3: Improving Generalization with Dropout

After observing gaps between training and testing performance in earlier experiments, this implementation introduced a Dropout layer to reduce overfitting and improve the model’s ability to generalize on unseen data.

Rather than allowing the network to rely too heavily on specific neurons, Dropout encouraged the model to learn more distributed and flexible feature representations. This led to noticeably better performance during evaluation.

* **Result:** This became the strongest-performing implementation, reaching **70%** test accuracy.

---

### Test 3: Results Visualization

<img width="674" height="580" alt="image" src="https://github.com/user-attachments/assets/f51d166a-3e22-489e-94ed-742f951f904e" />

### Model Summary

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :--- |
| **Conv2D** (5x5, 32 filters) | (None, 146, 146, 32) | 2,432 |
| **MaxPooling2D** | (None, 73, 73, 32) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 71, 71, 64) | 18,496 |
| **MaxPooling2D** | (None, 35, 35, 64) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 33, 33, 64) | 36,928 |
| **Flatten** | (None, 69696) | 0 |
| **Dense** (ReLU) | (None, 128) | 8,921,216 |
| **Dropout** (0.2) | (None, 128) | 0 |
| **Dense** (Sigmoid) | (None, 1) | 129 |

---

## Test Implementation 4: Testing Momentum-Based Optimization

This phase focused on experimenting with Momentum as the optimizer while keeping most of the architecture relatively unchanged.

The goal was to see whether smoother weight updates and accumulated learning direction could help the model converge more effectively during training. Although training became more stable, the overall performance did not surpass earlier experiments.

* **Result:** The model achieved **60%** test accuracy and **66%** validation accuracy.

### Model Summary

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :--- |
| **Conv2D** (5x5, 32 filters) | (None, 146, 146, 32) | 2,432 |
| **MaxPooling2D** | (None, 73, 73, 32) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 71, 71, 64) | 18,496 |
| **MaxPooling2D** | (None, 35, 35, 64) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 33, 33, 64) | 36,928 |
| **Flatten** | (None, 69696) | 0 |
| **Dense** (ReLU) | (None, 128) | 8,921,216 |
| **Dense** (ReLU) | (None, 64) | 8,256 |
| **Dense** (Sigmoid) | (None, 1) | 65 |

---

### Test 4: Results Visualization

<img width="682" height="573" alt="image" src="https://github.com/user-attachments/assets/55759c6c-9eba-4c8f-b6a6-f5ca593a6843" />

---

## Test Implementation 5: Stabilization and Training Refinement

The final experiment introduced Batch Normalization, Padding, and He-Uniform initialization in an attempt to create a more stable and mathematically optimized training process.

This implementation aimed to preserve image details more effectively while also improving gradient flow during learning. Despite the more advanced setup, the model did not generalize as well as expected on this dataset.

* **Result:** Final test accuracy reached **56%**.

### Model Summary

| Layer (type) | Output Shape | Param # |
| :--- | :--- | :--- |
| **Conv2D** (5x5, 32 filters) | (None, 146, 146, 32) | 2,432 |
| **BatchNormalization** | (None, 146, 146, 32) | 128 |
| **MaxPooling2D** | (None, 73, 73, 32) | 0 |
| **Dropout** (0.25) | (None, 73, 73, 32) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 71, 71, 64) | 18,496 |
| **BatchNormalization** | (None, 71, 71, 64) | 256 |
| **MaxPooling2D** | (None, 35, 35, 64) | 0 |
| **Dropout** (0.25) | (None, 35, 35, 64) | 0 |
| **Conv2D** (3x3, 64 filters) | (None, 33, 33, 64) | 36,928 |
| **BatchNormalization** | (None, 33, 33, 64) | 256 |
| **Flatten** | (None, 69696) | 0 |
| **Dropout** (0.5) | (None, 69696) | 0 |
| **Dense** (ReLU) | (None, 128) | 8,921,216 |
| **Dense** (Sigmoid) | (None, 1) | 129 |

---

### Test 5: Performance Results Visualization

<img width="687" height="630" alt="image" src="https://github.com/user-attachments/assets/c049d461-a987-4b8d-8ac8-a81e46f7b080" />

---

## Conclusion

Across the different experiments, a clear pattern emerged: increasing architectural complexity did not always lead to better performance.

The earlier implementations established a strong foundation, but they also revealed issues with overfitting and inconsistent generalization. As testing progressed, the experiments became less about simply adding layers and more about understanding how the model actually learned from the data.

The most important improvement came in Test 3 with the introduction of Dropout. While some later implementations used more advanced techniques such as Batch Normalization and specialized initialization methods, the simpler Dropout-based architecture ultimately performed better on unseen images. This suggested that, for this dataset, improving generalization was more valuable than increasing structural complexity.

Overall, the project demonstrated a gradual shift from experimentation to informed architectural decision-making. Each implementation contributed insight into how optimization methods, regularization, and network depth affected performance, leading to a more practical understanding of ConvNet behavior beyond just achieving higher accuracy scores.

---

*Developed by keden49*
