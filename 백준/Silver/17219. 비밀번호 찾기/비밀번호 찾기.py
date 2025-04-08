import sys
input = sys.stdin.readline

site_pw = {}

N, M = map(int, input().strip().split())
for i in range(N):
    x = input().strip().split()
    site_pw[x[0]] = x[1]
for i in range(M):
    print(site_pw[input().strip()])