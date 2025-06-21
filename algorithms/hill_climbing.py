import random
from models.nonogram import random_grid, generate_neighbours


def hill_climbing(nonogram, max_iterations, stochastic=False):
    current = random_grid(nonogram.R, nonogram.C)
    current_loss = nonogram.loss(current)

    for i in range(max_iterations):
        neighbours = generate_neighbours(current)
        if stochastic:
            neighbour = random.choice(neighbours)
            neighbour_loss = nonogram.loss(neighbour)
            if neighbour_loss < current_loss:
                current = neighbour
                current_loss = neighbour_loss
        else:
            best_neighbour = current
            best_loss = current_loss
            for n in neighbours:
                loss_val = nonogram.loss(n)
                if loss_val < best_loss:
                    best_neighbour = n
                    best_loss = loss_val
            if best_loss < current_loss:
                current = best_neighbour
                current_loss = best_loss
            else:
                break
    return current, current_loss
