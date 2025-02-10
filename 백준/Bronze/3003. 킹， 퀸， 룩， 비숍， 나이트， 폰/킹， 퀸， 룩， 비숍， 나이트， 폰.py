chess = [1, 1, 2, 2, 2, 8]
own = list(map(int, input().split()))
res = []
for i in range(6):
    res.append(chess[i] - own[i])

for i in res:
    print(i, end=' ')