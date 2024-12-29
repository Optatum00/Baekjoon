import sys

N = int(sys.stdin.readline().rstrip())

def std(n):
    return 3*n**2-3*n+1

count = 1

while True:
    if (std(count) == N):
        print(count)
        break
    elif (std(count) < N < std(count+1)):
        print(count+1)
        break
    count += 1