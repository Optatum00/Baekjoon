x,y,z = map(int, input().split())

if (x==y==z):
    prize1 = 10000+x*1000
    print(prize1)
elif(x==y):
    prize2 = 1000+x*100
    print(prize2)
elif(x==z):
    prize2 = 1000+x*100
    print(prize2)
elif(z==y):
    prize2 = 1000+y*100
    print(prize2)
elif(x!=y and x!=z and y!=z):
    prize3 = max(x,y,z)*100
    print(prize3)