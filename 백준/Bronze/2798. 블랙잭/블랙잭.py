import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0
end  = len(num)

for i in range(end):
    for j in range(i+1,end):
        for k in range(j+1, end):
            sum = num[i] + num[j] +num[k]
            if (M > sum > result):
                result = sum
            elif (M == sum):
                result = sum
                break
print(result)