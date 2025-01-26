import sys

while True:
    stack = []
    N = sys.stdin.readline().rstrip()
    if (N == '.'):
        exit(0)
        
    for j in range(len(N)):
        if(N[j].isalpha()):
            continue
        else:
            if ('(' in N[j]):
                stack.append('(')
            if ('[' in N[j]):
                stack.append('[')
            if (')' in N[j]):
                if (len(stack) == 0):
                    stack.append(0)
                    print('no')
                    break
                if (stack[-1] == '('):
                    stack.pop()
                else:
                    print('no')
                    stack = [0]
                    break
            if (']' in N[j]):
                if (len(stack) == 0):
                    stack.append(0)
                    print('no')
                    break
                if (stack[-1] == '['):
                    stack.pop()
                else:
                    print('no')
                    stack = [0]
                    break
    if (len(stack) == 0):
        print('yes')
    elif ('(' in stack or '[' in stack):
        print('no')