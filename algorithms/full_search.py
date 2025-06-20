import sys
from models.nonogram import Nonogram


def full_search(nonogram):
    R, C = nonogram.R, nonogram.C
    total_cells = R * C
    if total_cells > 20:
        print("Full search skipped for grid size > 20", file=sys.stderr)
        return None, float('inf')

    best_grid = None
    best_loss = float('inf')
    for i in range(2 ** total_cells):
        grid = []
        for r in range(R):
            row = []
            for c in range(C):
                bit_index = r * C + c
                bit = (i >> bit_index) & 1
                row.append(bit)
            grid.append(row)
        loss_val = nonogram.loss(grid)
        if loss_val == 0:
            return grid, 0
        if loss_val < best_loss:
            best_loss = loss_val
            best_grid = grid
    return best_grid, best_loss