file = open('input.txt','r')


class Tree():
    def __init__(self, name='/', size = 'dir', children=None):
        self.name = name
        self.size = size
        self.children = []
        self.parent = None
        if children is not None:
            for child in children:
                self.add_child(child)
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
        for child in self.children:
            child.parent = self
    def idx_name(self, name):
        for i in len(self.children):
            if self.children[i].name == name:
                return i
            return -1


def search(node):
    sum = 0
    visited = []
    stack = []
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node.name)
            #print(node.size)
            if node.size != 'dir':
                sum += int(node.size)
            for adjacent in node.children:
                stack.append(adjacent)
    return sum

def search2(node, required):
    smallest = 70000000
    visited = []
    stack = []
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node.name)
            #print(node.size)
            if node.size == 'dir':
                dummy = search(node)
                if dummy >= required:
                    if smallest > dummy:
                        smallest = dummy
            for adjacent in node.children:
                stack.append(adjacent)
    return smallest

init = Tree()
command = None
depth = 0
current = init
while True:
    line = file.readline()
    if len(line) == 0:
        break
    line = line.replace('\n','')
    line = line.split(' ')
    print(line)
    
    if line[0] != '$':
        if command == 'ls':
            current.add_child(Tree(line[1],line[0]))

    #parse
    if line[0] == '$':
        if line[1] == 'cd':
            command = 'cd'
            if line[2] == '/':
                current = init
            elif line[2] == '..':
                current = current.parent
                continue
            for child in current.children:
                if child.name == line[2]:
                    current = child
                    break
            #do stuff
        elif line[1] == 'ls':
            command = 'ls'
            #do other stuff

print(len(init.children))
print(init.children)
print(init.children[0].name)
print(init.children[0].size)
print(init.children[0].children)
file.close()

#sum = search(init)
#print(sum)

update = 30000000
total = 70000000
used = search(init)
unused = total - used
required = update - unused
print(required)

size_to_delete = search2(init,required)
print(size_to_delete)

'''for node in init.children:
    if node.size != 'dir':
        sum += int(node.name)'''
