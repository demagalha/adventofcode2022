file = open('input.txt','r')

def intersection(range1,range2):
    #define if intersection
    if a[1] < b[0] or b[1] < a[0]:
        return -1
    else:
        print('First range')
        print(a)
        print('Second range')
        print(b)
        print('Intersection')
        print([max(a[0],b[0]), min(a[1],b[1])])
        return [max(a[0],b[0]), min(a[1],b[1])]


sum = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break
    line = line.replace('\n','')
    A = line.split(',')
    a = A[0].split('-')
    a = [eval(i) for i in a]
    b = A[1].split('-')
    b = [eval(i) for i in b]
    x = intersection(a,b)
    if x != -1:
        sum +=1
print(sum)
file.close()