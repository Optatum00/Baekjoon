from bisect import bisect_left, bisect_right
import sys
# 입력
N = int(sys.stdin.readline().strip())
num_card = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
find_card = list(map(int, sys.stdin.readline().strip().split()))

num_card.sort()

res = []

for i in range(M):
    target = find_card[i]
    # 이분탐색
    res.append(bisect_right(num_card,target)-bisect_left(num_card,target))

for i in res:
    i = str(i)
    print(i+' ', end='')