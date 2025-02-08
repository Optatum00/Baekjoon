import sys
# 컴퓨터 수 및 연결된 컴퓨터 쌍의 수 입력받기
com = int(sys.stdin.readline().strip())
edge = int(sys.stdin.readline().strip())
# 그래프 구현 by 인접리스트 (무방향 그래프)
graph = [[] for i in range(com+1)] # 컴퓨터 번호 1번부터 카운트 따라서 리스트도 하나 더 만듬
for i in range(edge):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# 감염된 컴퓨터 수 구하기 (1번에서부터 퍼져나감) by DFS
# DFS 메서드 정의
#그래프 array, 시작 위치, 방문 정보가 들어있는 리스트
res = []
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    res.append(v)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # grqph[i]에 있는 원소가 방문되어 잇지 않다면 재귀함수 호출
            dfs(graph, i, visited)
    return res
visited = [False]*len(graph)
virus = dfs(graph, 1, visited)
print(len(virus)-1)