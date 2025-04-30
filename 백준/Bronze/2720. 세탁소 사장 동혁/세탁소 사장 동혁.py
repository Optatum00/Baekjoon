import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    C = int(input().strip())
    if (C//25 != 0):
        Q = C//25
        C = C%25
    else:
        Q = 0
    if (C//10 != 0):
        D = C//10
        C = C%10
    else:
        D = 0
    if (C//5 != 0):
        N = C//5
        C = C%5
    else:
        N = 0
    P = C
    print(Q, D, N, C)