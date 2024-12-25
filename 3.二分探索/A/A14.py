n, key = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

# 半列挙
q = [0 for i in range(n*n)]
p = [0 for i in range(n*n)]
k = 0
for i in range(n):
    for j in range(n):
        q[k] = a[i] + b[j]
        k += 1
k = 0
for i in range(n):
    for j in range(n):
        p[k] = c[i] + d[j]
        k += 1

q = sorted(q)
p = sorted(p)

# k - q = pとなる値を二分探索で探す
is_exist = False
for i in range(n*n):
    if is_exist:
        break
    query = key - q[i]
    left = 0
    right = n*n - 1
    while left < right:
        mid = (left + right) // 2
        if query > p[mid]:
            left = mid + 1
        elif query < p[mid]:
            right = mid
        else:
            is_exist = True
            break

if is_exist:
    print("Yes")
else:
    print("No")