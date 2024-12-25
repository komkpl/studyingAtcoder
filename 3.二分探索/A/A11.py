n, x = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = n-1

for i in range(n+1):
    m = (l+r)//2
    if a[m] == x:
        break
    elif a[m] > x:
        r = m - 1
    else:
        l = m + 1

print(m+1)