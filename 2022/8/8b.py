def find_visible_trees(trees, height):
    visible_trees = 0
    for tree_x in trees:
        if tree_x < height:
            visible_trees = visible_trees + 1
        else:
            visible_trees = visible_trees + 1
            break
    return visible_trees

def find_scenic_score(trees, location):
    height = trees[location[0]][location[1]]
    
    left_visible = find_visible_trees(list(reversed(trees[location[0]][:location[1]])), height)
    right_visible = find_visible_trees(trees[location[0]][location[1]+1:], height)
    top_visible = find_visible_trees(list(reversed(list(zip(*trees))[location[1]][:location[0]])), height)
    bottom_visible = find_visible_trees(list(zip(*trees))[location[1]][location[0]+1:], height)

    return top_visible * left_visible * bottom_visible * right_visible

trees = []
with open('8input.txt','r') as f:
    for line in f:
        trees.append([int(x) for x in list(line.rstrip())])
        
list_of_trees = []
for i, tree in enumerate(trees):
    for j, inner_tree in enumerate(trees[i]):
        list_of_trees.append(find_scenic_score(trees, [i, j]))

print(max(list_of_trees))