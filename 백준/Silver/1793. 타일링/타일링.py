import sys
while True:
    try:
        n = int(sys.stdin.readline().strip())
        dp = [0]*1001
        dp[1], dp[2], dp[0] = 1, 3, 1
        def tile(n):
            dp[n] = dp[n-1] + 2*dp[n-2]
        for i in range(3,n+1):
            tile(i)
        print(dp[n])
    except:
        break