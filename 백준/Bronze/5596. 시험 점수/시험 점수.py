kuk = list(map(int, input().split()))
se = list(map(int, input().split()))
if (sum(kuk) > sum(se)):
    print(sum(kuk))
elif (sum(kuk) < sum(se)):
    print(sum(se))
else:
    print(sum(kuk))