n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
visited = [0] * (n+1)


def dfs(x):
    visited[x] = 1
    
    for i in arr[x]:
        if visited[i] == 0:
            dfs(i)


dfs(1)
print(visited.count(1) - 1)