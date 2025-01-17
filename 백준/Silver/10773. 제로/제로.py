import sys

N = int(sys.stdin.readline().strip())
stack = []

for i in range(N):
    put = int(sys.stdin.readline().strip())
    if (put == 0):
        stack.pop()
        continue
    stack.append(put)

print(sum(stack))