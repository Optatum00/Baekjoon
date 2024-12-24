bowl = input() # ['((((']
lst_bowl = list(bowl)
ans = 10
while len(lst_bowl) > 1:
    if lst_bowl[0] == lst_bowl[1]:
        lst_bowl = lst_bowl[1:]
        ans+=5
    else:
        lst_bowl = lst_bowl[1:]
        ans+=10
print(ans)