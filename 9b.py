def print_snake(snake_body, canvas_size):
    for i in range(-int(canvas_size/2),int(canvas_size/2)):
        line = ''
        for j in range(-int(canvas_size/2),int(canvas_size/2)):
            if j == 0 and i == 0:
                line = line + 's'
                continue
            if [j, -i] in snake_body:
                line = line + str(snake_body.index([j,-i]))
            else:
                line = line + '.'
            
        print(line)
    print()
        

def move_snake(incoming_snake_body, movement):
    movment_direction = movement.split(' ')[0]
    tail_visited = []
    snake_body = incoming_snake_body.copy()
    sign = lambda a: (a>0) - (a<0)
    for idx in range(int(movement.split(' ')[1])):
        previous_movement = ''
        move_to_do = ''
        for idx, _ in enumerate(snake_body):
            this_movement = ''
            start_position = snake_body[idx].copy()
            if idx == 0 or abs(snake_body[idx][0] - snake_body[idx-1][0]) > 1 \
                or abs(snake_body[idx][1] - snake_body[idx-1][1]) > 1:
                if movment_direction == 'U':
                    snake_body[idx][1] = snake_body[idx][1] + 1
                    if idx > 0 and abs(snake_body[idx][0] - snake_body[idx-1][0]) > 0:                       
                        snake_body[idx][0] = snake_body[idx][0] + sign((snake_body[idx-1][0] - snake_body[idx][0])) * 1
                elif movment_direction == 'D':
                    snake_body[idx][1] = snake_body[idx][1] - 1
                    if idx > 0 and abs(snake_body[idx][0] - snake_body[idx-1][0]) > 0:
                        snake_body[idx][0] = snake_body[idx][0] + sign((snake_body[idx-1][0] - snake_body[idx][0])) * 1
                elif movment_direction == 'L':
                    #print(snake_body[idx][1], snake_body[idx-1][1] , snake_body[idx][1] + sign((snake_body[idx-1][1] - snake_body[idx][1])) * 1)
                    snake_body[idx][0] = snake_body[idx][0] - 1
                    if idx > 0 and abs(snake_body[idx][1] - snake_body[idx-1][1]) > 0:
                        snake_body[idx][1] = snake_body[idx][1] + sign((snake_body[idx-1][1] - snake_body[idx][1])) * 1
                elif movment_direction == 'R':
                    snake_body[idx][0] = snake_body[idx][0] + 1
                    if idx > 0 and abs(snake_body[idx][1] - snake_body[idx-1][1]) > 0:
                        snake_body[idx][1] = snake_body[idx][1] + sign((snake_body[idx-1][1] - snake_body[idx][1])) * 1
                if snake_body[idx][0] - start_position[0] > 0:
                    this_movement = 'R'
                elif snake_body[idx][0] - start_position[0] < 0:
                    this_movement = 'L'
                if snake_body[idx][1] - start_position[1] > 0:
                    this_movement = 'U'
                elif snake_body[idx][1] - start_position[1] < 0:
                    this_movement = 'D'
        print_snake(snake_body,28)
        if snake_body[idx] not in tail_visited:
            tail_visited.append(snake_body[idx].copy())
        #print(movement, snake_body)


        #     if movment_direction == 'U':
        #         if idx > 0 and abs(current_part[1] - snake_body[idx-1][1]) <= 1:
        #             new_snake.append(current_part.copy())
        #             continue
        #         current_part[1] = current_part[1] + 1 # move y direction
        #         new_snake.append(current_part.copy())
        #         if current_part[0] == next_part[0]:  # move x direction
        #             if current_part[1] - next_part[1] <= 1:
        #                 continue
        #             #next_part[1] = next_part[1] + 1
        #         else:
        #             if current_part[1] - next_part[1] <= 1:
        #                 continue
        #            # next_part[1] = next_part[1] + 1
        #             next_part[0] = current_part[0]

        #     elif movment_direction == 'D':
        #         if idx > 0 and abs(current_part[1] - snake_body[idx-1][1]) <= 1:
        #             new_snake.append(current_part.copy())
        #             continue
        #         current_part[1] = current_part[1] - 1
        #         new_snake.append(current_part.copy())
        #         if current_part[0] == next_part[0]:
        #             if next_part[1] - current_part[1] <= 1:
        #                 continue
        #             #next_part[1] = next_part[1] - 1
        #         else:
        #             if next_part[1] - current_part[1] <= 1:
        #                 continue
        #             #next_part[1] = next_part[1] - 1
        #             next_part[0] = current_part[0]

        #     elif movment_direction == 'R':
        #         if idx > 0 and abs(current_part[0] - snake_body[idx-1][0]) <= 1:
        #             new_snake.append(current_part.copy())
        #             continue
        #         current_part[0] = current_part[0] + 1
        #         new_snake.append(current_part.copy())
        #         if current_part[1] == next_part[1]:
        #             if current_part[0] - next_part[0] <= 1:
        #                 continue
        #             #next_part[0] = next_part[0] + 1
        #         else:
        #             if current_part[0] - next_part[0] <= 1:
        #                 continue
        #             #next_part[0] = next_part[0] + 1
        #             next_part[1] = current_part[1]

        #     elif movment_direction == 'L':
        #         if idx > 0 and abs(current_part[0] - snake_body[idx-1][0]) <= 1:
        #             new_snake.append(current_part.copy())
        #             continue
        #         if current_part[1] == next_part[1]:
        #             if next_part[0] - current_part[0] <= 1:
        #                 new_snake.append(current_part.copy())
        #                 continue
        #             #next_part[0] = next_part[0] - 1
        #         else:
        #             if next_part[0] - current_part[0] <= 1:
        #                 new_snake.append(current_part.copy())
        #                 continue
        #             #next_part[0] = next_part[0] - 1
        #             next_part[1] = current_part[1]
        #         current_part[0] = current_part[0] - 1
        #         new_snake.append(current_part.copy())
            
        #     if idx == 8 and current_part != [] and current_part not in tail_visited:
        #             tail_visited.append(current_part.copy())
        #             new_snake.append(current_part.copy())

        #print(movement, new_snake)
        # snake_body = new_snake
    return snake_body, tail_visited

with open('9testinput2.txt','r') as f:
    snake_body = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    tail_visited = [[0,0]]
    i = 0
    for line in f:
        snake_body, this_tail_visit = move_snake(snake_body, line.rstrip())
        tail_visited = tail_visited + this_tail_visit
        i = i + 1
        if i == 3:
            break
        print(line.rstrip(), snake_body)
unique_visits = [list(x) for x in set(tuple(x) for x in tail_visited)]
#print(tail_visited)
print(len(unique_visits))
