S = int(input())
cnt = 1

def sigma(n):
    return n*(n+1)//2

if S == 1:
    print("1")
    exit()

while (True):
    if S < sigma(cnt):
        break
    cnt += 1

print(cnt-1)