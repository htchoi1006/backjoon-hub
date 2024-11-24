from collections import deque
import sys

t = int(input())
for _ in range(t):

    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def check(a, b):
        queue = deque([(a, b)])
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '#' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#' and visited[i][j] == 0:
                visited[i][j] = 1
                check(i, j)
                ans += 1

    print(ans)
            
