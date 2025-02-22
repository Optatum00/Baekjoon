import sys
input = sys.stdin.readline

N = int(input().strip())
fibo = [0,1,1]
if (N == 1):
    print(fibo[N])
elif (N == 2):
    print(fibo[N])
else:
    for i in range(N-2):
        fibo.append(fibo[-1]+fibo[-2])
    print(fibo[N])