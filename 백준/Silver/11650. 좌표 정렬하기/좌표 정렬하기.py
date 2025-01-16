import sys

N = int(sys.stdin.readline().strip())

coordinate = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    coordinate.append([x,y])

coordinate.sort()

for i in coordinate:
    print(i[0], i[1])