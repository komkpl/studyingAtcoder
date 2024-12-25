d = int(input())
n = int(input())

b = [0 for i in range(d+2)]
S = [0 for i in range(d+2)]
for i in range(n):
    l, r = list(map(int, input().split()))
    b[l] += 1
    b[r+1] -= 1

for i in range(1,d+1):
    S[i] = S[i-1] + b[i]

for i in range(1,d+1):
    print(S[i])