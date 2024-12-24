N = input().upper()
lst = list(N)
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
find_max = []  

for i in range(26):
    count = lst.count(alphabet[i])
    find_max.append(count)

maximum = max(find_max)

if find_max.count(maximum)>1:
    print("?")
else:
    location = find_max.index(maximum)
    print(alphabet[location])