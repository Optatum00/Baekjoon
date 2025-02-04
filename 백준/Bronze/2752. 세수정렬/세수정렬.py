import sys
num = list(map(int, sys.stdin.readline().strip().split()))
num.sort()
print(num[0],num[1],num[2])