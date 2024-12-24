T = int(input())
ans = []
for i in range(T):
    result = ''
    R, S = input().split()
    lst = list(S)
    for i in range(len(S)):
        result += lst[i]*int(R)
    ans.append(result)
for i in range(T):
    print(ans[i])