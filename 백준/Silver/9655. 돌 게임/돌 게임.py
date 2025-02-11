n = int(input())
arr = [-1] * (n+10)

arr[1] = 1  #SK
arr[2] = 0  #CY
arr[3] = 1  #SK


for i in range(4, n+1):
    if arr[i-3] == 1 or arr[i-1] == 1:
        arr[i] = 0
    else:
        arr[i] = 1
            
            
if arr[n] == 1:
    print("SK")
else:
    print("CY")
            
