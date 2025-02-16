import sys
input = sys.stdin.readline
board = []

M = 0
for i in range(9):
    board.append(list(map(int, input().split())))
    now = max(board[-1])
    if (M < now):
        M = now

for i in range(9):
    if (M in board[i]):
        row = i+1
        col = board[i].index(M)+1

print(M)
print(row, col)