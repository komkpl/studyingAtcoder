h, w, n = list(map(int, input().split()))

snow = [[0 for i in range(w+2)] for j in range(h+2)]
snow_covered = [[0 for i in range(w+2)] for j in range(h+2)]
for i in range(n):
    a, b, c, d = list(map(int, input().split()))
    snow[a][b] += 1
    snow[a][d+1] -= 1
    snow[c+1][b] -= 1
    snow[c+1][d+1] += 1

# 横方向の累積和
for i in range(1,h+2):
    for j in range(1,w+2):
        snow_covered[i][j] = snow_covered[i][j-1] + snow[i][j]

# 縦方向の累積和
for i in range(1,h+2):
    for j in range(1,w+2):
        snow_covered[i][j] += snow_covered[i-1][j]

# 答えを表示
for i in range(1,h+1):
    for j in range(1, w+1):
        print(f'{snow_covered[i][j]} ',end='')
    print()