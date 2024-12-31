import sys

N = int(sys.stdin.readline().rstrip())

count = 0
target = 665
while True:
    target += 1
    x = str(target)
    if ('666' in x):
        count += 1 
        if (N == count):
            break

print(target)