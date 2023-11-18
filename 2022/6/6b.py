current_chars =  []
found = False
with open('6input.txt','r') as f:
    for line in f:
        for idx, letter in enumerate(line.rstrip()):
            print(idx, letter, current_chars)
            if len(current_chars) < 13:
                current_chars.append(letter)
            elif len(current_chars) == 13:
                current_chars.append(letter)
            else:
                current_chars.pop(0)
                current_chars.append(letter)
            
            if len(current_chars) == 14 and len(set(current_chars)) == 14:
                print(idx+1, letter, current_chars)
                break