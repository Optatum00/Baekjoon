A, B = input().split()
A = int(A)
B = int(B)
lst = [0,2,5]
test = (A, B)

A_win = [(0,2),(5,0),(2,5)]
B_win = [(2,0),(0,5),(5,2)]
if A in lst and B in lst:
    if test in A_win:
        print(">")
    elif A == B:
        print("=")
    elif test in B_win:
        print("<")
elif A not in lst and B not in lst:
    print("=")
elif A not in lst and B in lst:
    print("<")
elif A in lst and B not in lst:
    print(">")