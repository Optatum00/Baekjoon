import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = []

for i in range(N):
    line = sys.stdin.readline().strip()
    board.append(line)

def get_min(board):
    test1, test2 = "WBWBWBWB", "BWBWBWBW"
    res = min(check(board,test1,test2), check(board,test2,test1))
    return res

def check(board,first_test,second_test):
    count = 0
    for i in range(0,8,2):
        for j in range(8):
            if (board[i][j] == first_test[j]):
                continue
            
            else:
                count += 1
    for i in range(1,8,2):
        for j in range(8):
            if (board[i][j] == second_test[j]):
                continue
            
            else:
                count += 1
    return count

def slice_board(board):
    initial_board = board
    sliced_board = []
    res = 100
    width_case = M-8+1
    length_case = N-8+1
    for i in range(width_case):
        for j in range(length_case):
            # 위아래로 8개 맞추기
            updown_board = initial_board[j:8+j]
            # 양옆으로 8개 맞추기
            for k in range(8):
                sliced_board.append(updown_board[k][i:8+i])
            # 케이스별로 오류갯수 찾고 갱신
            error = get_min(sliced_board)
            if (res > error):
                res = error
            sliced_board = []
    return res

print(slice_board(board))