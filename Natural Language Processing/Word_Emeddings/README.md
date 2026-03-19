# Word Embedding Analysis: High-Dimensional Model
## V1 Model Sematic Contextualization


**Scatter Plot**

<img width="591" height="397" alt="image" src="https://github.com/user-attachments/assets/cf06e632-b782-4f99-a50c-536008bed5b7" />

## Key Observations
### 1. The Gender Dimension
The model has successfully developed a primary axis for **gender representation**. 
* **Upper Cluster ($y > 0.5$):** Groups female-coded terms such as *woman*, *daughter*, *queen*, and *princess*.
* **Lower Cluster ($y < -0.5$):** Groups male-coded terms such as *man*, *prince*, *king*, and *boy*.
* **Observation:** The vertical $y$-axis effectively serves as a "gender dimension," separating masculine and feminine concepts into distinct spatial regions.

### 2. Descriptive Adjective Association
The model demonstrates an understanding of descriptive context by clustering adjectives near the nouns they most frequently modify in the training data:
* **"Beautiful"** is positioned almost identically to **"queen,"** suggesting these words appeared in highly similar linguistic contexts.
* **"Strong"** is located in close proximity to **"king"** and **"son,"** reflecting a learned association between those terms.

### 3. Familial and Generational Roles
There is a clear diagonal relationship between familial pairs. **"Daughter"** and **"woman"** occupy the top-left/center, while **"son"** and **"boy"** occupy the bottom-right. This indicates the model is distinguishing between adult roles and youth/offspring roles across both axes simultaneously.

### 4. Status and Linguistic Outliers
While most "royal" terms (*queen*, *king*, *princess*) are clustered toward the center and right, **"prince"** and **"man"** are notable outliers on the far left. 
* **Observation:** This suggests that in the specific training corpus used, the word "prince" may have appeared in different syntactic structures or less frequently than "princess" or "king," leading the model to distance it from the other royal titles.

## V2 Model Cotextualization
> **Experiment:** Increasing Hidden Layer Dimensions + t-SNE Visualization

After transitioning from a simple 2D bottleneck to a **higher-dimensional hidden layer**, the model has successfully mapped the vocabulary into sophisticated semantic neighborhoods. Here are the key observations from the V2 model:

<img width="684" height="560" alt="image" src="https://github.com/user-attachments/assets/79a1e60f-20c5-4276-88af-4d6944748bf1" />



### 1. The "Royalty & Family" Cluster
In the center-right of the visualization, there is a clear **High-Status Cluster**:
*   **Words:** `king`, `queen`, `daughter`.
*   **Observation:** The model has prioritized **Status/Role** over **Gender**. 
*   **Inference:** In the training data, these words likely shared the same "royal" neighbors (e.g., *palace*, *throne*, *rule*), pulling them into the same mathematical "zip code."

### 2. The "Masculine Role" Gradient
On the far-left, the model has established a very logical **Gender-specific String**:
*   **Sequence:** `prince` $\rightarrow$ `man` $\rightarrow$ `boy` $\rightarrow$ `son`.
*   **Observation:** The model has separated "informal" masculine roles from the "formal" royalty cluster. 
*   **Inference:** This suggests the training data used these words in distinct narrative contexts (e.g., "The boy plays" vs. "The king rules").

### 3. Part-of-Speech Specialization (Outliers)
*   **`beautiful`**: Positioned at the extreme bottom-right. This is a sign of **Semantic Separation**. The model recognizes that "beautiful" (an adjective) functions differently in a sentence than the nouns (people).
*   **`strong` & `princess`**: These two are tightly clustered together. In this specific dataset, the model has learned a strong **Association Rule**, likely because they appeared together in many bigrams.

### 4. The Central Semantic "Hub"
*   **`future`**: Positioned as a bridge between the masculine cluster and the royalty cluster. 
*   **Observation:** Abstract words often sit in the "center" of embedding spaces because they are **poly-contextual**—they can legitimately appear next to almost any other noun in the dataset.

---

###  Conclusion
By increasing the **hidden layer dimensions**, the model has moved from simple 2D rules to a **multi-faceted semantic map**. The weights now categorize words by **Role**, **Status**, and **Contextual Association** rather than just spatial coordinates.


## V3 Model Analytsis

This version of the model was developed utilizing **trigrams** (sequences of three words) and a significantly larger hidden layer of **100 neurons**. While this architectural shift increased the model's capacity to capture complex linguistic nuances, it led to rapid **overfitting** within the early epochs of training.

### 1. High-Dimensional Sparsity
By increasing the hidden layer to **100 dimensions**, the model's parameter count grew substantially. 
* **The Challenge:** In a 100D vector space, data points become extremely "sparse." 
* **The Result:** When the number of trainable parameters is large relative to the number of unique trigrams in the dataset, the model can "assign" specific neurons to memorize individual trigram sequences. This allows the model to achieve near-perfect training accuracy without ever learning the underlying semantic relationships between the words.

### 2. Trigram Specificity vs. Semantic Generalization
Trigrams provide a much narrower and more specific context ($W_1, W_2 \rightarrow W_3$) compared to bigrams ($W_1 \rightarrow W_2$). 
* Because specific three-word sequences often appear only once or twice in a smaller dataset, the 100D model finds a mathematical "shortcut" to map these specific inputs directly to their targets.
* Consequently, the model fails to develop the generalized "clusters" (such as the Gender or Status axes) observed in the lower-dimensional bigram model, as it is preoccupied with memorizing exact phrasing.*



### Conclusion
While the **100D Trigram model** possesses the theoretical capacity to understand complex sentence structures, it requires a significantly larger and more diverse dataset to prevent "memorization" of the training samples. For smaller-scale experiments, the **lower-dimensional bigram model** remains more robust, as the "bottleneck" effect forces the model to compress information and discover broader, more useful semantic categories.

# Credits 
Coding Lane - By learn with Jay, for the detailed explaanations and demonstrations on word embeddings



