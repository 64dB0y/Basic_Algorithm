def dfs(graph, visited, start):
    stack = [start]  # 시작 노드를 스택에 추가
    visited[start] = True  # 시작 노드 방문 처리

    while stack:  # 스택이 빌 때까지 반복
        v = stack.pop()  # 스택에서 하나의 노드를 꺼냄
        for i in range(len(graph[v])):  # 현재 노드와 연결된 노드들을 탐색
            if graph[v][i] and not visited[i]:  # 연결되어 있으며, 방문하지 않은 노드라면
                visited[i] = True  # 방문 처리
                stack.append(i)  # 스택에 추가

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
    if not visited[i]:  # 방문하지 않은 노드가 있으면
        dfs(graph, visited, i)  # 해당 노드를 시작점으로 dfs 탐색 실행
        count += 1  # 탐색이 끝난 후 연결 요소 개수 1 증가

print(count)
