import math


def full_search(nonogram):
    R, C = nonogram.R, nonogram.C
    # Najlepsza znaleziona siatka
    best_grid = None
    # Minimalna strata (początkowo nieskończoność)
    best_loss = math.inf

    # wszystkie mozliwosci
    for i in range(2 ** (R * C)):
        grid = []
        # Konwersja liczby na siatkę
        for r in range(R):
            row = []
            for c in range(C):
                # Pozycja bitu
                bit_index = r * C + c
                # Wyciągnięcie bitu
                bit = (i >> bit_index) & 1
                row.append(bit)
                # dodanie do siatki wiersza
            grid.append(row)

        loss_val = nonogram.loss(grid)
        # Rozwiazanie idealne
        if loss_val == 0:
            return grid, 0
        # Aktualizacja najlepszego
        if loss_val < best_loss:
            best_grid = grid
            best_loss = loss_val
    # najlepsze znalezione
    return best_grid, best_loss
