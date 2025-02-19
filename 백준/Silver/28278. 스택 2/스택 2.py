import sys
input = sys.stdin.readline
N = int(input())
stack = []

def stack1(x):
    stack.append(x)

def stack2():
    if (len(stack) == 0):
        return -1
    else:
        x = stack.pop()
        return x

def stack3():
    return len(stack)

def stack4():
    if (len(stack) == 0):
        return 1
    else:
        return 0

def stack5():
    if (len(stack) == 0):
        return -1
    else:
        return stack[-1]     

for i in range(N):
    # 입력을 한개 만 받아도 오류 x, 리스트로 저장됨
    cmd = input().strip().split()
    if (len(cmd) != 1):
        cmd[-1] = int(cmd[-1])
        stack1(cmd[1])
    else:
        cmd[-1] = int(cmd[-1])
        if cmd[0] == 2:
            print(stack2())
        elif cmd[0] == 3:
            print(stack3())
        elif cmd[0] == 4:
            print(stack4())
        else:
            print(stack5())