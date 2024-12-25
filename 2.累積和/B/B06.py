n = int(input())
a = list(map(int, input().split()))
a = [a[i] if a[i]==1 else -1 for i in range(n)]

s = [0 for i in range(n+1)]

for i in range(n):
    s[i+1] = s[i] + a[i]

q = int(input())
for i in range(q):
    l, r = list(map(int, input().split()))
    if s[r] - s[l-1] > 0:
        print('win')
    elif s[r] - s[l-1] < 0:
        print('lose')
    else:
        print('draw')