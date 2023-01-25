import numpy as np

file = open('input.txt','r')


count = 0
while True:
    line = file.readline()
    if len(line) == 0:
        break
    line = line.replace('\n','')
    a = [int(i) for i in line]
    b = np.array(a)
    if count == 0:
        matrix = b
        count += 1
        continue
    matrix = np.vstack((matrix,b))

file.close()
visible = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i == 0 or i == matrix.shape[0]-1 or j == 0 or j == matrix.shape[1]-1:
            visible += 1
            continue
        #first let's check if it's visible to the left
        if not any(matrix[i,j] <= matrix[i,0:j]):
            visible += 1
            continue
        #check to the right
        elif not any(matrix[i,j] <= matrix[i,j+1:matrix.shape[1]]):
            visible += 1
            continue
        #check up
        elif not any(matrix[i,j] <= matrix[0:i, j]):
            visible += 1
            continue
        #check down
        elif not any(matrix[i,j] <= matrix[i+1:matrix.shape[0],j]):
            visible += 1


print(visible)