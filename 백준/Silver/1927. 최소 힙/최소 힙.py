import sys
import heapq

input = sys.stdin.readline
# 연산 개수
heap = []
N = int(input().strip())
for i in range(N):
    x = int(input().strip())
    if (x == 0):
        # 배열에서 최솟값 출력, 그리고 배열 제거
        try:
            print(heapq.heappop(heap))
        except IndexError:
            print(0)
    else:
        # 배열에 x 추가
        heapq.heappush(heap, x)