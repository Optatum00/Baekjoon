S = input()
a, b = len(S)//10, len(S)%10
for i in range(a):
    print(S[10*i:10*(i+1)])
print(S[10*a:10*a+b])