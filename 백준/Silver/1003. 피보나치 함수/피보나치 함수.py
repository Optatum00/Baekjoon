import sys
T = int(sys.stdin.readline().strip())
fibo = [[1,0],[0,1]]
for i in range(T):
    n = int(sys.stdin.readline().strip())
    for i in range(n-1):
        fibo.append([fibo[i][0]+fibo[i+1][0], fibo[i][1]+fibo[i+1][1]])
    print(fibo[n][0], fibo[n][1])
    fibo = [[1,0],[0,1]]