
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/keden49/Machine-learning-with-python-freecode-camp/blob/main/Frozen%20Lake%20Environment/Frozen_Lake_Environment(Visualization).ipynb)

# Frozen Lake Environment 

[Frozen Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) involves crossing a frozen lake from start to goal without falling into any holes by walking over the frozen lake. The player may not always move in the intended direction due to the slippery nature of the frozen lake.

## Description

The game starts with the player at location [0,0] of the frozen lake grid world with the goal located at far extent of the world e.g. [3,3] for the 4x4 environment.

Holes in the ice are distributed in set locations when using a pre-determined map or in random locations. The player makes moves until they reach the goal and avoids falling into the gaping holes.
The lake is slippery (unless disabled) so the player may move perpendicular to the intended direction.

## Agent Simulation Visualization

**Starting Position**
<img width="374" height="365" alt="image" src="https://github.com/user-attachments/assets/d4c906f0-4f8c-4482-a435-1d6940efbdc1" />



**Goal**


<img width="375" height="382" alt="image" src="https://github.com/user-attachments/assets/c50e5e19-4ae4-40dd-afc3-b2d6432d5c92" />


---

## How the Environment Works

The agent can move in four directions:
- Left (0)
- Down (1)
- Right (2)
- Up (3)

In this project:
- `is_slippery = False`
- This means movement is **deterministic** (no randomness in direction)

---

## Reinforcement Learning 

### Learning Strategy: Q-Learning
The agent employs **Q-learning**, an off-policy reinforcement learning algorithm used to learn the value of actions in specific states.


**Bellman Equation:** The agent updates its knowledge after every step using the following formula

```
Q_TABLE[state, action] = Q_TABLE[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q_TABLE[next_state, :]) - Q_TABLE[state, action])
```

### Hyperparameters
The model achieved success using the following configuration

| Hyperparameter | Value | Description |
| :--- | :--- | :--- |
| **Learning Rate ($\alpha$)** | **0.81** | Controls how much new information overrides old estimates[cite: 2, 3]. |
| **Discount Factor ($\gamma$)** | **0.96** | Determines the importance of long-term future rewards[cite: 2, 3]. |
| **Episodes** | **5,000** | The total number of training iterations[cite: 2]. |
| **Epsilon ($\epsilon$)** | **0.9** | Starting probability for random exploration[cite: 1, 2]. |



---

## Agents Training Performance

The agent was trained over 5000 episodes and 100 steps per episode. In this way it was able to achive an average success rate of about **0.89 (89%)**

**Visualization**

<img width="550" height="435" alt="image" src="https://github.com/user-attachments/assets/1ce55dfb-a62f-40aa-b4e8-7396e9112ae4" />


---

## Running the Simulation

- Click the "Open in Colab" button to run
- Navigate the colab Notebook and click Runtime then run all

# Credits 

- freeCodeCamp: This project was developed as part of the freeCodeCamp "Machine Learning with Python" curriculum, which provided the foundational knowledge for building and training reinforcement learning agents.  
- OpenAI Gymnasium: The Frozen Lake environment is provided by OpenAI Gymnasium (formerly OpenAI Gym), an open-source Python toolkit used for developing and comparing reinforcement learning algorithms.  


