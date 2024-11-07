import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0] * (n+1)

def dfs(x):
    for i in arr[x]:
        if visited[i] == 0:
            visited[i] = x
            dfs(i)
            
    
dfs(1)
for i in visited[2:]:
    print(i)

