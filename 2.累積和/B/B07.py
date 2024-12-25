t = int(input())
n = int(input())
b = [0 for _ in range(t+2)]
s = [0 for _ in range(t+2)]

for i in range(n):
    l, r = list(map(int, input().split()))
    b[l] += 1
    b[r] -= 1

for i in range(t):
    s[i+1] = s[i] + b[i]

for i in range(1,t+1):
    print(s[i])