import sys

print(sys.argv[1])

with open(sys.argv[1], 'r') as numFile:
    array = []
    for line in numFile:
        array.append(line.rstrip('\n'))

print ("array = ", array)
