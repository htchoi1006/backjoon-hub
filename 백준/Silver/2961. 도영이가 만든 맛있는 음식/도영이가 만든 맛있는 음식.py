from itertools import *
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

for i in range(1, n+1):
    for c in combinations(arr, i):
        sour, bitter = 1, 0
        for j in c:
            sour *= j[0]
            bitter += j[1]
            ans = min(ans, abs(sour-bitter))

        
print(ans)
    