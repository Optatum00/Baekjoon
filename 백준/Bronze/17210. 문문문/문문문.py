N = int(input())
door = int(input())
door_lst = [0,1,0,1]
door_lst2 = [1,0,1,0]

if N <= 5:
    if door == 1:
        for i in range(N-1):
            print(door_lst[i])
    else:
        for i in range(N-1):
            print(door_lst2[i])
else:
    print("Love is open door")