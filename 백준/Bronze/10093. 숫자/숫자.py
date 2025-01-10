a, b = map(int, input().split())
if(a==b):
    print(0)
    exit()
elif(a<b):
    print(b-a-1)
    for i in range(1, b-a):
        print(a+i, end = ' ', sep ='')
else:
    a, b = b, a
    print(b-a-1)
    for i in range(1, b-a):
        print(a+i, end = ' ', sep ='')