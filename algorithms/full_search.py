import math


def full_search(nonogram):
    R, C = nonogram.R, nonogram.C
    best_grid = None  # Najlepsza znaleziona siatka
    best_loss = math.inf  # Minimalna strata (początkowo nieskończoność)

    # wszystkie mozliwosci
    for i in range(2 ** (R * C)):
        grid = []
        # Konwersja liczby na siatkę
        for r in range(R):
            row = []
            for c in range(C):
                bit_index = r * C + c  # Pozycja bitu
                bit = (i >> bit_index) & 1  # Wyciągnięcie bitu
                row.append(bit)
            grid.append(row) # dodanie do siatki wiersza

        loss_val = nonogram.loss(grid)
        if loss_val == 0:  # Rozwiazanie idealne
            return grid, 0
        if loss_val < best_loss:  # Aktualizacja najlepszego
            best_grid = grid
            best_loss = loss_val

    return best_grid, best_loss  # najlepsze znalezione
