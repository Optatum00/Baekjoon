N = int(input())
result = []
if N != 1:
    divisor = 2
    while (True):
        if N%divisor == 0:
            N = N//divisor
            result.append(divisor)
        else:
            divisor += 1
        if N == 1:
            break
    if len(result) == 1:
        print(divisor)
    else:
        for i in range(len(result)):
            print(result[i])