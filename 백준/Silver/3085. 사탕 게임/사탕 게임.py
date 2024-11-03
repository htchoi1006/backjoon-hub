from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

def check(arr):
    maxnum = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
            else:
                cnt = 1
                
            maxnum = max(maxnum, cnt)
        
        cnt = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
            else:
                cnt = 1
                
            maxnum = max(maxnum, cnt)
            
    return maxnum
    
        

ans = 0
for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            ans = max(check(arr), ans)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            
        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            ans = max(check(arr), ans)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            
print(ans)
                