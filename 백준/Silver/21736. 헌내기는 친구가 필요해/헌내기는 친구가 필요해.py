from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 0

queue = deque()
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            queue.append((i, j))
            

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 'X':
            visited[nx][ny] = 1
            queue.append((nx, ny))
            if arr[nx][ny] == 'P':
                cnt += 1


print(cnt) if cnt else print('TT')