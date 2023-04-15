'''
특정 위치를 하나 지정되었으면 그 주변에도 1이 있는지를 상하좌우를 확인하여 찾아서 count를 늘리고
더이상 주변에 1이 없으면 그 나머지도 찾되 1이 있어도 이미 visited면 무시하고 1인데
visited 리스트에 없으면 관심을 갖고 dfs 정의한데로 돌리면서 count를 늘려라
'''
#!/usr/bin/env python3
# 상하좌우 이동을 위한 dx, dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, cnt):
    # 현재 위치 방문 처리
    visited[x][y] = True
    # 현재 단지의 집 수 1 증가
    cnt += 1
    # 상하좌우 위치에 대해 재귀적으로 dfs 탐색
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # 아예 행렬을 벗어날려고 하면 무시하라
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == '1' and not visited[nx][ny]:
            cnt = dfs(nx, ny, cnt)
    return cnt

# 입력 받기
n = int(input())
graph = [input() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
ans = []

# 모든 위치에 대해 dfs 탐색
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            ans.append(dfs(i, j, 0))

# 단지 수와 각 단지 내 집의 수 출력
print(len(ans))
for cnt in sorted(ans):
    print(cnt)