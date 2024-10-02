n, k = map(int, input().split())
arr = list(map(int, input().split()))

if max(arr) == 0:
    print('SAD')

else:
    result = [sum(arr[:k])]

    for i in range(n-k):
        result.append(result[i] - arr[i] + arr[i+k])

    print(max(result))
    print(result.count(max(result)))