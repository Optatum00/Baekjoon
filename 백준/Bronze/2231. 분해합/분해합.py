import sys

N = int(sys.stdin.readline().strip())

def d_sum(M):
    initial_M = M
    for i in range(len(str(M)),0,-1): 
        x = M//10**(i-1)
        M = M%10**(i-1)
        initial_M += x
    return initial_M

x = 1
while (True):
    if (d_sum(x) == N):
        print(x)
        break
    elif (x >= N):
        print(0)
        break
    else:
        x += 1