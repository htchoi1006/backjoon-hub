def find(x):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end)//2
        if arr1[mid] == x:
            return True
        elif arr1[mid] > x:
            end = mid - 1
        elif arr1[mid] < x:
            start = mid + 1
    
    else:
        return False

    
t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    arr1.sort()
    
    for i in arr2:
        if find(i):
            print(1)
        else:
            print(0)
        