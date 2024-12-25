n, k = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))

# 累積和
z = [0 for i in range(n+1)]
z[0] = 0
for i in range(1, n+1):
    z[i] += z[i-1] + a[i]

# しゃくとり法
r = [0 for i in range(n+1)]
for i in range(n):
    # スタート地点を決める
    if i == 0:
        r[i] = -1
    else:
        r[i] = r[i-1]
    
    while (r[i] < n-1) and (z[r[i]+2] - z[i] <= k):
        r[i] += 1

answer = 0
for i in range(n):
    answer += r[i] - i + 1

print(answer)