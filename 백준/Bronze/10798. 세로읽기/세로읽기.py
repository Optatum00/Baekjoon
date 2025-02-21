import sys
input = sys.stdin.readline

S = [[] for i in range(15)]

for i in range(5):
    sen = input().strip()
    idx = 0
    for i in sen:
        S[idx].append(i)
        idx += 1

for i in S:
    if (i == []):
        break
    for j in i:
        print(j,end='')