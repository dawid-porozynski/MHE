import random

class Nonogram:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.R = len(rows)
        self.C = len(cols)

    def compute_blocks(self, vector):
        blocks = []
        count = 0
        for v in vector:
            if v == 1:
                count += 1
            else:
                if count > 0:
                    # Zapis bloku przy zmianie 1->0
                    blocks.append(count)
                    count = 0
        if count > 0:
            # Ostatni blok na końcu
            blocks.append(count)
        return blocks

    def loss(self, grid):
        errors = 0

        # sprawdza rows
        for i in range(self.R): # sprawdza rows
            actual = self.compute_blocks(grid[i])
            if actual != self.rows[i]:
                errors += 1

        # sprawdza kolumny
        for j in range(self.C):
            col = [grid[i][j] for i in range(self.R)]
            actual = self.compute_blocks(col)
            if actual != self.cols[j]:
                errors += 1
        return errors

def random_grid(R, C):
    return [[random.randint(0, 1) for _ in range(C)] for _ in range(R)]

def generate_neighbours(grid):
    neighbours = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid = [row.copy() for row in grid]
            new_grid[i][j] = 1 - new_grid[i][j]
            neighbours.append(new_grid)
    return neighbours