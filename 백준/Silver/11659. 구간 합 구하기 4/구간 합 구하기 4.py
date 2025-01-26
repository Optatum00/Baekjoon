import sys

N, M = map(int, sys.stdin.readline().strip().split())
num = list(map(int, sys.stdin.readline().strip().split()))

# perfix sum
perfix = []
for i in range(len(num)):
    if (i == 0):
        perfix.append(num[i])
    else:
        perfix.append(num[i]+perfix[i-1])

for i in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    if (i == 1):
        print(perfix[j-1])
    else:
        print(perfix[j-1]-perfix[i-2])