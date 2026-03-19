# Word Embedding Analysis: High-Dimensional Model
> **Experiment:** Increasing Hidden Layer Dimensions + t-SNE Visualization

After transitioning from a simple 2D bottleneck to a **higher-dimensional hidden layer**, the model has successfully mapped the vocabulary into sophisticated semantic neighborhoods. Here are the key observations from the latest plot:

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
