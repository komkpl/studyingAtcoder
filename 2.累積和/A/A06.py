n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [0 for _ in range(n+1)]

for i in range(n):
    s[i+1] = s[i] + a[i]

for i in range(q):
    l, r = list(map(int, input().split()))
    print(s[r] - s[l-1])