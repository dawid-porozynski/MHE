import random
from models.nonogram import Nonogram


def genetic_algorithm(nonogram, pop_size, max_generations, crossover_method, mutation_method, mutation_rate):
    def create_individual():
        return [random.randint(0, 1) for _ in range(nonogram.R * nonogram.C)]

    def individual_to_grid(individual):
        grid = []
        index = 0
        for r in range(nonogram.R):
            row = individual[index:index + nonogram.C]
            index += nonogram.C
            grid.append(row)
        return grid

    def fitness(individual):
        grid = individual_to_grid(individual)
        return nonogram.loss(grid)

    def selection(population, fitnesses):
        selected = []
        for _ in range(pop_size):
            indices = random.sample(range(pop_size), 2)
            idx1, idx2 = indices
            selected.append(population[idx1] if fitnesses[idx1] < fitnesses[idx2] else population[idx2])
        return selected

    def crossover(parent1, parent2, method):
        if method == 'one_point':
            point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
            return child1, child2
        elif method == 'two_point':
            points = sorted(random.sample(range(1, len(parent1)), 2))
            child1 = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:]
            child2 = parent2[:points[0]] + parent1[points[0]:points[1]] + parent2[points[1]:]
            return child1, child2

    def mutation(individual, method, rate):
        if method == 'bit_flip':
            for i in range(len(individual)):
                if random.random() < rate:
                    individual[i] = 1 - individual[i]
            return individual
        elif method == 'swap':
            if random.random() < rate:
                idx1, idx2 = random.sample(range(len(individual)), 2)
                individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
            return individual

    population = [create_individual() for _ in range(pop_size)]
    best_individual = None
    best_fitness = float('inf')

    for generation in range(max_generations):
        fitnesses = [fitness(ind) for ind in population]
        min_fit = min(fitnesses)
        if min_fit < best_fitness:
            best_idx = fitnesses.index(min_fit)
            best_individual = population[best_idx]
            best_fitness = min_fit
        if best_fitness == 0:
            break

        parents = selection(population, fitnesses)
        next_population = []
        for i in range(0, pop_size, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1] if i + 1 < pop_size else parents[0]
            child1, child2 = crossover(parent1, parent2, crossover_method)
            child1 = mutation(child1, mutation_method, mutation_rate)
            child2 = mutation(child2, mutation_method, mutation_rate)
            next_population.extend([child1, child2])
        population = next_population[:pop_size]

    grid = individual_to_grid(best_individual)
    return grid, best_fitness