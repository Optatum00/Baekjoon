import sys
input = sys.stdin.readline

T = int(input().strip())
testcase = list(map(int, input().strip().split()))

lst = [0]*80001
ans = 0

for i in range(80001):
    if (i%3 == 0 or i%7 ==0):
        ans += i
    lst[i] = ans
    
for j in testcase:
    print(lst[j])