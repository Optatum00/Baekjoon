T = int(input())

inlist = []
outlist =[]

for i in range(T):
    s = input()
    inlist.append(s)

for i in inlist:
    if (len(i) == 1):
        res = i*2
        outlist.append(res)
    else:
        res = i[0]+i[-1]
        outlist.append(res)

for i in outlist:
    print(i)