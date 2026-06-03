# RPS: Beat Them At Their Own Game
## Project Description 
In this project, the objective was to develop a Rock, Paper, Scissors program capable of competing against multiple predefined algorithms. To successfully complete the challenge, the program needed to achieve a win rate of at least 60% against each of four different opponent algorithms.

**Project Details** : https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

---
## My solution

This project is built around an idea that the best way to win in Rock,Paper,Scissors is to understand how the opposing algorithm makes decisions on what moves to play and then use that information to predict and counter its moves.
Rather than relying on a single fixed strategy, the program collects data during gameplay, identifies the opponent's patterns, and selects the most effective counter-strategy. Both my move history and the opponent's move history are treated as valuable sources of information for making predictions.

---

## Opponent Algorithms

The project is designed to compete against four predefined algorithms:

- **Quincy** – Follows a repeating five-move pattern: `R, R, P, P, S`
- **Kris** – Plays the move that beats your previous move
- **Mrugesh** – Tracks your most frequent move from the last ten rounds and counters it
- **Abbey:** Keeps track of moves in pairs and selects the counter to the most frequent move

---

## Project Structure

The solution consists of two main components:

### 1. Counter Strategies

These functions are designed to exploit the behavior of each opponent.

#### `beat_mrugesh`

Tracks my move history to determine which move Mrugesh is most likely to target, predicts the response, and plays the appropriate counter.

#### `beat_abbey`

Replicates Abbey's prediction method by monitoring move pairs and identifying common patterns. This allows the algorithm to anticipate Abbey's next move and respond effectively.

#### `beat_quincy`

Uses Quincy's known repeating sequence to predict its next move and select the correct counter.

#### `beat_kris`

Predicts the move Kris will play based on my previous move and then counters that prediction.

---

### 2. Opponent Identification

Before a counter-strategy can be used, the program must determine which algorithm it is facing.

During the first 15 rounds, moves are selected randomly while the opponent's history is recorded. The collected data is then analyzed to identify characteristic patterns.

#### Detection Functions

- **`find_abbey`** distinguishes between Abbey and Kris patterns as they are similar in the early rounds
- **`find_quincy`** checks for a repeating sequence in the opponent's move history.
- **`find_mrugesh`** looks at the early rounds of Mrugesh which follow a distinct pattern from the other algorithms.
---

## Main Function: `player()`

The `player()` function is the fully compossed function that coordinates the entire process.

### Rounds 1–15

- Plays random moves.
- Collects information about the opponent's behavior.
- Records data that may be useful for pattern analysis.

### Round 16

- Analyzes the collected history.
- Identifies the opponent algorithm.
- Selects the corresponding counter-strategy.

### Rounds 16–1000

- Continuously applies the selected counter-strategy.
- Adapts decisions based on the identified opponent.

### New Match Reset

- Clears stored data when a match ends.
- Prevents information from one opponent from affecting future games.

---

## Conclusion


**PROS**

The algorithm perfoms exceptionally well with the lowest win rate being at 86%  and highest going as far 99% win rate and the missing 1% can be attributed to the first 15 rounds where no stratergy is applied

**CONS**

- The algorithm is only limited to this 4 bots, which is enough to complete the fcc challenge, but when the algorithm is faced with a new opponent it crambles terribly.
- Dense code the idea of designing specific functions to beat specific bots increases linearly as the number of bots increase, making it inefficient for challenges that have many bots.

# Way forward 

Due to the weight of the cons, my way forward would be to design a new algorithm that despite the bot it is faced with, it can be able to adjust its stratergy effectively. This can be achieved by strategies such as Markov Chains and N- Grams

  
