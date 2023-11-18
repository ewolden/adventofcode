from os import replace
import re

def find_bag_contents(bag):
    contents = bag.split('contain')[1]
    bag_contents = []
    for inner_bag in contents.split(','):
        bag_contents.append(inner_bag.strip())
    return [bag.split('contain')[0].strip(), bag_contents]


def find_number_of_subbags(list_of_bags, next_bag):
    totalNumberOfBags = 0
    #print(next_bag)
    for bag in list_of_bags:
        if next_bag in bag[0]:
            for inner_bag in bag[1]:
                if inner_bag.strip() == 'no other':
                    return 1
                else:
                    #print(int(inner_bag[0]))
                    totalNumberOfBags = totalNumberOfBags + int(inner_bag[0]) * find_number_of_subbags(list_of_bags, inner_bag[1:].strip())
                    #print(totalNumberOfBags, inner_bag)
                    #print(totalNumberOfBags)
    return totalNumberOfBags + 1


bag_list = []

testbaglist = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
number_of_bags = 0

for line in testbaglist.split('\n'):
    line = line.replace('.','')
    line = line.replace('bags','')
    line = line.replace('bag','')
    currentbag = find_bag_contents(line)
    bag_list.append(currentbag)
#print(find_number_of_subbags(bag_list,'shiny gold') - 1 )


bag_list = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.replace('.','')
        line = line.replace('bags','')
        line = line.replace('bag','')
        
        currentbag = find_bag_contents(line)
        #if 'shiny gold' in currentbag[0]:
        #    bags_to_search.append(currentbag[1])


        bag_list.append(currentbag)
print(find_number_of_subbags(bag_list,'shiny gold') - 1)



# done_bags = ['o other']
# while bags_to_search:
#     #print('before', bags_to_search)
#     current_bag_to_search_for = bags_to_search[0]
#     for bag in bag_list:
#         for inner_bag in bag[1]:
#             if 
#             #if current_bag_to_search_for in inner_bag and bag[0] not in done_bags and bag[0] not in bags_to_search:
#             #    bags_to_search.append(bag[0])
#     #number_of_bags = number_of_bags + 1
#     done_bags.append(bags_to_search.pop(0))
#     #print('after', bags_to_search)
#     #break
#print(number_of_bags)
#with open('input.txt', 'r') as f:
#    for line in f:
        