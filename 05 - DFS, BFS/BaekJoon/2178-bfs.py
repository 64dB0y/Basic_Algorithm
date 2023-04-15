'''
1. 라이브러리 및 변수 초기화
먼저, collections 모듈에서 deque를 가져와 큐를 구현한다. 그리고 미로의 크기와 내부 구조를 나타내는 이차원 리스트 maze를 입력받는다. 상하좌우 이동을 위해 dx와 dy 리스트를 초기화한다.

2. BFS 수행
시작점(0, 0)에서부터 BFS를 수행한다. 먼저, 시작점을 큐에 추가하고 방문 처리한다. 
큐가 빌 때까지, 현재 위치에서 이동할 수 있는 모든 칸을 큐에 추가하고, 큐에서 하나씩 꺼내며 도착점까지의 최단 거리를 구한다.
방문 여부를 체크하기 위해 visited 집합을 사용한다. 이전 칸에서 현재 칸으로 이동할 때 거리를 1 증가시켜 maze 리스트에 저장한다.

3. 결과 출력
도착점에 도달한 경우, 최단 거리를 출력한다. 이 때, 시작점과 도착점도 포함하여 이동한 칸 수를 출력한다.
'''
from collections import deque

# 미로 크기와 미로 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작점부터 BFS 수행
q = deque([(0, 0)])  # 큐에 시작점 추가
visited = set([(0, 0)])  # 시작점 방문 처리
while q:
    x, y = q.popleft()  # 큐에서 하나씩 꺼내기
    if x == n-1 and y == m-1:  # 도착점에 도달한 경우
        print(maze[x][y])  # 최단 거리 출력(시작점과 도착점 미포함)
        break
    for i in range(4):  # 상하좌우 칸에 대해
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and (nx, ny) not in visited:
            # 이동 가능한 칸이면 큐에 추가하고 방문 처리
            q.append((nx, ny))
            visited.add((nx, ny))
            # 이전 칸에서 현재 칸으로 이동할 때 거리를 1 증가시켜 저장
            maze[nx][ny] = maze[x][y] + 1
