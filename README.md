# Nonogram problem Solver - Metaheuristics

Projekt akademicki implementujący algorytmy optymalizacyjne do rozwiązywania nonogramu. System ocenia jakość rozwiązań poprzez porównanie generowanych siatek z idealnymi rozwiązaniami przy użyciu własnej funkcji loss.

# Główne Funkcje
- Analiza porównawcza metaheurystyk
-Licznik strat (loss counter)
-Wizualizacja siatki
-Implementacja wielu algorytmów

## Zaimplementowane algorytmy
| Algorithm            | 
|----------------------|
| Brute-force          |
| Hill Climbing        |
| Tabu Search          |
| Genetic Algorithm    |

## Wymagania
- Python 3.8+

## Podstawowa komenda
bash
python3 main.py -a [algorithm] -f input.txt

python3 main.py -a genetic -f input2.txt \
    --pop_size 200 \
    --max_gen 500 \
    --crossover two_point \
    --mutation bit_flip \
    --mutation_rate 0.05

---------------------------------------------------------------------------------------------------------------------    

# Nonogram problem Solver - Metaheuristics

An academic project implementing optimization algorithms to solve nonogram puzzles. The system evaluates solution quality by comparing generated grids against perfect solutions using a custom loss function.

## Key Features
- Comparative analysis of metaheuristics
- Loss counter
- Grid visualization
- Multiple algorithm implementations

## Algorithms Implemented
| Algorithm            | 
|----------------------|
| Brute-force          |
| Hill Climbing        |
| Tabu Search          |
| Genetic Algorithm    |

## Requirements
- Python 3.8+
  

## Basic Command
bash
python3 main.py -a [algorithm] -f input.txt

python3 main.py -a genetic -f input2.txt \
    --pop_size 200 \
    --max_gen 500 \
    --crossover two_point \
    --mutation bit_flip \
    --mutation_rate 0.05
