import sys
input = sys.stdin.readline

N = int(input().strip())

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)

num_init_lst = list(map(int, input().strip().split()))
num_set = set(num_init_lst)
num_init = list(num_set)
num_sort = num_init[:]
num_sort.sort()

for i in num_init_lst:
    print(binary_search(num_sort, i, 0, len(num_sort)-1), end=' ')