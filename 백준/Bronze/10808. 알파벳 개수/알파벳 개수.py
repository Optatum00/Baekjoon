S = input()
aList = [0 for i in range(26)]
for i in S:
    aList[ord(i)-97] += 1
for i in aList:
    print(i, end=' ')