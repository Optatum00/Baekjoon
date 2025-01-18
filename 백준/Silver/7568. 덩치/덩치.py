import sys
N = int(sys.stdin.readline().strip())

info = []

res = [1]*N

def compare(a,b):
    if (info[a][0] < info[b][0] and info[a][1] < info[b][1]):
        res[a] += 1

for i in range(N):
    x = list(map(int, sys.stdin.readline().strip().split()))
    info.append(x)
    
    
for i in range(N):
    for j in range(N):
         compare(i,j)

for i in res:
    print(str(i)+' ', end='')