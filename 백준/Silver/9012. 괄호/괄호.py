import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    PS = sys.stdin.readline().rstrip()
    stack = []
    
    for i in range(len(PS)):
        if (PS[i] == '('):
            stack.append(PS[i])
        elif (PS[i] == ')'):
            if (len(stack) == 0):
                stack.append(PS[i])
                break
            else:
                stack.pop()
        
    if(len(stack) != 0):
        print("NO")
    else:
        print("YES")