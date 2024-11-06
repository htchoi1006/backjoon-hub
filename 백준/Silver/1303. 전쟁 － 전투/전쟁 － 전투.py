from collections import deque

m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

c = [0, 0]
visited = [[0]*m for _ in range(n)]

def check(a, b, color):
    cnt = 0
    queue = deque([(a, b)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
                
    return cnt
    
    
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            num = max(check(i, j, arr[i][j]), 1)
            if arr[i][j] == 'W':
                c[0] += num**2
            else:
                c[1] += num**2
                
print(*c)
                
            