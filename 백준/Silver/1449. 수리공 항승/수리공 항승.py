n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
idx1 = 0
idx2 = 1

while idx2 != n:
    if arr[idx2] - arr[idx1] < l:
        idx2 += 1
    else:
        ans += 1
        idx1 = idx2
        idx2 += 1
        
ans += 1
        
print(ans)
        
