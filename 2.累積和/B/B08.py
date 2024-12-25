n = int(input())
s = [[0 for i in range(1506)] for j in range(1506)]
for i in range(n):
    x, y = list(map(int, input().split()))
    s[x][y] += 1

q = int(input())

z = [[0 for i in range(1506)] for j in range(1506)]

# 横方向の累積和
for i in range(1, 1506):
    for j in range(1, 1506):
        z[i][j] = z[i][j-1] + s[i][j]

# 縦方向の累積和
for i in range(1, 1506):
    for j in range(1, 1506):
        z[i][j] = z[i-1][j] + z[i][j]

for _ in range(q):
    a, b, c, d = list(map(int, input().split()))
    print(z[a-1][b-1] + z[c][d] - z[c][b-1] - z[a-1][d])