import sys

A, B = map(int, sys.stdin.readline().strip().split())

def GCD(A, B): #최대 공약수
    if (B ==0):
        return A
    return GCD(B, A%B)

def LCM(A, B):
    return int((A*B)/GCD(A, B))

print(GCD(A, B))
print(LCM(A, B))