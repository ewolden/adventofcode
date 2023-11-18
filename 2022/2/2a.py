hands = {
    'A': {
        'name': 'Rock',
        'letter': 'A',
        'points': 1,
        'beats': 'Z'
    },
    'B': {
        'name': 'Paper',
        'letter': 'B',
        'points': 2,
        'beats': 'X'
    },
    'C': {
        'name': 'Scissors',
        'letter': 'C',
        'points': 3,
        'beats': 'Y'
    },
    'X': {
        'name': 'Rock',
        'letter': 'X',
        'points': 1
    },
    'Y': {
        'name': 'Paper',
        'letter': 'Y',
        'points': 2
    },
    'Z': {
        'name': 'Scissors',
        'letter': 'Z',
        'points': 3
    }
}

total_score = 0
with open('2input.txt','r') as f:
    for line in f:
        opponent = hands.get(line.split(' ')[0])
        player = hands.get(line.split(' ')[1].rstrip())

        if opponent.get('name') == player.get('name'): ## draw
            total_score = total_score + 3 + player.get('points')
        elif opponent.get('beats') == player.get('letter'): ## loss
            total_score = total_score + player.get('points')
        else: ## Win
            total_score = total_score + 6 + player.get('points')

print(total_score)
