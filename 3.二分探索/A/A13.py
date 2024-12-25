n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [0]
a = b + a
r = [0 for i in range(n+1)]

# しゃくとり法
for i in range(1, n):
    # スタート地点を決める
    if i == 1:
        r[i] = 1
    else:
        r[i] = r[i-1]
    
    while (r[i] < n) and (a[r[i]+1] - a[i] <= k):
        r[i] += 1

answer = 0
for i in range(1, n):
    answer += (r[i] - i)

print(answer)