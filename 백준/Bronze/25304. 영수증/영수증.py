price = int(input())
count = int(input())
total = 0

for i in range(count):
    product, p_count = map(int, input().split())
    total += product * p_count

if total == price:
    print("Yes")
else:
    print("No")