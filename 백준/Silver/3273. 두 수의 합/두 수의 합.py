n = int(input())
arr = list(map(int, input().split()))
m = int(input())

ans = 0

arr.sort()

a, b = 0, n-1
while a != b:
    if arr[a] + arr[b] == m:
        ans += 1
        a += 1
    elif arr[a] + arr[b] < m:
        a += 1
    elif arr[a] + arr[b] > m:
        b -= 1

print(ans)