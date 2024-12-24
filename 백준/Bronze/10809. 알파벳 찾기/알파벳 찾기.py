S = input()
lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = []
step = 0
for i in lst:
    for j in S:
        if (i == j):
            ans.append(step)
            break
        else:
            step += 1
    if (step == len(S)):
        ans.append(-1)
    step = 0
for n in ans:
    print(n, end=" ")
