x,y = map(int, input().split())
z = int(input())

if (y+z)>=60:
    quotient = (y+z)//60
    remainder = (y+z)%60
    if x+quotient>=24:
        print(x+quotient-24,remainder)
    else:
        print(x+quotient,remainder)
elif (y+z)<60:
    print(x,y+z)