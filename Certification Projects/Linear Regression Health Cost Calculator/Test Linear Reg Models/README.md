# Project Overview

This project explores the behavior and limitations of different regression approaches used in predicting health insurance costs. The notebooks compare how simple linear models behave against deeper non-linear neural networks when trained on the same health cost dataset.

## Experiments

### Test 1 - Baseline Linear Regression
A simple linear regression implementation, built from Keras with a single unit in the dense layer, used to establish a baseline for prediction performance and model behavior.

### Test 2 - Traditional sklearn Linear Models
Experiments using older linear regression implementations from `sklearn` to compare their behavior against a Keras single-neuron model and verify whether a single neuron can effectively behave as a linear regression model.

### Test 3 - Adressing Exploding Gradients 
Additional tests focused on evaluating prediction consistency, error patterns. The first Test failed to learn as the training labels/expenses were unormalized causing the graidents to be very large and preventing the network from Learning 

### Test 4 - Deep Non-Linear Network
A deeper neural network architecture designed to capture more complex and non-linear relationships within the health cost dataset.

## Graph Analysis: Comparison Between Linear and Deep Neural Network Models
<table>
  <tr>
    <td align="center">
      <strong>Simple Linear Regression Actual Labels vs Predictions</strong><br>
      <img src="https://github.com/user-attachments/assets/02329a36-fe2e-4d5b-a5c1-bd2a8e587b4c" width="400"/>
    </td>
    <td align="center">
      <strong>Deep Neural Network Actual Labels vs Predictions</strong><br>
      <img src="https://github.com/user-attachments/assets/fad2a989-8e27-4631-91ea-8b546beb138f" width="400"/>
    </td>
  </tr>
</table>



#### Description
The graphs compare the prediction behavior of two different models trained on the same insurance cost dataset. The first graph represents a simple linear regression model, while the second represents a deeper neural network that incorporates non-linear activation functions in its hidden layers.

#### Trend Analysis

- **Linear Regression Model Performance:**  
  In the first graph, the predictions remain significantly distant from the actual target values. Most predicted values collapse close to zero, despite the real insurance costs varying widely across the dataset. This pattern shows that the model failed to learn the underlying relationship between the input features and the target variable.

  The trend suggests severe underfitting. Because the model relied only on a single linear relationship, it lacked the flexibility required to represent the complexity of medical insurance pricing. Important interactions between variables such as smoking status, age, and BMI were not captured effectively.

- **Deep Neural Network Performance:**  
  In the second graph, the predicted values follow the actual targets much more closely. Instead of collapsing toward a single region, the predictions spread across the range of true values and begin reflecting the overall structure of the dataset.

  This improvement indicates that the deeper architecture was able to extract more meaningful patterns from the data. The use of non-linear activation functions in the earlier layers allowed the network to model relationships that a purely linear system could not represent.


# Observations

Through these experiments, I observed that linear models perform reasonably well when relationships in the dataset are relatively simple, but they struggle to capture more complex patterns and feature interactions.

The Keras single-neuron model behaved similarly to traditional linear regression models, reinforcing the idea that a single neuron with no hidden layers essentially functions as a linear model.

The deeper neural network demonstrated better flexibility and learning capacity, allowing it to model non-linear relationships between features more effectively and improve prediction performance compared to simpler regression approaches.
