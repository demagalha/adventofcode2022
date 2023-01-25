file = open('input.txt','r')

def priority(str):
    str_size = len(str)-1 #'\n'
    c_size = int(str_size/2)
    str_first = str[0:c_size]
    str_second = str[c_size:str_size]
    equal_c = None
    for i in range(c_size):
        for j in range(c_size):
            if str_first[i] == str_second[j]:
                equal_c = str_first[i]
                break
            if equal_c != None:
                break
    if equal_c.islower():
        return ord(equal_c)-ord('a')+1
    else:
        return ord(equal_c)-ord('A')+27      

sum = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break
    sum += priority(line)

print(sum)
file.close()