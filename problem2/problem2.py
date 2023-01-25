file = open('input.txt','r')


#very ugly
def evaluate(a,b):
    points = 0
    if b == 'X':
        points += 1
        if a == 'A':
            points += 3
        elif a == 'C':
            points += 6
    elif b == 'Y':
        points += 2
        if a =='A':
            points += 6
        elif a == 'B':
            points += 3
    elif b == 'Z':
        points += 3
        if a == 'B':
            points += 6
        elif a == 'C':
            points += 3
    return points

points = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break
    points += evaluate(line[0],line[2])

print(points)

file.close()