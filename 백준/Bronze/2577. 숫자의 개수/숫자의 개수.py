A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)

lst = [0 for i in range(10)]

for i in result:
    lst[int(i)] += 1
    
for i in lst:
    print(i)