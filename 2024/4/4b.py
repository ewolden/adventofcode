def diagonal_slices(matrix):
    diagonals = []

    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diag = []
        for i in range(max(0, d - cols + 1), min(d + 1, rows)):
            j = d - i
            diag.append((matrix[i][j], (i, j), 'top-right'))
        if len(diag) > 3:
            diagonals.append(diag)

    return diagonals

import re
import itertools
num_occurences = 0
with open('4input.txt','r') as f:
    input_matrix = []
    for line in f:
        input_matrix.append(line.strip())
    for diag in diagonal_slices(input_matrix):
        combined_string = ''.join([t[0] for t in diag])
        for match in itertools.chain(re.finditer('MAS', combined_string), re.finditer('SAM', combined_string)):
            direction = diag[match.start()][2]
            center = (diag[match.start()][1][0] + 1, diag[match.start()][1][1] - 1)
            if (input_matrix[center[0] - 1][center[1] - 1] == 'M' and \
                input_matrix[center[0] + 1][center[1] + 1] == 'S') or \
                (input_matrix[center[0] - 1][center[1] - 1] == 'S' and \
                    input_matrix[center[0] + 1][center[1] + 1] == 'M'):
                num_occurences += 1

print(num_occurences)
