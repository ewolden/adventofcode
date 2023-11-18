hands = {
    'A': {
        'name': 'Rock',
        'letter': 'A',
        'points': 1,
        'beats': 'Z',
        'loses': 'Y'
    },
    'B': {
        'name': 'Paper',
        'letter': 'B',
        'points': 2,
        'beats': 'X',
        'loses': 'Z'
    },
    'C': {
        'name': 'Scissors',
        'letter': 'C',
        'points': 3,
        'beats': 'Y',
        'loses': 'X'
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
        result = line.split(' ')[1].rstrip()

        if result == 'X': ## loss
            total_score = total_score + hands.get(opponent.get('beats')).get('points')
        elif result == 'Y': ##draw
            total_score = total_score + 3 + opponent.get('points')
        else: ##win
            total_score = total_score + 6 + hands.get(opponent.get('loses')).get('points')

print(total_score)
