from collections import deque
import sys
n = int(sys.stdin.readline().strip())

if (n == 0):
    print(0)
    sys.exit(0)

opinion = []

for i in range(n):
    level = int(sys.stdin.readline().strip())
    opinion.append(level)

def custom_round(num):
    if ((num - int(num)) >= 0.5):
        return int(num)+1
    else:
        return int(num)
    
def trimmed_mean(n):
    opinion.sort()
    bound = custom_round(n*3/20)

    dq = deque(opinion)

    for i in range(bound):
        dq.pop()
        dq.popleft()

    return list(dq)

final_value = trimmed_mean(n)
count = 0
for i in final_value:
    count += i
res = custom_round(count/len(final_value))
print(res)