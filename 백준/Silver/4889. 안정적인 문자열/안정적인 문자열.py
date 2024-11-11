cnt = 1
while True:
    arr = list(input())
    stack = []
    ans = 0
    
    if '-' in arr:
        break
    
    if len(arr) == 0:
        print(f'{cnt}. {ans}')
        cnt += 1
        
    else:
        for i in arr:
            if i == '{':
                stack.append(i)
            else:
                if stack: 
                    if stack[-1] == '{':
                        stack.pop()
                else:
                    ans += 1
                    stack.append('{')
                
    if stack:
        ans += max(1, len(stack)//2)
        
    print(f'{cnt}. {ans}')
    cnt += 1
        
