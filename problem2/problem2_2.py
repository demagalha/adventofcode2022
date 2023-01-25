file = open('input.txt','r')


#very ugly
def evaluate(a,b):
    points = 0
    if b == 'X':
        points += 0
        if a == 'A':
            points += 3
        elif a == 'B':
            points += 1
        elif a == 'C':
            points += 2
    elif b == 'Y':
        points += 3
        if a =='A':
            points += 1
        elif a == 'B':
            points += 2
        elif a == 'C':
            points += 3
    elif b == 'Z':
        points += 6
        if a == 'A':
            points += 2
        elif a == 'B':
            points += 3
        elif a == 'C':
            points+= 1
    return points

points = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break
    points += evaluate(line[0],line[2])

print(points)

file.close()