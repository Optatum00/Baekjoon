import sys

N = int(sys.stdin.readline().strip())

coordinate = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    coordinate.append([x,y])

# sorted는 parameter로 넘겨준 리스트의 요소들을 가져와 
# 새로운 리스트를 만들고 정렬한 후 새로 만든 리스트를 반환합니다.
# 따라서 따로 저장 받아줘야함. key로 정렬 기준 설정 밑은 y요소 오름차순 후 x요소 오름차순
coordinate = sorted(coordinate, key = lambda x: (x[1], x[0]))

for i in coordinate:
    print(i[0], i[1])