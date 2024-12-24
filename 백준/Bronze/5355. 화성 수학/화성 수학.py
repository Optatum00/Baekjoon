T = int(input())
lst_ans = []
for i in range(T):
    N = input()
    N = N.split()
    result = float(N[0])
    for i in range(1,len(N)):
        if N[i] == '@':
            result *= 3
        elif N[i] == '%':
            result += 5
        elif N[i] == '#':
            result -= 7
    result = str(result)
    save = result.split('.')
    if len(save[1]) > 2:
        result = round(float(result), 2)
        result = str(result)
        save = result.split('.')
        if len(save[1]) == 1:
            result = result+'0'
    elif save[1] == '0':
        result = result+'0'
    lst_ans.append(result)

for i in range(T):
    print(lst_ans[i])