file = open('input.txt','r')

line = file.readline()
#line = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg='

counter_g = 0


def repeated(str):
    for i in range(len(str)):
        if str.count(str[i]) > 1:
            return 1
    return 0

for i in range(len(line)):
    dummy = line[i:i+14]
    if not repeated(dummy):
        counter_g = i + 14
        break

print(counter_g)

file.close()