n = int(input())
z = [[0 for i in range(1506)] for j in range(1506)]

for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    z[a][b] += 1
    z[a][d] -= 1
    z[c][b] -= 1
    z[c][d] += 1


# 横方向の累積和
for i in range(0,1505):
    for j in range(1,1505):
        z[i][j] = z[i][j-1] + z[i][j]

# 縦方向の累積和
for i in range(1,1505):
    for j in range(0,1506):
        z[i][j] = z[i-1][j] + z[i][j]

# 答えを表示
Answer = 0
for i in range(1506):
    for j in range(1506):
        if z[i][j] >= 1:
            Answer += 1
print(Answer)