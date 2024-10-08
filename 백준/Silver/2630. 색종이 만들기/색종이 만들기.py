n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0, 0

def check(row, col, l):
    global blue, white
    
    color = arr[row][col]
    
    for i in range(row, row+l):
        for j in range(col, col+l):
            if color != arr[i][j]:
                check(row, col, l//2)
                check(row, col+l//2, l//2)
                check(row+l//2, col, l//2)
                check(row+l//2, col+l//2, l//2)
                return
            
    if color == 0:
        white += 1
        
    else:
        blue += 1
        
    return


check(0, 0, n)
print(white)
print(blue)
            
            
