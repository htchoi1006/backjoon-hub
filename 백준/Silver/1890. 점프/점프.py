n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
visited[0][0] = 1

for i in range(n):
    for j in range(n):
        k = arr[i][j]
        
        if k == 0 or visited[i][j] == 0:
            continue
        if i + k < n:
            visited[i+k][j] += visited[i][j]
        if j + k < n:
            visited[i][j+k] += visited[i][j]
            
            
print(visited[-1][-1])
