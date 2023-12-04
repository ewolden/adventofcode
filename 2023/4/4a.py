total_points = 0
with open('4input.txt','r') as f:
    for line in f:
        line = line.replace('  ', ' ')
        winning_nums = line.split('|')[0].split(':')[1].strip().split(' ')
        play_nums = line.split('|')[1].strip().split(' ')
        total_wins = [num for num in play_nums if num in winning_nums]
        game_points = int(pow(2,len(total_wins)- 1)) 
        total_points += game_points
print(total_points)