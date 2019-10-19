# HackerRank collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

import collections

file = open('collections_counter_input.txt')
lines = file.readlines()

numOfShoes = lines[0]
shoesStock = collections.Counter(lines[1].split())
numOfCustomers = int(lines[2])
d = dict()

for key, value in shoesStock.items():   
    d[int(key)] = value
    
counter = 0
index = 3
total = 0

while counter < numOfCustomers:
    
    counter += 1
    line = lines[index].split()
    size = int(line[0])
    
    try:   
        if d[size] > 0:
            total += int(line[1])
            d[size] -= 1              
        index += 1
   
    except:
        index += 1
        continue
    

print(total)
