N = input().split()
result = 0
for i in range(len(N)):
    result += int(N[i])**2
result %= 10
print(result)