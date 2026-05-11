# SMS Spam Classification: Model Performance Report

This project explores how different Recurrent Neural Network (RNN) architectures perform in classifying SMS messages as either **spam** or **ham** (legitimate messages).


---

## Model Architectures & Performance Overview

| Model | Architecture Type | Overall Observation | 
| :--- | :--- | :--- | 
| **Simple RNN** | Unidirectional | fast and perfomed significantly better as baseline model |  
| **Bidirectional RNN** | Bidirectional | Better contextual understanding 
| **Bidirectional LSTM** | Bidirectional | Handles long-term dependencies effectively |
| **Stacked LSTM** | Multi-layered | Deeper sequence learning |

---

## 1. Simple RNN and LSTM Models

The Simple single layer models served as the starting point for the project.  
They processes text sequentially from left to right while maintaining a running memory of previous words.

This implementation helped establish a performance baseline before moving to more advanced architectures.

**Models Evaluation**

Across 5 and 10 epochs for the LSTM and RNN respectively this is how the networks perfomed on different data 

|Data| Simple RNN | Simple LSTM| 
| :--- | :--- | :--- |
*Training data* | 99.88% | 99.82%
*Validation data* | 97.85% | 98.21%
*Testing data* | 98.20%  |98.42%

One of its main limitations became clear during testing: the model struggled to retain important information over longer message sequences.Due to vanishing gradients, which occur when differentiting activations which have very low gradients ending up in clumping the gradient flow, over long sequences of timesteps. 
> **[ Simple RNN Training/Validation Accuracy and Loss Curves]**

<img width="680" height="682" alt="image" src="https://github.com/user-attachments/assets/c9852875-bcb6-47dd-b7d5-0e4e4dcc2100" />

---

## 2. Bidirectional RNN Model

The Bidirectional RNN improved performance by processing text in two directions simultaneously forward and backward.

Instead of relying only on earlier words in a sentence, the model could also use future context when making predictions. This proved especially useful in spam detection, where certain keywords appearing later in a message can completely change its meaning.

Compared to the Simple RNN, this model showed a stronger understanding of sentence structure and context, leading to more reliable classifications.

**Models Evaluation**

Across 5 epochs for the BidirectinalRNN this is how the network perfomed on different data 

|Data|Perfomance |  
| :--- | :--- | 
*Training data* | 100% | 
*Validation data* | 98.44% | 
*Testing data* | 98.64%  |

> **[BidirectionalRNN Training/Validation Accuracy and Loss Curves]**


<img width="680" height="682" alt="image" src="https://github.com/user-attachments/assets/5f0f0e4d-7cb1-4e9f-a151-fde5eebd830f" /> 


---

## 3. Bidirectional LSTM Model

The Bidirectional LSTM (BiLSTM) produced the strongest overall performance during testing.

Unlike standard RNNs, LSTMs are designed to manage long-term dependencies more effectively using internal gating mechanisms. These gates help the model decide what information to retain, what to ignore, and what should influence future predictions.

Combining this memory capability with bidirectional processing allowed the model to capture both immediate and long-range contextual patterns in spam messages.

As a result, the BiLSTM handled nuanced message structures more consistently and achieved the most stable performance across evaluations.

**Models Evaluation**

Across 5 epochs for the BidirectinalLSTM this is how the network perfomed on different data 

|Data|Perfomance |  
| :--- | :--- | 
*Training data* | 100% | 
*Validation data* | 97.73% | 
*Testing data* | 98.71%  |

> **[BidirectionalLSTM Training/Validation Accuracy and Loss Curves]**

<img width="680" height="682" alt="image" src="https://github.com/user-attachments/assets/8356b982-acca-4765-979a-0a8b306adec8" />


---

## 4. Stacked LSTM Model

The Stacked LSTM experimented with a deeper architecture by layering multiple LSTM network on top of one another.

The intention behind this setup was to allow the model to learn increasingly abstract sequence features at different levels of depth. While the architecture had strong theoretical potential, the results were less stable during testing.

Performance dropped in the later evaluation stages, suggesting that the model had not fully converged during training. Deep recurrent networks generally require more training time, careful tuning, and larger computational resources to perform effectively.


**Models Evaluation**

Across 8 epochs for the StackedLSTM this is how the network perfomed on different data  

|Data|Perfomance |  
| :--- | :--- | 
*Training data* | 98.81% | 
*Validation data* | 97.73% | 
*Testing data* | 98.49%  |



> **[Stacked LSTM Training/Validation Accuracy and Loss Curves]**

<img width="680" height="682" alt="image" src="https://github.com/user-attachments/assets/a2a38a37-3db8-4989-a79e-030f9531be43" />


---

## General Testing Procedure

The following process was used across all experiments:

1. **Preprocessing**  
   SMS data was loaded from `.tsv` files and normalized by converting text to lowercase.

2. **Tokenization**  
   Words were transformed into numerical representations using a Keras `Tokenizer`.

3. **Padding**  
   Since messages vary in length, sequences were padded to a fixed size to maintain consistent model input dimensions.

4. **Classification**  
   The processed sequences were passed through recurrent layers and finally into a Dense layer with a **Sigmoid** activation for binary spam prediction.

---

## Final Observation

A clear trend emerged throughout the experiments: models that could better preserve contextual information consistently produced stronger results.

The Simple RNN provided a useful foundation, but its limitations with long-range dependencies became evident as testing progressed. Introducing bidirectional processing significantly improved contextual understanding, while the addition of LSTM memory mechanisms further strengthened performance stability and classification accuracy.

The Bidirectional LSTM ultimately achieved the best balance between learning capacity, reliability, and generalization. Meanwhile, the Stacked LSTM demonstrated that deeper architectures do not automatically guarantee better performance, especially when training time and tuning are limited.

Overall, the project evolved from testing basic sequence learning to gaining a deeper understanding of how different recurrent architectures capture language patterns in real-world text classification tasks.

---

*Developed by keden49*
