h, w = list(map(int, input().split()))
x = [[0 for i in range(1,w+2)]for j in range(1,h+2)]
input_num = [0 for i in range(w)]
for i in range(1,h+1):
    input_num = list(map(int, input().split()))
    for j in range(1, w+1):
        x[i][j] = input_num[j-1]

q = int(input())

Z = [[0 for i in range(w+2)]for j in range(h+2)]

# 横方向に累積和を取る
for i in range(1,h+1):
    for j in range(1,w+1):
        Z[i][j] = Z[i][j-1] + x[i][j]

# 縦方向に累積和を取る
for i in range(1,w+1):
    for j in range(1, h+1):
        Z[j][i] = Z[j-1][i] + Z[j][i]

for _ in range(q):
    A, B, C, D = list(map(int, input().split()))
    print(Z[A-1][B-1] + Z[C][D] - Z[C][B-1] - Z[A-1][D])