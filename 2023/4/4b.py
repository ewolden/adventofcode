total_scratchcards = []
with open('4input.txt','r') as f:
    for idx, line in enumerate(f):
        if len(total_scratchcards) - 1 < idx:
            total_scratchcards.append(1)
        line = line.replace('  ', ' ')
        winning_nums = line.split('|')[0].split(':')[1].strip().split(' ')
        play_nums = line.split('|')[1].strip().split(' ')
        total_wins = [num for num in play_nums if num in winning_nums]
        for wins, __ in enumerate(total_wins):
            if len(total_scratchcards) - 1 < idx + 1 + wins:
                total_scratchcards.append(total_scratchcards[idx] + 1)
            else:
                total_scratchcards[idx + 1 + wins] += total_scratchcards[idx]
print(sum(total_scratchcards))
