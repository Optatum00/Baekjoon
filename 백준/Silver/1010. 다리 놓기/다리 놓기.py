import sys
input = sys.stdin.readline

def comb(n,r):
    pascal = [[1 for i in range(r+1)]]
    for i in range(n-r):
        pascal.append([1])
    for i in range(1,n-r+1):
        for j in range(1,r+1):
            pascal[i].append(pascal[i][-1]+pascal[i-1][j])
    return pascal[-1][-1]

T = int(input().strip())
for i in range(T):
    r, n = map(int, input().strip().split())
    print(comb(n,r))