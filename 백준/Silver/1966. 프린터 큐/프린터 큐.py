import sys

T = int(sys.stdin.readline().strip())
M_lst, num_lst = [], []
for i in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())  
    num = list(map(int, sys.stdin.readline().strip().split()))
    M_lst.append(M)
    num_lst.append(num)

for i in range(T):
    count = 0
    index = M_lst[i]
    target = num_lst[i][index] # 출력순서 알고 싶은 문서
    while True:
        if (num_lst[i][0] == max(num_lst[i])):
            out = num_lst[i].pop(0)
            count += 1
            if (index == 0 and out == target):
                break
            index -= 1
            if (index == -1):
                index = len(num_lst[i])-1
        else:
            x = num_lst[i].pop(0)
            num_lst[i].append(x)
            index -= 1
            if (index == -1):
                index = len(num_lst[i])-1
    print(count)