file = open('input.txt','r')

def priority(char):
    if char.islower():
        return ord(char)-ord('a')+1
    else:
        return ord(char)-ord('A')+27      

sum = 0
group = []
equal_c = None
b1 = 0
b2 = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break
    group.append(line)
    print(group)
    if len(group) == 3:
        for i in range(len(group[0])):
            if b1:
                break
            for j in range(len(group[1])):
                if b2: break
                if group[0][i] == group[1][j]:
                    for k in range(len(group[2])):
                        if group[0][i] == group[2][k]:
                            equal_c = group[0][i]
                            print(equal_c)
                            b2 = 1
                            b1 = 1
                            break
        sum += priority(equal_c)
        b1 = 0
        b2 = 0
        group = []

print(sum)
file.close()