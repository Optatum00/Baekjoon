import sys
T = int(sys.stdin.readline().strip())
S = []
    
for i in range(T):
    cmd = sys.stdin.readline().strip()
    if (cmd != "all" and cmd != "empty"):
        cmd, x = cmd.split()[0], int(cmd.split()[1])
        if (cmd == "add"):
            if (x in S):
                continue
            else:
                S.append(x)
        elif (cmd == "remove"):
            if (x in S):
                S.remove(x)
        elif (cmd == "check"):
            if (x in S):
                print(1)
            else:
                print(0)
        else:
            if (x in S):
                S.remove(x)
            else:
                S.append(x)
    else:
        if (cmd == "all"):
            S = [int(i) for i in range(1,21)]
        else:
            S = []