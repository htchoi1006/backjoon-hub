n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
length = min(n, m)

def check(length):
    while True:
        for i in range(n-length+1):
            for j in range(m-length+1):
                if arr[i][j] == arr[i+length-1][j] == arr[i][j+length-1] == arr[i+length-1][j+length-1]:
                    return length**2


        else:
            length -= 1
        
print(check(length))