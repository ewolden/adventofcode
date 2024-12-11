ok_nums = []
ordering = []
finsihed_order = False
with open('5input.txt','r') as f:
    for line in f:
        clean_line = line.strip()
        if clean_line == '':
            finsihed_order = True
            continue
        if finsihed_order == False:
            ordering.append([int(x) for x in clean_line.split('|')])
        else:
            input = [int(x) for x in clean_line.split(',')]
            line_ok = True
            for order in ordering:
                if order[0] in input and order[1] in input:
                    if not input.index(order[0]) < input.index(order[1]):
                       line_ok = False
            if line_ok:
                #print(clean_line, order, input[len(input) // 2])
                ok_nums.append(input[len(input) // 2])
print(sum(ok_nums))