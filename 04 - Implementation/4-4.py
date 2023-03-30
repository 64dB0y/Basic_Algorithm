'''
1. 맵의 세로 크기 n와 가로 크기 m을 입력받습니다.
2. 캐릭터의 위치 (x,y)와 바라보는 방향 direction을 입력받습니다.
3. d 배열은 캐릭터가 방문한 위치를 저장하기 위한 2차원 리스트입니다. 캐릭터의 시작 위치를 1로 설정합니다.
4. 맵의 정보를 입력받아 array에 저장합니다.
5. dx, dy는 캐릭터가 이동할 수 있는 방향을 나타냅니다. 북쪽으로 이동하려면 x좌표에서 -1을 해야하고, 동쪽으로 이동하려면 y좌표에서 +1을 해야합니다.
6. turn_left() 함수는 캐릭터가 왼쪽으로 회전하는 함수입니다. direction 변수를 전역 변수로 선언하여 함수 내에서 사용할 수 있도록 합니다.
7. 캐릭터가 이동한 칸의 수를 저장하는 count와 회전한 횟수를 저장하는 turn_time 변수를 초기화합니다.
8. while문을 통해 캐릭터가 이동할 수 없을 때까지 반복합니다.
9. 왼쪽으로 회전한 후, 앞으로 이동할 위치 (nx, ny)를 계산합니다.
10. 만약 해당 위치에 캐릭터가 가보지 않았고 육지라면, 해당 위치로 이동하고 count와 turn_time을 갱신합니다.
11. 만약 해당 위치에 캐릭터가 가본 곳이거나 바다라면 turn_time을 1 증가시킵니다.
12. 만약 네 방향 모두 갈 수 없다면(turn_time이 4라면), 뒤로 이동합니다.
13. 뒤로 이동할 수 없다면 while문을 종료합니다.
14. 마지막으로 count 값을 출력합니다.
'''
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)