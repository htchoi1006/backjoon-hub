from math import factorial

n = int(input())
s = str(factorial(n))[::-1]

for i in s:
    if i != '0':
        print(i)
        break