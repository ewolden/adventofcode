state = [{'X': 1}]
pixels = [' ']*241
pixels[0] = '.'
i = 1
with open('10input.txt','r') as f:
    num_to_add = 0
    pixelrow = 0
    for line in f:
        if line[:4] == 'noop':
            new_instruction={'X': state[i-1]['X'] + num_to_add}
            state.append(new_instruction)
            if abs(state[i-1]['X'] + num_to_add - (i-1 - pixelrow*40)) < 2:
                pixels[i] = '#'
            i = i + 1
            if i % 40 == 0:
                pixelrow = pixelrow + 1
            num_to_add = 0
        else:
            new_instructions = [{'X': state[i-1]['X'] + num_to_add}, \
                {'X': state[i-1]['X'] + num_to_add}]
            if abs(state[i-1]['X'] + num_to_add - (i-1 - pixelrow*40)) < 2:
                pixels[i] = '#'
            if abs(state[i-1]['X'] + num_to_add - ((i ) - pixelrow*40)) < 2:
                pixels[i+1] = '#'
            state.extend(new_instructions)
            num_to_add = int(line.rstrip().split(' ')[1])
            i = i + 2
            if i % 40 == 0 or (i-1) % 40 == 0:
                pixelrow = pixelrow + 1
        print(pixelrow)
        #if i == 40:
        #    break

print(state[10])

print(''.join(pixels[1:40]))
print(''.join(pixels[41:80]))
print(''.join(pixels[81:120]))
print(''.join(pixels[121:160]))
print(''.join(pixels[161:200]))
print(''.join(pixels[201:240]))