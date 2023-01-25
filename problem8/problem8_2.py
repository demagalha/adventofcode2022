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
def distance(h, arr):
    dist = 1
    for i in range(arr.shape[0]-1,-1,-1):
        if h <= arr[i]:
            return dist
        elif i == 0:
            return dist
        else:
            dist +=1
    return dist


#matrix = np.array(([3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]))
#just to check

highest = -1
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if i == 0 or i == matrix.shape[0]-1 or j == 0 or j == matrix.shape[1]-1:
            continue
        #first let's check if it's visible to the left
        dummy = matrix[i,0:j]
        left = distance(matrix[i,j], dummy)
        #check to the right
        dummy = matrix[i,j+1:matrix.shape[1]]
        right = distance(matrix[i,j], np.flip(dummy))
        #check up
        dummy= matrix[0:i, j]
        up = distance(matrix[i,j], dummy)
        #check down
        dummy = matrix[i+1:matrix.shape[0],j]
        down = distance(matrix[i,j], np.flip(dummy))
        scenic_score = left*right*up*down
        #print(scenic_score)
        if scenic_score > highest:
            highest = scenic_score


print(highest)