import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    n = int(input().strip())
    fashion = {}
    type_lst = []
    res = 1
    for i in range(n):
        name, type = input().strip().split()
        if (i != 0):
            if (type not in type_lst):
                fashion[type] = [name]
                type_lst.append(type)
            else:
                fashion[type].append(name)
                type_lst.append(type)
        else:
            fashion[type] = [name]
            type_lst.append(type)
    for key in fashion.keys():
        res *= ((len(fashion[key]))+1)
    print(res-1)