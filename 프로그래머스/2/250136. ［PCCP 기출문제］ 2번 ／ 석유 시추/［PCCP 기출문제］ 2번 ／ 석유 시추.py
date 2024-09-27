from collections import deque

def solution(arr):
    def bfs(a, b):
        cnt = 0
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        
        queue = deque([(a, b)])
        min_y, max_y = b, b
        visited[a][b] = 1
        
        while queue:
            x, y = queue.popleft()
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            cnt += 1
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    
        for i in range(min_y, max_y+1):
            result[i] += cnt
                    
                

        
    n = len(arr)
    m = len(arr[0])
    visited = [[0]*m for _ in range(n)]
    ans = []
    result = [0 for _ in range(m+1)]
    
    for i in range(m):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1 and visited[j][i] == 0:
                bfs(j, i)
        
        
    return max(result)

    
    
# [0, 0, 0, 1, 1, 1, 0, 0]
# [0, 0, 0, 0, 1, 1, 0, 0]
# [1, 1, 0, 0, 0, 1, 1, 0]
# [1, 1, 1, 0, 0, 0, 0, 0]
# [1, 1, 1, 0, 0, 0, 1, 1]





