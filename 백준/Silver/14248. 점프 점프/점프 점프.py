n = int(input())
arr = list(map(int, input().split()))
m = int(input())

visited = [0] * n
visited[m-1] = 1


def jump(x):
    if x + arr[x] < n:
        visited[x+arr[x]] = 1
        jump(x+arr[x])
        
    if x - arr[x] >= 0:
        visited[x - arr[x]] = 1
        jump(x - arr[x])
        
    
    
jump(m-1)
print(sum(visited))