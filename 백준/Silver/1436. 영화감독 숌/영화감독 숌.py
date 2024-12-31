import sys

N = int(sys.stdin.readline().rstrip())

count = 0
target = '666'
while True:
    if ('666' in target  ):
        count += 1 
    if (N == count):
        break
    target = int(target)
    target += 1
    target = str(target)
print(target)