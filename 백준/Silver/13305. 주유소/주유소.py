n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

# n = 4
# distance, price = [2, 3, 1], [5, 2, 4, 1]
min_price = price[0]
total = 0

for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]

    total += min_price * distance[i]
    
print(total)
    