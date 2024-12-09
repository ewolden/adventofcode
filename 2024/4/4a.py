def vertical_slices(matrix):
    return [''.join(list(col)) for col in zip(*matrix)]

def diagonal_slices(matrix):
    diagonals = []

    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diag = []
        for i in range(max(0, d - cols + 1), min(d + 1, rows)):
            j = d - i
            diag.append(matrix[i][j])
        if len(diag) > 3:
            diagonals.append(''.join(diag))

    # Top-right to bottom-left diagonals
    for d in range(rows + cols - 1):
        diag = []
        for i in range(max(0, d - cols + 1), min(d + 1, rows)):
            j = cols - 1 - (d - i)
            if 0 <= j < cols:
                diag.append(matrix[i][j])
        if len(diag) > 3:
            diagonals.append(''.join(diag))

    return diagonals

import re
num_occurences = 0
with open('4input.txt','r') as f:
    input_matrix = []
    for line in f:
        input_matrix.append(line.strip())
        num_occurences += len(re.findall('(?=XMAS|SAMX)', line))
        
    for slice in vertical_slices(input_matrix):
        num_occurences += len(re.findall('(?=XMAS|SAMX)', slice))
    
    for slice in diagonal_slices(input_matrix):
        num_occurences += len(re.findall('(?=XMAS|SAMX)', slice))
print(num_occurences)