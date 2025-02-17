import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a*b/gcd(a, b))

T = int(input().strip())
for i in range(T):
    A, B = map(int, input().strip().split())
    print(lcm(A, B))