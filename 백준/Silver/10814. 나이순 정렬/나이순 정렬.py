import sys

def quick_sort_age(arr):
    if(len(arr) <= 1):
        return arr
    pivot = arr[len(arr)//2][0] #2차원리스트에서 0번째 인덱스인 age기준으로 정렬    
    left, equal, right = [], [], []
    for num in arr:
        if( num[0] < pivot):
            left.append(num)
        elif (pivot < num[0]):
            right.append(num)
        else:
            equal.append(num)
    return quick_sort_age(left) + equal + quick_sort_age(right)

N = int(sys.stdin.readline())
member_sort = []

for i in range(N):
    age, member = sys.stdin.readline().split()
    age = int(age)
    member_sort.append([age, member])
    
member_sort = quick_sort_age(member_sort)

for i in member_sort:
    print(i[0], i[1])