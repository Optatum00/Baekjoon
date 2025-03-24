import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())
std = []
cnt = 0
for i in range(N):
    std.append(int(input().strip()))

while (K != 0):
    min = 99999999999
    for i in range(N):
        quo = K//std[i]
        if (quo == 0):
            break
        if (min > quo):
            min = quo
            div = std[i]
    cnt += min
    K -= div*min

print(cnt)