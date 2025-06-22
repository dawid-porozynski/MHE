from collections import deque
# Kolejka dwukierunkowa używana do implementacji listy tabu
from models.nonogram import random_grid, generate_neighbours


def tabu_search(nonogram, max_iterations, tabu_size=100):
    current = random_grid(nonogram.R, nonogram.C)
    best = current
    best_loss = nonogram.loss(current)
    # Kolejka o stalym rozmiarze, max = taby_size
    tabu_list = deque([current], maxlen=tabu_size)

    for i in range(max_iterations):
        neighbours = [n for n in generate_neighbours(current) if n not in tabu_list]
        if not neighbours:
            break

        current = min(neighbours, key=lambda x: nonogram.loss(x))
        current_loss = nonogram.loss(current)
        tabu_list.append(current)

        if current_loss < best_loss:
            best = current
            best_loss = current_loss

    return best, best_loss
