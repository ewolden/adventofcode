bag_contents = {'red': 12, 'green': 13, 'blue': 14}
total_ids = 0
with open('2input.txt','r') as f:
    for line in f:
        min_number_of_cubes = {'red': 0, 'green': 0, 'blue': 0}
        game_id = line[4:line.index(':')]
        sets = line[line.index(':')+1:].split(';')
        for game in sets:
            game = game.strip()
            for draw in game.split(','):
                draw = draw.strip()
                if min_number_of_cubes[draw[draw.index(' ')+1:]] < int(draw[:draw.index(' ')]): min_number_of_cubes[draw[draw.index(' ')+1:]] = int(draw[:draw.index(' ')])
        total_ids += min_number_of_cubes['red'] * min_number_of_cubes['blue'] * min_number_of_cubes['green']
print(total_ids)