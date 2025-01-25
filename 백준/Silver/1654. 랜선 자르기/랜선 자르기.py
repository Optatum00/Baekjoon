import sys

K, N = map(int, sys.stdin.readline().strip().split())

lan = [int(sys.stdin.readline().strip()) for _ in range(K)]

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in lan:
        count += i//mid
    if count >= N:
        start = mid+1
    else:
        end = mid-1
    
print(end)