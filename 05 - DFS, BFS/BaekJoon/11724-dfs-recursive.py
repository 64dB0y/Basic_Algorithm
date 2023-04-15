'''
그래프의 크기가 최대 1000 * 1000이 될 수 있기 때문에 재귀 깊이 제한을 해제
'''
import sys
sys.setrecursionlimit(1000000)  # 재귀 깊이 제한을 해제

def dfs(graph, visited, v):
    visited[v] = True  # 현재 노드 방문 처리
    for i in range(len(graph[v])):
        if graph[v][i] and not visited[i]:
            dfs(graph, visited, i)

n, m = map(int, input().split())

# n x n 크기의 2차원 리스트 graph를 생성하고 0으로 초기화
graph = [[0] * n for _ in range(n)]

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1

# 방문 정보를 저장할 리스트 초기화
visited = [False] * n

count = 0  # 연결 요소의 개수

# 모든 노드에 대해 dfs 탐색
for i in range(n):
    if not visited[i]:
        dfs(graph, visited, i)
        count += 1

print(count)
