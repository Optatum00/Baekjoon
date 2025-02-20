import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    max = int(num**0.5)+1
    for i in range(2, max):
        if (num % i == 0):
            return False
    else:
        return True

n = int(input().strip())
for i in range(n):
    M = int(input().strip())
    i = M   
    while (True):
        if (M == 0 or M == 1 or M == 2):
            print(2)
            break
        if isPrime(i):
            print(i)
            break
        i += 1