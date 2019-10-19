# namedtyple() Tutorial 
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

file = open('collections_namedtuple.txt')
lines = file.readlines()
numOfStudents = int(lines[0])

index = lines[1].split()
Student = namedtuple('Student', [index[0], index[1], index[2], index[3]])
iteration = 0

position = 2
students = list()

while iteration < numOfStudents:
    line = lines[position].split()
    student = Student(line[0], line[1], line[2], line[3])
    students.append(student)
    position += 1
    iteration += 1
        
sumMarks = 0
for student in students:
    sumMarks += int(getattr(student, 'MARKS'))
    
print(sumMarks / len(students))
