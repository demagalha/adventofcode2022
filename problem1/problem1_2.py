file = open('input.txt', 'r')

high = []
sum = 0
count = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break

    if line != '\n': 
        sum += int(line)
    print(sum)
    if line == '\n':
        if count < 3:
            high.append(sum)
            min = high[0]
            count += 1
        else:
            min = high[0]
            idx_min = 0
            for i in range(len(high)):
                if high[i] < min:
                    print(min)
                    min = high[i]
                    idx_min = i

            if sum > min:   
                high[idx_min] = sum
        sum = 0

print(high)
sum = 0
for i in range(len(high)):
    sum += high[i]
print(sum)
file.close()