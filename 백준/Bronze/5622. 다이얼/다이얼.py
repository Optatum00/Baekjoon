s = input()
res = 0

for i in range(len(s)):
    num = ord(s[i])
    if (64<=num<=67):
        res += 3
    elif (68<=num<=70):
        res += 4
    elif (71<=num<=73):
        res += 5
    elif (74<=num<=76):
        res += 6   
    elif (77<=num<=79):
        res += 7
    elif (80<=num<=83):
        res += 8
    elif (84<=num<=86):
        res += 9
    elif (87<=num<=90):
        res += 10

print(res)