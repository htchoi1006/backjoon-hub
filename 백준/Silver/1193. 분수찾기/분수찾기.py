n = int(input())

if n == 1:
    print('1/1')
    exit(0)
elif n == 2:
    print('1/2')
    exit(0)
    
cnt = 1
num = n
a, b = 0, 0

for i in range(1, n):
    if i < num:
        num = num - i
        cnt += 1

    else:
        if cnt % 2 == 1:
            a = i - num + 1
            b = num
            print(str(a) + '/' + str(b))
            break
        else:
            a = num
            b = i - num + 1
            print(str(a) + '/' + str(b))
            break