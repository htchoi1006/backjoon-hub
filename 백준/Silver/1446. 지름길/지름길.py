n, goal = map(int, input().split())
dp = [i for i in range(goal+1)]
arr = []

for _ in range(n):
    start, end, distance = map(int, input().split())
    if end - start > distance:
        arr.append((start, end, distance))
        
arr.sort()

for start, end, distance in arr:
    for i in range(1, goal+1):
        if i == end:
            dp[i] = min(dp[i], dp[start] + distance)
        else:
            dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[goal])