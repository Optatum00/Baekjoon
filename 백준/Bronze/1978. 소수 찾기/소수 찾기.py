N = int(input())
num = list(map(int, input().split()))

count = 2
res = 0
for i in num:
    if (i == 1):
        continue
    while (True):
        if (i > count):
            if (i%count == 0):
                count = 2
                break
            else:
                count += 1
        else:
            res += 1
            count = 2
            break
print(res)