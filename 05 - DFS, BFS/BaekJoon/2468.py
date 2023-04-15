#!/usr/bin/env python3
# 상하좌우 이동을 위한 dx, dy
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 해제
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
        if graph[nx][ny] <= current_num and not visited[nx][ny]:
            cnt = dfs(nx, ny, cnt)
    return cnt


# 입력 받기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

range_num = set(range(1, 101))
visited = [[False] * n for _ in range(n)]
ans = []
# 초기화
result = [0] * len(range_num)

# 모든 위치에 대해 dfs 탐색
for k in range(len(range_num)):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                current_num = k
                ans.append(dfs(i, j, 0))
    result.append(len(ans))

print(max(result))
