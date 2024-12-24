Test = int(input())
count = 0
sum = 0
for i in range(Test):
    case = input()
    for i in case:
        if (i == 'O'):
            count += 1
        else:
            count = 0
        sum += count
    print(sum)
    count = 0
    sum = 0