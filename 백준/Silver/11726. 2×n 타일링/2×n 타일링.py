import sys
n = int(sys.stdin.readline().strip())
dp = [0]*1001
dp[1], dp[2] = 1, 2
def tile(n):
    dp[n] = dp[n-1] + dp[n-2]
for i in range(3,n+1):
    tile(i)
print(dp[n]%10007)