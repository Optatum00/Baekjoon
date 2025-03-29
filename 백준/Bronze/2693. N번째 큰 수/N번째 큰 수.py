import sys
input = sys.stdin.readline
T = int(input().strip())
for i in range(T):
    num = list(map(int, input().strip().split()))
    num.sort(reverse=True)
    print(num[2])