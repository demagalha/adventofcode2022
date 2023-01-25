file = open('input.txt', 'r')

high = -1
sum = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break

    if line != '\n': 
        sum += int(line)

    if line == '\n':
        if high < sum:
            high = sum
            print(sum)
        sum = 0

print(high)
file.close()