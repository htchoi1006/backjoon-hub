from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

rain = 0
maxnum = max(map(max, arr))
check = [[0]*n for _ in range(n)]
ans = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def flood(rain):
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= rain and check[i][j] == 0:
                check[i][j] = 1
                
                
def bfs(a, b):
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
        
    



while rain <= maxnum:
    visited = [[0]*n for _ in range(n)]
    flood(rain)
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1
                
            
    ans = max(ans, cnt)
    rain += 1
    
print(ans)
            
            
            