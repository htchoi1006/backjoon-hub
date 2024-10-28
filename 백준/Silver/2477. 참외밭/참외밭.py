n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]

row, col = 0, 0
idx_row, idx_col = 0, 0

for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2: 
        if arr[i][1] > row:
            row = arr[i][1]
            idx_row = i
        
    elif arr[i][0] == 3 or arr[i][0] == 4: 
        if arr[i][1] > col:
            col = arr[i][1]
            idx_col = i


small_row = abs(arr[(idx_col+1)%6][1] - arr[(idx_col-1)%6][1])
small_col = abs(arr[(idx_row+1)%6][1] - arr[(idx_row-1)%6][1])

print((row * col - small_row * small_col) * n)