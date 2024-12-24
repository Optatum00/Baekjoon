def fac(x):
    if x <= 1:
        return x
    else:
        return fac(x-1) * x

N = int(input())
result = str(fac(N))
length = len(result)
count = 0

for i in range(length-1,1,-1):
    if (result[i] == '0'):
        count += 1
    else:
        break

print(count)