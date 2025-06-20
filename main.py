import argparse
import sys
from models.nonogram import Nonogram
from algorithms.hill_climbing import hill_climbing
from algorithms.tabu import tabu_search
from algorithms.genetic_algorithm import genetic_algorithm
from algorithms.full_search import full_search


def print_grid(grid):
    for row in grid:
        print(''.join('#' if cell == 1 else '.' for cell in row))


def main():
    parser = argparse.ArgumentParser(description='Nonogram Solver')
    parser.add_argument('-a', '--algorithm', required=True,
                        choices=['full', 'hill', 'hill_stoch', 'tabu', 'genetic'])
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--max_iter', type=int, default=10000)
    parser.add_argument('--tabu_size', type=int, default=100)
    parser.add_argument('--pop_size', type=int, default=100)
    parser.add_argument('--max_gen', type=int, default=100)
    parser.add_argument('--crossover', choices=['one_point', 'two_point'], default='one_point')
    parser.add_argument('--mutation', choices=['bit_flip', 'swap'], default='bit_flip')
    parser.add_argument('--mutation_rate', type=float, default=0.1)
    args = parser.parse_args()

    # Load puzzle
    data = args.file.readlines()
    R, C = map(int, data[0].split())
    rows = [list(map(int, line.split())) for line in data[1:R + 1]]
    cols = [list(map(int, line.split())) for line in data[R + 1:R + 1 + C]]

    nonogram = Nonogram(rows, cols)

    # Run algorithm
    if args.algorithm == 'full':
        grid, loss = full_search(nonogram)
    elif args.algorithm == 'hill':
        grid, loss = hill_climbing(nonogram, args.max_iter, stochastic=False)
    elif args.algorithm == 'hill_stoch':
        grid, loss = hill_climbing(nonogram, args.max_iter, stochastic=True)
    elif args.algorithm == 'tabu':
        grid, loss = tabu_search(nonogram, args.max_iter, args.tabu_size)
    elif args.algorithm == 'genetic':
        grid, loss = genetic_algorithm(
            nonogram, args.pop_size, args.max_gen,
            args.crossover, args.mutation, args.mutation_rate
        )

    # Output results
    if grid is None:
        print("No solution found", file=sys.stderr)
        sys.exit(1)

    print_grid(grid)
    print(f"Loss: {loss}")


if __name__ == '__main__':
    main()