from collections import deque
import sys

q = deque()

N = int(sys.stdin.readline().strip())

card_list = [i for i in range(1,N+1)]

q = deque(card_list)

def card(q):
    while (len(q) != 1):
        q.popleft() # 맨 앞 카드 제거
        q.rotate(-1) # 첫카드 저장 및 첫카드 맨뒤로 이동
    return q.pop()

print(card(q))