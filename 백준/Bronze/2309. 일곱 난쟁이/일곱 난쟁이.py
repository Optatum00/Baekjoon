from itertools import *
import sys
input = sys.stdin.readline

dataset = [0,1,2,3,4,5,6,7,8]

printList = list(combinations(dataset, 2))

height = []
for i in range(9):
    height.append(int(input().strip()))

for i in printList:
    first, second = i
    x = height[first]
    y = height[second]
    height.remove(x)
    height.remove(y)
    if (sum(height) == 100):
        break
    else:
        height.insert(first,x)
        height.insert(second,y)

height.sort()
for i in height:
    print(i)