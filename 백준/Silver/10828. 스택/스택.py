import sys

N = int(sys.stdin.readline().rstrip())

stack = []

def push(x):
    stack.append(x)

def pop():
    if (len(stack) == 0):
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    if (len(stack) == 0):
        print(1)
    else:
        print(0)

def top():
    if (len(stack) == 0):
        print(-1)
    else:
        print(stack[-1])

for i in range(N):
    command = list(sys.stdin.readline().rstrip().split())
    if (len(command) == 2):
        push(int(command[1]))
        command = []
    else:
        if (command[0] == 'pop'):
            pop()
        elif (command[0] == 'size'):
            size()
        elif (command[0] == 'empty'):
            empty()
        else:
            top()