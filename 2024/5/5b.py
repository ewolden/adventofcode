ok_nums = []
ordering = []
finsihed_order = False

def order_input_list(ordering, input):
    is_ordered = True
    final_order = []
    for order in ordering:
        if order[0] in input and order[1] in input:
            if not input.index(order[0]) < input.index(order[1]):
                is_ordered = False
                next_order = input.copy()
                next_order[input.index(order[0])] = order[1]
                next_order[input.index(order[1])] = order[0]                
                final_order = order_input_list(ordering, next_order)
                break
    if is_ordered:  
        return input
    elif final_order:
        return final_order

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
            if not line_ok:
                new_order = order_input_list(ordering, input)
                #print(clean_line, order, input[len(input) // 2])
                ok_nums.append(new_order[len(new_order) // 2])
print(sum(ok_nums))