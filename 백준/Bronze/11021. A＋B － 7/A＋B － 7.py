T = int(input())
lst = []

for i in range(T):
    A, B = map(int, input().split())
    lst.append(A+B)

for i in range(0,T):
    print(f'Case #{i+1}: {lst[i]}')