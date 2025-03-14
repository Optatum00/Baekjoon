import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque()

def push(x):
    queue.append(x)

def pop():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[0])
        queue.popleft()

def size():
    print(len(queue))

def empty():
    if (len(queue) == 0):
        print(1)
    else:
        print(0)

def front():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[0])
        
def back():
    if (len(queue) == 0):
        print(-1)
    else:
        print(queue[-1])    

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
        elif (command[0] == 'front'):
            front()
        else:
            back()