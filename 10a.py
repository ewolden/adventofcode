state = [{'X': 1, 'signal_strength': 1}]
i = 1
with open('10input.txt','r') as f:
    num_to_add = 0
    for line in f:
        if line[:4] == 'noop':
            new_instruction={'X': state[i-1]['X'] + num_to_add, 'signal_strength': (state[i-1]['X'] + num_to_add) * i}
            state.append(new_instruction)
            i = i + 1
            num_to_add = 0
        else:
            new_instructions = [{'X': state[i-1]['X'] + num_to_add, 'signal_strength': (state[i-1]['X'] + num_to_add) * i}, \
                {'X': state[i-1]['X'] + num_to_add, 'signal_strength': (state[i-1]['X'] + num_to_add) * (i+1)}]
            state.extend(new_instructions)
            num_to_add = int(line.rstrip().split(' ')[1])
            i = i + 2
signal_strengths = [
    state[20]['signal_strength'],
    state[60]['signal_strength'],
    state[100]['signal_strength'],
    state[140]['signal_strength'],
    state[180]['signal_strength'],
    state[220]['signal_strength'],
]
print(sum(signal_strengths))