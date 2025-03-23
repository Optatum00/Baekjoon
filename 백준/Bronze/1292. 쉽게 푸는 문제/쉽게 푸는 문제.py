import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())

sequence = [0]
while (True):
    for i in range(1, 46):
        if (len(sequence) > 1001):
            break
        for j in range(i):
            sequence.append(i)
    break

sum = 0
for i in range(A,B+1):
    sum += sequence[i]
print(sum)