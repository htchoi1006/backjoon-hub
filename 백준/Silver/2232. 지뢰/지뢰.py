import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = [0] + arr
arr.append(0)

ans = []
for i in range(1, n+1):
    if arr[i-1] <= arr[i] >= arr[i+1]:
        ans.append(i)
        
print("\n".join(map(str, ans)))