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
    centers = []
    for diag in diagonal_slices(input_matrix):
        combined_string = ''.join([t[0] for t in diag])
        print(combined_string)
        for match in itertools.chain(re.finditer('MAS', combined_string), re.finditer('SAM', combined_string)):
            print(match)
            print(match.start(), diag[match.start()][1], diag[match.start()][2])
            direction = diag[match.start()][2]
            center = (diag[match.start()][1][0] + 1, diag[match.start()][1][1] - 1)
            if (input_matrix[center[0] - 1][center[1] - 1] == 'M' and \
                input_matrix[center[0] + 1][center[1] + 1] == 'S') or \
                (input_matrix[center[0] - 1][center[1] - 1] == 'S' and \
                    input_matrix[center[0] + 1][center[1] + 1] == 'M'):

                print(combined_string, (center[0], center[1]), input_matrix[center[0]][center[1]])
                num_occurences += 1
                centers.append(center)
            # elif diag[match.start()][2] == 'top-left':
            #     if (input_matrix[center[0] - 1][center[1] + 1] == 'M' and \
            #         input_matrix[center[0] + 1][center[1] - 1] == 'S') or \
            #         (input_matrix[center[0] - 1][center[1] + 1] == 'S' and \
            #          input_matrix[center[0] + 1][center[1] - 1] == 'M'):
            #         print(f'center: {center}, direction: {direction}')
            #         print(combined_string, (match.start(), diag[match.start()][1], diag[match.start()][2]), input_matrix[center[0]][center[1]])
            #         num_occurences += 1
            #         centers.append(center)


print(num_occurences)
print(centers)



#Intent for unity catalog