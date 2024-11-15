import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tmp = arr[:k]
ans = 0

for i in range(n):
    tmp.pop(0)
    tmp.append(arr[(i+k)%n])
    ans = max(ans, len(set(tmp + [c])))
    
    if ans == d:
        break
        
print(ans)