T = int(input())
lst = []
a = []
b = []

for i in range(T):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)
    lst.append(A+B)

for i in range(0,T):
    print(f'Case #{i+1}: {a[i]} + {b[i]} = {lst[i]}')    
