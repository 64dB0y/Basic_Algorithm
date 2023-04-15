'''
visited[v] = True 는 visited 리스트에서 해당 노드를 방문했다고 체크해야 한다(재방문 방지 <-> 무한 루프 방지)
'''
from collections import deque

# DFS 함수 정의
def dfs(v):
    visited[v] = True # v를 방문했다고 체크
    print(v, end=' ') # v를 출력
    for i in range(1, n+1): # 1부터 n까지 인접한 노드들에 대해
        if not visited[i] and graph[v][i]: # 방문하지 않았고, 연결되어 있다면
            dfs(i) # 해당 노드로 이동하여 dfs 수행

# BFS 함수 정의
def bfs(v):
    q = deque([v]) # 시작 노드를 큐에 삽입
    visited[v] = True # 시작 노드를 방문했다고 체크
    while q: # 큐가 빌 때까지 반복
        now = q.popleft() # 큐에서 노드 하나를 꺼내옴
        print(now, end=' ') # 노드를 출력
        for i in range(1, n+1): # 1부터 n까지 인접한 노드들에 대해
            if not visited[i] and graph[now][i]: # 방문하지 않았고, 연결되어 있다면
                q.append(i) # 큐에 삽입
                visited[i] = True # 방문했다고 체크

# 입력값 받기
n, m, v = map(int, input().split())
graph = [[False] * (n+1) for _ in range(n+1)] # 인접행렬 초기화

# 간선 정보 입력받기
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = True # 양방향 연결

visited = [False] * (n+1) # 방문 여부 초기화
dfs(v) # DFS 수행

print() # 줄바꿈

visited = [False] * (n+1) # 방문 여부 초기화
bfs(v) # BFS 수행
