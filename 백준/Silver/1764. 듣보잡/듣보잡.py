import sys
N, M = map(int, sys.stdin.readline().strip().split())
no_listen = [sys.stdin.readline().strip() for i in range(N)]
no_see = [sys.stdin.readline().strip() for i in range(M)]
no_listen.sort()
no_see.sort()

def binary_search(target, data): # 이분탐색
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target: # 가운데 기준 오른쪽 구간으로 이동
            start = mid + 1
        else:                    # 가운데 기준 왼쪽 구간으로 이동
            end = mid -1
    return False # 찾는값 없으면 False

name = []
count = 0
if (N>=M):
    for i in no_see:
        if(binary_search(i, no_listen)):
            name.append(i)
            count += 1
else:
    for i in no_listen:
        if(binary_search(i, no_see)):
            name.append(i)
            count += 1
name.sort()
print(count)
for i in name:
    print(i)