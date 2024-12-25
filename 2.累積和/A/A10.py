n = int(input())
a = [0 for i in range(1, n+2)]
A = list(map(int, input().split()))
for i in range(1, n+1):
    a[i] = A[i-1]


d = int(input())
p = [0 for i in range(100009)]
q = [0 for i in range(100009)]
l = [0 for i in range(d+1)]
r = [0 for i in range(d+1)]

for i in range(1, d+1):
    l[i], r[i] = map(int, input().split())

# 左からの累積maxを求める
p[1] = a[1]
for i in range(2,n+1):
    p[i] = max(p[i-1], a[i])

# 右からの累積maxを求める
q[n] = a[n]
for i in range(n, 0, -1):
    q[i] = max(q[i+1], a[i])

for i in range(1, d+1):
    print(max(p[l[i] - 1], q[r[i] + 1]))