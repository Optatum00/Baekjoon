import sys

n = int(sys.stdin.readline().rstrip()) # n 입력받음 
stack = []
result = []

def push(x,y):
    for i in range(x,y+1):
        stack.append(i)
        result.append('+')
    
def pop():
    stack.pop()
    result.append('-')

for i in range(n): # 1<=x<=n 사이의 
    if (i == 0):
        init = int(sys.stdin.readline().rstrip())
        previous = init
        push(1, init)
        pop()
    else:
        num = int(sys.stdin.readline().rstrip())
        if (num > previous):
            push(previous+1, num)
            pop()
            previous = num
        elif (num == stack[-1]):
            pop()
        else:
            result.append("NO")
if("NO" in result):
    print("NO")
else:
    for i in result:
        print(i)