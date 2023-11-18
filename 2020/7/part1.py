from os import replace
import re

def find_bag_contents(bag):
    contents = bag.split('contain')[1]
    bag_contents = []
    for inner_bag in contents.split(','):
        bag_contents.append(inner_bag.strip())
    return [bag.split('contain')[0].strip(), bag_contents]





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
bags_to_search = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.replace('.','')
        line = line.replace('bags','')
        line = line.replace('bag','')
        
        currentbag = find_bag_contents(line)
        for bag in currentbag[1]:
            if 'shiny gold' in bag:
                bags_to_search.append(currentbag[0])
                break

        bag_list.append(currentbag)

done_bags = ['o other']
while bags_to_search:
    #print('before', bags_to_search)
    current_bag_to_search_for = bags_to_search[0]
    for bag in bag_list:
        for inner_bag in bag[1]:
            if current_bag_to_search_for in inner_bag and bag[0] not in done_bags and bag[0] not in bags_to_search:
                bags_to_search.append(bag[0])
    number_of_bags = number_of_bags + 1
    done_bags.append(bags_to_search.pop(0))
    #print('after', bags_to_search)
    #break
print(number_of_bags)
#with open('input.txt', 'r') as f:
#    for line in f:
        