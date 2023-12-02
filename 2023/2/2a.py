bag_contents = {'red': 12, 'green': 13, 'blue': 14}
total_ids = 0
with open('2input.txt','r') as f:
    for line in f:
        game_id = line[4:line.index(':')]
        sets = line[line.index(':')+1:].split(';')
        set_works = True
        for game in sets:
            game = game.strip()
            for draw in game.split(','):
                draw = draw.strip()
                if bag_contents[draw[draw.index(' ')+1:]] < int(draw[:draw.index(' ')]): set_works = False
        if set_works: total_ids += int(game_id)
print(total_ids)