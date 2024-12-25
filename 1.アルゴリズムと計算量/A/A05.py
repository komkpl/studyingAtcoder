n, k = list(map(int, input().split()))
ways = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if (k - i - j) >= 1 and (k - i - j) <= n:
            ways += 1

print(ways)