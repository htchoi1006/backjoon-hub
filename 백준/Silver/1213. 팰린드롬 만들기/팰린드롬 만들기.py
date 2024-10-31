import collections

arr = list(input())
arr.sort()
dic = collections.Counter(arr)


cnt = 0
mid = ''
for i in dic:
    if dic[i] % 2 == 1:
        cnt += 1
        mid = i
        
        
ans = ''
if cnt < 2:
    for i, j in sorted(dic.items()):
        ans += i * (j//2)
        
    print(ans + mid + ans[::-1])
    
else:
    print("I'm Sorry Hansoo")

