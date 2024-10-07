n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    

visited = [0] * (n+1)
ans = 0

def dfs(num, cnt):
    global ans
    cnt += 1
    visited[num] = 1
    
    if num == b:
        ans = cnt
    
    for i in arr[num]:
        if visited[i] == 0:
            dfs(i, cnt)

dfs(a, 0)

print(-1) if ans == 0 else print(ans-1)



