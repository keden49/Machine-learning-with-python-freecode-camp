# Overview 

This repository contains all deployment notebooks and an additional diabetes KNN project to get a better understanding of K - Nearest Neighbors.

## Key Highlights

### Categorical Data Types

```python
sparse_df['User_ID'] = sparse_df['User_ID'].astype('category')
sparse_df['ISBN'] = sparse_df['ISBN'].astype('category')
```

**What Happens Under The Hood**

* **The Lookup Translation**: Instead of showing the raw integer codes, pandas takes each code (e.g., `0`), looks it up in the master dictionary, and grabs the original text (e.g., `'111-ISBN'`).
* **On-the-Fly Formatting**: Pandas builds a temporary string grid using those translated values, projects it to your screen, and deletes it from RAM instantly.
* **Saves Memory**: Codes are saved with ```int32``` hence saving memory compared to storing dataset using raw string objects which take much more

---
**Example**
###  Memory Analysis: Standard Strings vs. Categorical Types

Let's look at a realistic dataset of **1,000,000 rows** containing only **10,000 unique values** repeating across those rows.

#### 1. Standard String Column (No Categories)
Every single row stores a heavy string object explicitly in memory.
*   **Formula:** $1,000,000 \text{ rows} \times 60 \text{ bytes per string}$
*   **Total Cost:** $\mathbf{60,000,000 \text{ bytes }(\approx 60 \text{ MB})}$

#### 2. Categorical Column (Optimized)
The memory footprint is split into two lightweight parts:
*   **The Master Dictionary:** Stores the 10,000 unique strings exactly *once*.
    *   $10,000 \text{ strings} \times 60 \text{ bytes} = \mathbf{600,000 \text{ bytes }(\approx 0.6 \text{ MB})}$
*   **The Codes Array:** Stores 1,000,000 rows of lightweight integers (`int16` because 10,000 unique items fit perfectly under the 32,767 threshold).
    *   $1,000,000 \text{ rows} \times 2 \text{ bytes per code} = \mathbf{2,000,000 \text{ bytes }(\approx 2.0 \text{ MB})}$

####  Total Categorical Cost:
$$\text{Total Cost} = 0.6 \text{ MB (Dictionary)} + 2.0 \text{ MB (Codes)} = \mathbf{2.6 \text{ MB}}$$


**Verdict:** By switching to a categorical type, memory usage drops from **60 MB to 2.6 MB** (a savings of roughly 95.6%).

---

### CSR MATRIX(scipy.sklearn)

A CSR matrix (Compressed Sparse Row) is a specialized data structure used to store matrices that consist mostly of zeros (known as sparse matrices). It drastically reduces memory consumption and speeds up calculations by omitting the zeros and only storing the non-zero values

A CSR matrix compresses an \(m \times n\) matrix into three separate, 1D NumPy arrays:

- data: An array containing all the non-zero values from the original matrix, read row by row.
- indices: An array containing the column index for each corresponding value in the data array.
- indptr: An index pointer array that indicates where each row starts and ends in the data and indices arrays.


**Benefits**

*   **Memory Efficiency**: It doesn't store the `0`s, saving space.
*   **Computational Efficiency**: Distance calculations (like dot products) can be optimized to only consider the shared, non-zero ratings between two books, making them much faster than iterating over all users, many of whom haven't rated both books. The `0`s (non-ratings) effectively don't contribute to the similarity calculation in many common metrics, so explicitly storing and processing them would be wasteful.

----

### Distance Metrics 

**Euclidian Distance**

Euclidean distance is the straight-line distance between two points in space. It is the most common method for measuring how far apart objects or data points are and is derived directly from the Pythagorean theorem.

#### Reasons why This approach is undesirable for this project 

*   **Distance concentration (curse of dimensionality)**
    *   As dimensionality increases, pairwise Euclidean distances between random points tend to concentrate tightly around their mean. Relative differences shrink, so the ratio (max − min)/min → 0 in many common distributions.
    *   Practical consequence: nearest and farthest neighbors become nearly indistinguishable, undermining ranking, classification, and retrieval.
*   **Growing influence of irrelevant/noisy features**
    *   Each added dimension adds noise and variance; if many dimensions are irrelevant, their contributions drown signal dimensions in the squared-sum calculation of Euclidean distance.
    *   Practical consequence: distances reflect aggregate noise rather than meaningful similarity; feature scaling or selection is often required.
*   **Increasing sparsity and empty space**
    *   Volume grows exponentially with dimensionality; data points occupy an ever-smaller fraction of the space, so local neighborhoods become sparse and statistical estimates (densities, means) become unstable.
    *   Practical consequence: methods that rely on local distances (k-NN, density estimation) lose reliability and require many more samples to achieve the same coverage.
*   **Metric distortions and loss of interpretability**
    *   High-dimensional Euclidean distance mixes many orthogonal contributions; a single large coordinate can dominate distance, making global distance hard to interpret as similarity.
    *   Practical consequence: small differences in a few features can be masked or exaggerated, reducing robustness.
*   **Computational and storage costs**
    *   Computing Euclidean distances scales linearly with dimensionality per comparison; with many points and high d this becomes expensive and memory-intensive.
    *   Practical consequence: distance computations dominate runtime in large-scale systems.


 **Cosine Similarity**

Cosine similarity measures the cosine of the angle between two non-zero vectors. In the context of our `csr_matrix`, each row represents a book, and the values in that row are the ratings given by different users. Therefore, each book is a vector in a high-dimensional space (where each dimension corresponds to a user).

**Formula**

$$\text{cosine similarity} (A, B) = \frac{A \cdot B}{||A|| \cdot ||B||}$$

Where:
*   $A \cdot B$ is the dot product of vectors A and B (sum of the products of corresponding components).
*   $||A||$ is the Euclidean norm (magnitude) of vector A, calculated as $\sqrt{\sum_{i=1}^{n} A_i^2}$.
*   $||B||$ is the Euclidean norm (magnitude) of vector B.

**The Core Concept

Orientation over Magnitude: It only evaluates the direction (angle) of the vectors. If two data points share the same orientation, they are highly similar even if one is much larger than the other.
- Score Range: Scores range from -1 to 1:
- 1: Vectors point in the exactly same direction (highly similar)
- 0: Vectors are orthogonal (no similarity)
- -1: Vectors point in opposite directions













