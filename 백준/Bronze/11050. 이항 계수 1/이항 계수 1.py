def fac(x):
    if x <= 1:
        return 1
    else:
        return fac(x-1) * x
    
n, r = map(int, input().split())
c = int(fac(n)/(fac(r)*fac(n-r)))
print(c)