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
        previous_movement = [0,0]
        if movment_direction == 'U':
            previous_movement = [0,1]
        elif movment_direction == 'D':
            previous_movement = [0,-1]
        elif movment_direction == 'L':
            previous_movement = [-1,0]
        elif movment_direction == 'R':
            previous_movement = [1,0]
        move_to_do = ''
        for idx, _ in enumerate(snake_body):
            start_position = snake_body[idx].copy()
            if idx == 0:
                snake_body[idx][0] = snake_body[idx][0] + previous_movement[0]
                snake_body[idx][1] = snake_body[idx][1] + previous_movement[1]
            elif abs(snake_body[idx][0] - snake_body[idx-1][0]) > 1 \
                or abs(snake_body[idx][1] - snake_body[idx-1][1]) > 1:
                
                #move x axis
                if abs(snake_body[idx][0] - snake_body[idx - 1][0]) > 1:
                    #check if diagonal
                    if abs(snake_body[idx][1] - snake_body[idx-1][1]) > 0:
                         snake_body[idx][0] = snake_body[idx][0] + sign((snake_body[idx-1][0] - snake_body[idx][0])) * 1
                         snake_body[idx][1] = snake_body[idx][1] + sign((snake_body[idx-1][1] - snake_body[idx][1])) * 1
                    #not diagonal movment
                    else:
                        snake_body[idx][0] = snake_body[idx][0] + sign((snake_body[idx-1][0] - snake_body[idx][0])) * 1

                #move y axis
                if abs(snake_body[idx][1] - snake_body[idx - 1][1]) > 1:
                    #check if diagonal
                    if abs(snake_body[idx][0] - snake_body[idx-1][0]) > 0:
                         snake_body[idx][0] = snake_body[idx][0] + sign((snake_body[idx-1][0] - snake_body[idx][0])) * 1
                         snake_body[idx][1] = snake_body[idx][1] + sign((snake_body[idx-1][1] - snake_body[idx][1])) * 1
                    #not diagonal movment
                    else:
                        snake_body[idx][1] = snake_body[idx][1] + sign((snake_body[idx-1][1] - snake_body[idx][1])) * 1
                previous_movement[0] = snake_body[idx][0] - start_position[0]
                previous_movement[1] = snake_body[idx][1] - start_position[1] 
                
        #print_snake(snake_body,28)
        if snake_body[idx] not in tail_visited:
            tail_visited.append(snake_body[idx].copy())

    return snake_body, tail_visited

with open('9input.txt','r') as f:
    snake_body = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    tail_visited = [[0,0]]
    for line in f:
        snake_body, this_tail_visit = move_snake(snake_body, line.rstrip())
        tail_visited = tail_visited + this_tail_visit
unique_visits = [list(x) for x in set(tuple(x) for x in tail_visited)]
#print(tail_visited)
print(len(unique_visits))
