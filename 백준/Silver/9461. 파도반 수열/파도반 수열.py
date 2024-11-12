t = int(input())
for _ in range(t):
    arr = [0] * 101
    arr[:5] = [1, 1, 1, 2, 2]
    
    n = int(input())
    if n <= 5:
        print(arr[n-1])

    else:
        idx = 0
        for i in range(6, n+2):
            arr[i-1] = arr[idx] + arr[idx+4]
            idx += 1
            
        print(arr[n-1])
        
        
