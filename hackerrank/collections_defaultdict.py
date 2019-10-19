# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

file = open('collections_defaultdict.txt')
lines = file.readlines()

firstline = lines[0].split()
numOfWordsGroupA = int(firstline[0])
numOfWordsGroupB = int(firstline[1])
d = defaultdict(list)

for i in range(numOfWordsGroupA):
    letter = lines[i+1].split()
    d[letter[0]].append(i + 1)

index = numOfWordsGroupA + 1

for x in range(numOfWordsGroupB):
    char = lines[index].split()
    if char[0] in d.keys():
        result = d[char[0]]
        print(*result)
    else:
        print('-1')
        
    index += 1
    