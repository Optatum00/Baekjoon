import sys

T = int(sys.stdin.readline().strip())

def count_resident(k, n):
    resident_num = []
    tmp = []
    x = 0
    resident_num.append([n for n in range(1,n+1)])
    for i in range(k):
        for j in range(n):
            x += resident_num[i][j]
            tmp.append(x)
        resident_num.append(tmp)
        tmp = []
        x = 0
    return resident_num[-1][-1]

res = []

for i in range(T):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    res.append(count_resident(k,n))

for i in res:
    print(i)