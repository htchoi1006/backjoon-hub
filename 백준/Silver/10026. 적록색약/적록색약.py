from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

def bfs(a, b, visited):
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == arr[x][y]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                


def check():
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j, visited)
                cnt += 1
    ans.append(cnt)

check()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'
            
check()
print(*ans)

    

