from collections import deque

n = int(input())
tmp = list(map(int, input().split()))
arr = []


for i, j in enumerate(tmp):
    arr.append((i, j))
queue = deque(arr)


ans = []
while queue:
    a = queue[0]
    if a[1] > 0:
        queue.popleft()
        ans.append(a[0]+1)
        for i in range(a[1]-1):
            queue.rotate(-1)
    else:
        queue.popleft()
        ans.append(a[0]+1)
        for i in range(abs(a[1])):
            queue.rotate(1)

            
print(*ans)
        
        