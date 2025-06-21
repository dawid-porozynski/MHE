# Nonogram problem Solver - Metaheuristics

An academic project implementing optimization algorithms to solve nonogram puzzles. The system evaluates solution quality by comparing generated grids against perfect solutions using a custom loss function.

## Key Features
- Comparative analysis of metaheuristics
- Loss counter
- Grid visualization
- Multiple algorithm implementations

## Algorithms Implemented
|---------------------------------------------------------------|
| Algorithm            | Key Characteristics                    |
|----------------------|----------------------------------------|
| Brute-force          | Complete search algorithm              |
| Hill Climbing        | Both classic and stochastic verrsion   |
| Tabu Search          | With aspiration criteria               |
| Genetic Algorithm    | Customizable crossover/mutation        |
|---------------------------------------------------------------|

## Requirements
- Python 3.8+
- d

## Basic Command
bash
python main.py -a [algorithm] -f input.txt
