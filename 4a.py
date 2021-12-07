import numpy as np

def calc_unmarked_nums(board, marker_board):
    total_sum = 0
    for x_index, column in enumerate(board):
        for y_index, value in enumerate(column):
            if marker_board[x_index, y_index] == 0:
                total_sum += value
    return total_sum

boards = []
numbers = []
with open('4input.txt','r') as f:
    numbers = np.array(f.readline().strip().split(','))
    f.readline()
    current_board = np.empty(shape=(5,5))
    current_index = 0
    for line in f:
        if line.strip() == '':
            boards.append(np.copy(current_board))
            current_board = np.empty(shape=(5,5))
            current_index = 0
            continue
        current_board[current_index] = line.strip().split()
        current_index += 1
    boards.append(np.copy(current_board))

bingo_numbers = np.zeros_like(boards)

total_unmarked_sum = 0
last_number = 0
finished = False
for number in numbers:
    for board_index, board in enumerate(boards):
        result = np.where(board == int(number))
        if result[0].size != 0:
            list_of_results = list(zip(result[0], result[1]))
            for result_coordinate in list_of_results:
                bingo_numbers[board_index][result_coordinate[0],result_coordinate[1]] = 1
    for board_index, board in enumerate(bingo_numbers):
        for i in range(5):
            if np.sum(board[i,:]) == 5 or np.sum(board[:,i]) == 5:
                total_unmarked_sum = calc_unmarked_nums(boards[board_index], board)
                finished = True
                last_number = int(number)
                break
        if finished:
            break
    if finished:
        break

print(total_unmarked_sum * last_number)


            

#print(bingo_numbers)

