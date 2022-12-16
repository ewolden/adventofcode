class Tree:
    def __init__(self, height = None, left = None, right = None, up = None, down = None) -> None:
        self.height = height
        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def __str__(self) -> str:
        current_dirs = []
        if self.left:
            current_dirs.append('L')
        if self.right:
            current_dirs.append('R')
        if self.up:
            current_dirs.append('U')
        if self.down:
            current_dirs.append('D')
        current_dirs = ",".join(current_dirs)
        return "height: " + str(self.height) + ", current dirs :"  + current_dirs

def print_heightmap(input_array):
    for line in input_array:
        print(line)

def check_if_not_visited_and_okay(height_array, current_height, next_location, grid_size, visited):
    if next_location[0] < 0 or next_location[0] > grid_size[0] \
        or next_location[1] < 0 or next_location[1] > grid_size[1] \
            or next_location in visited:
        return False
    if height_array[next_location[0]][next_location[1]] == current_height \
        or height_array[next_location[0]][next_location[1]] == current_height + 1:
        return True
    else:
        return False

def create_tree_from_loc(height_array, current_height, current_location, visited, current_tree):
    current_tree.height = current_height
    current_location_height = height_array[current_location[0]][current_location[1]] 
    grid_size = [len(height_array) - 1, len(height_array[0]) - 1]
    current_visited = visited.copy()
    if current_location_height == 27:
        return current_tree
    else:
        #try to go in all directions
        #left
        next_location = [current_location[0] - 1, current_location[1]]
        if check_if_not_visited_and_okay(height_array, current_height, next_location, grid_size, current_visited):
            current_visited.append(next_location)
            next_location_height = height_array[next_location[0]][next_location[1]]
            current_tree.left = create_tree_from_loc(height_array, next_location_height, next_location,current_visited, Tree())
        #right
        next_location = [current_location[0] + 1, current_location[1]]
        if check_if_not_visited_and_okay(height_array, current_height, next_location, grid_size, current_visited):
            current_visited.append(next_location)
            next_location_height = height_array[next_location[0]][next_location[1]]
            current_tree.right = create_tree_from_loc(height_array, next_location_height, next_location,current_visited, Tree())
        #up
        next_location = [current_location[0], current_location[1] - 1]
        if check_if_not_visited_and_okay(height_array, current_height, next_location, grid_size, current_visited):
            current_visited.append(next_location)
            next_location_height = height_array[next_location[0]][next_location[1]]
            current_tree.up = create_tree_from_loc(height_array, next_location_height, next_location,current_visited, Tree())
        #down
        next_location = [current_location[0], current_location[1] + 1]
        if check_if_not_visited_and_okay(height_array, current_height, next_location, grid_size, current_visited):
            current_visited.append(next_location)
            next_location_height = height_array[next_location[0]][next_location[1]]
            current_tree.down = create_tree_from_loc(height_array, next_location_height, next_location,current_visited, Tree())
        #print(current_tree)
        return current_tree


def dfs(input_tree):
    queue = [(input_tree, [])]
    while queue:
        (tree, path) = queue.pop(0)
        tree.path = path.copy() + [tree]
        if tree and tree.height == 27:
            yield tree.path
        if tree and tree.left:
            if tree.left not in tree.path:
                #visited.append(tree.left)
                queue.append((tree.left, tree.path))
        if tree and tree.right:
            if tree.right not in tree.path:
                #visited.append(tree.right)
                queue.append((tree.right, tree.path))
                #dfs(tree.right, target_node, visited)
        if tree and tree.up:
            if tree.up not in tree.path:
                #visited.append(tree.up)
                queue.append((tree.up, tree.path))
                #dfs(tree.up, target_node, visited)
        if tree and tree.down:
            if tree.down not in tree.path:
                #visited.append(tree.down)
                queue.append((tree.down, tree.path))
                #dfs(tree.down, target_node, visited)

height_array = []
starting_position = []
with open('12input.txt','r') as f:
    for i, line in enumerate(f):
        current_line = []
        for j, item in enumerate(line.rstrip()):
            if item == 'S':
                current_line.append(1)
                starting_position = [i, j]
            elif item == 'E':
                current_line.append(27)
            else:
                current_line.append(ord(item) - 96)
        height_array.append(current_line)
root_node = Tree()

create_tree_from_loc(height_array, 0, starting_position, [], root_node)    
print(root_node)
for trees in list(dfs(root_node)):
    #for single_tree in trees:
     #   print(single_tree)
    #break
    print(len(trees) - 1)
