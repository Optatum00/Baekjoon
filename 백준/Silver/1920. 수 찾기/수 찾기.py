N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

# 재귀 함수로 구현한 이진 탐색
def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    # 원하는 값 찾은 경우 인덱스 반환
    if array[mid] == target:
        return 1
    # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
    else:
        return binary_search(array, target, mid + 1, end)

for i in range(M):
    print(binary_search(N_list, M_list[i], 0, len(N_list)-1))