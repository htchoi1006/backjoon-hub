n = int(input())
arr = list(map(int, input().split()))
limit = int(input())

start, end = 0, max(arr)
ans = 0

while start <= end:
    mid = (start + end)//2
    total = 0

    for i in arr:
        total += min(i, mid)
        
    if total <= limit:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
        
print(ans)