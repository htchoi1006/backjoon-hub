import sys
input = sys.stdin.readline

n = int(input())
shortcut = []


for _ in range(n):
    word = list(map(str, input().split()))
    
    for i in range(len(word)):
        if word[i][0].upper() not in shortcut:
            shortcut.append(word[i][0].upper())
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            print(*word)
            break
            
    else:
        for j in range(len(word)):
            flag = False
            for k in range(len(word[j])):
                if word[j][k].upper() not in shortcut:
                    shortcut.append(word[j][k].upper())
                    flag = True
                    word[j] = word[j][:k] + '[' + word[j][k] + ']' + word[j][k+1:]
                    print(*word)
                    break
                    
            if flag:
                break
                    
        else:
            print(*word)
            