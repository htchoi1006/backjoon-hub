n = int(input())
arr = [[] for _ in range(n+1)]
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
visited = [0] * (n+1)

def dfs(x, cnt):
    if cnt == 2:
        return
    for i in arr[x]:
        if visited[i] == 0:
            visited[i] = 1
        dfs(i, cnt+1)
            
    

dfs(1, 0)
        
        
print(max(sum(visited)-1, 0))

