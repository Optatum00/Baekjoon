import sys
N = int(sys.stdin.readline().strip())
time = list(map(int, sys.stdin.readline().strip().split()))

def min_time(lst):
    lst.sort()
    time_sum = []
    for i in range(1,len(lst)+1):
        tmp = 0
        for j in range(i):
            tmp += lst[j]
        time_sum.append(tmp)
    return sum(time_sum)

print(min_time(time))