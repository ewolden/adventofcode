def move_tail(head_location, tail_location, movement):
    movment_direction = movement.split(' ')[0]
    head = head_location
    tail = tail_location
    tail_visited = []
    for idx in range(int(movement.split(' ')[1])):
        #print(head, tail)
        if movment_direction == 'U':
            head[1] = head[1] + 1
            if head[0] == tail[0]:
                if head[1] - tail[1] <= 1:
                    continue
                tail[1] = tail[1] + 1
            else:
                if head[1] - tail[1] <= 1:
                    continue
                tail[1] = tail[1] + 1
                tail[0] = head[0]

        elif movment_direction == 'D':
            head[1] = head[1] - 1
            if head[0] == tail[0]:
                if tail[1] - head[1] <= 1:
                    continue
                tail[1] = tail[1] - 1
            else:
                if tail[1] - head[1] <= 1:
                    continue
                tail[1] = tail[1] - 1
                tail[0] = head[0]

        elif movment_direction == 'R':
            head[0] = head[0] + 1
            if head[1] == tail[1]:
                if head[0] - tail[0] <= 1:
                    continue
                tail[0] = tail[0] + 1
            else:
                if head[0] - tail[0] <= 1:
                    continue
                tail[0] = tail[0] + 1
                tail[1] = head[1]
        

        elif movment_direction == 'L':
            head[0] = head[0] - 1
            if head[1] == tail[1]:
                if tail[0] - head[0] <= 1:
                    continue
                tail[0] = tail[0] - 1
            else:
                if tail[0] - head[0] <= 1:
                    continue
                tail[0] = tail[0] - 1
                tail[1] = head[1]
        tail_visited.append(tail.copy())
    return head, tail, tail_visited

with open('9input.txt','r') as f:
    head = [0,0]
    tail = [0,0]
    tail_visited = [[0,0]]
    for line in f:
        head, tail, this_tail_visit = move_tail(head, tail, line.rstrip())
        tail_visited = tail_visited + this_tail_visit
unique_visits = [list(x) for x in set(tuple(x) for x in tail_visited)]

print(len(unique_visits))