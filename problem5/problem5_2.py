file = open('input.txt','r')

stacks = []

for i in range(9):
    stacks.append([])

def eval_move(stacks, nel, init, to):
    size = len(stacks[init])
    for i in range(nel):
        stacks[to].append(stacks[init].pop(size-nel))

counter = 0

for k in range(9):
    line = file.readline()
    a = [*line]
    counter = 0
    for i in range(1,len(a),4):
        if ord(a[i]) >= 65 and ord(a[i]) <= 90:
            stacks[counter].append(a[i])
        counter += 1
for i in range(9):
    stacks[i] = list(reversed(stacks[i]))

lines = file.readlines()
for i in range(1,len(lines)):
    moves = lines[i].split()
    eval_move(stacks,int(moves[1]), int(moves[3])-1, int(moves[5])-1)

for i in stacks:
    print(i[-1])
file.close()    