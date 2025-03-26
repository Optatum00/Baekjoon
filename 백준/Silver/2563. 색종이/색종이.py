import sys
input = sys.stdin.readline

paper = [[0 for i in range(100)] for i in range(100)]

N = int(input().strip())
for i in range(N):
    x, y = map(int, input().strip().split())
    for i in range(100-y,90-y,-1):
        for j in range(x-1,x+9):
            paper[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if (paper[i][j] != 0):
            cnt += 1
print(cnt)  