import sys
T = int(sys.stdin.readline().strip())
dp = [0,1,2,4,1,1,1,1,1,1,1,1]
for m in range(4,12):
    dp[m] = dp[m-1] + dp[m-2] + dp[m-3]

for i in range(T):
    n = int(sys.stdin.readline().strip()) # 1 <= n <= 11
    print(dp[n])