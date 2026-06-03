## Project Overview 
This project implements a Hidden Markov Model (HMM) using tensorflow-probability to predict temperature patterns over a 7-day period. Unlike standard models, an HMM excels at modeling systems where the "state" (the weather) is hidden, but can be estimated through observable data (temperature readings).

## HOW THE WEATHER MODEL WORKS
How the Model WorksThe model relies on three key probability distributions to estimate future weather:

*1. Initial Distribution*
   
This defines the starting point of our prediction.,

- Cold State: 80% probability.
- Sunny State: 20% probability.

*2. Transition Distribution*

This represents the likelihood of the weather changing from one day to the next.

- If today is Cold: There is a 70% chance it stays cold and a 30% chance it turns sunny.
- If today is Sunny: There is an 80% chance it stays sunny and a 20% chance it turns cold.

*3.Observation Distribution*

Since we cannot "see" the state directly, we observe temperatures.

- Cold Day: Modeled with a mean ( μ ) of 0°C and a standard deviation ( σ ) of 5.
- Sunny Day: Modeled with a mean ( μ ) of 15°C and a standard deviation ( σ ) of 10.

## Built With

1. TensorFlow Probability: For probabilistic modeling and HMM implementation.
2. Google Colab: Cloud-based execution environment.
3. AI Collaborators: Developed with assistance from Gemini and DeepSeek for logic refinement.


