def check_if_visible(trees, location):
    height = trees[location[0]][location[1]]
    is_visible = True
    ## stop if we are on an edge
    if location[0] == 0 or location[1] == 0 or location[0] == len(trees) - 1 or location[1] == len(trees) - 1:
        return is_visible

    left_visible = True
    right_visible = True
    #Check the row
    for idx, tree_x in enumerate(trees[location[0]]):
        if idx < location[1] and tree_x >= height:
            left_visible = False
        elif idx > location[1] and tree_x >= height:
            right_visible = False

    #Check the column
    top_visible = True
    bottom_visible = True
    trees_flipped =  list(zip(*trees))
    for idx, tree_y in enumerate(trees_flipped[location[1]]):
        if idx < location[0] and tree_y >= height:
            top_visible= False
        elif idx > location[0] and tree_y >= height:
            bottom_visible = False
    if not left_visible and not right_visible and not top_visible and not bottom_visible:
        is_visible = False
    return is_visible

trees = []
with open('8input.txt','r') as f:
    for line in f:
        trees.append([int(x) for x in list(line.rstrip())])
        
total_visible_trees = 0
for i, tree in enumerate(trees):
    for j, inner_tree in enumerate(trees[i]):
        if check_if_visible(trees, [i, j]):
            total_visible_trees = total_visible_trees + 1
print(total_visible_trees)