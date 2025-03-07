T = int(input())
for i in range(T):
    N = int(input())
    data = {}
    for i in range(N):
        school, alcohol = input().split()
        data[school] = int(alcohol)
    max_key = max(data, key=data.get)
    print(max_key)