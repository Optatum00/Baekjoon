import sys

N = int(sys.stdin.readline().rstrip())
num_lst = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    num_lst.append(num)
    
def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(1, length-i):
            if (arr[j-1] > arr[j]):
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp
            else:
                continue
    return arr

num_lst = bubble_sort(num_lst)

for i in num_lst:
    print(i)