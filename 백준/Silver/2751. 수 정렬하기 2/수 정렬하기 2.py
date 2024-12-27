import sys

N = int(sys.stdin.readline().rstrip())

plus = [0] * 1000001
minus = [0] * 1000001

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    if (num >= 0):
        plus[num] += 1
    else:
        minus[num*-1] += 1
    
for i in range(1000000, -1, -1):
    if(minus[i] != 0):
        for j in range(minus[i]):
            print(i*-1)
            
for i in range(len(plus)):            
    if(plus[i] != 0):
        for j in range(plus[i]):
            print(i)