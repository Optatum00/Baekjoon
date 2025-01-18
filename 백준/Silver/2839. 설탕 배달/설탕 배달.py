import sys
sugar = int(sys.stdin.readline().strip())

bag = 0
while (sugar >= 0):
    if (sugar%5 == 0):
        bag += sugar//5
        print(bag)
        break
    else:
        sugar -= 3
        bag += 1
else:
    print(-1)