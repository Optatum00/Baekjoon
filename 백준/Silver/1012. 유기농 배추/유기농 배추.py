import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if (x < 0 or y <0 or x>M-1 or y>N-1):
        return False
    if (graph[y][x] == 1):
        graph[y][x] = 0
        dfs(x-1,y) #좌
        dfs(x,y-1) #하
        dfs(x+1,y) #우
        dfs(x,y+1) #상
        return True
    return False

T = int(input().strip())
for i in range(T):
    result = 0
    M, N, K = map(int, input().strip().split())
    # M x N 리스트 생성
    graph = [[0 for j in range(M)]for i in range(N)]
    for i in range(K):
        x, y = map(int, input().strip().split())
        graph[y][x] = 1
    for i in range(M):
        for j in range(N):
            if (dfs(i,j)):
                result += 1
    print(result)