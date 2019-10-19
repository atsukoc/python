# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict
import re

file = open('collections_ordereddict.txt')
lines = file.readlines()
ordered_dict = OrderedDict()
numOfItems = int(lines[0])

index = 1
for i in range(numOfItems):
    line = lines[index].rstrip()
    item = re.search('(\D*\s*\D*)', line)
    product = item[0].rstrip()
    quantity = re.findall('\d+', line)
    
    if(product) in ordered_dict:
        ordered_dict[product] += int(quantity[0])    
    else:
        ordered_dict[product] = int(quantity[0])
    
    index += 1
    
for key, value in ordered_dict.items():
    print(key, value)