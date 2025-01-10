A, B = input().split()

def reverse(n):
    rep = len(n)
    tmp = ''
    for i in range(rep-1,-1,-1):
        tmp += n[i]
    res = int(tmp)
    return res

if (reverse(A) > reverse(B)):
    print(reverse(A))
else:
    print(reverse(B))