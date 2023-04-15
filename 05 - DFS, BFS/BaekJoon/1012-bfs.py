'''
입력 받기, 초기화 진행
bfs 호출시, 최대한 인접해 있는 원소들이 다 visited에 포함되었는지 확인하여 count를 증가한다.
'''
from collections import deque

def bfs(x, y, visited, field):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(field) or ny < 0 or ny >= len(field[0]):
                continue
            if not visited[nx][ny] and field[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and field[i][j] == 1:
                bfs(i, j, visited, field)
                count += 1

    print(count)
