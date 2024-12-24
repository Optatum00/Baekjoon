T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    floor = str(N%H)
    number = str((N//H)+1)
    if (N%H == 0):
        number = str(N//H)
        floor = str(H)
    if (len(number) == 1):
        number = '0'+number
    print(str(floor) + str(number))