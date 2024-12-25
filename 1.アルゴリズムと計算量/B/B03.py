n = int(input())
a = list(map(int, input().split()))
existance = 0

for i in range(n):
    for j in range(n):
        if i != j:
            if ((1000 - a[i] - a[j]) in a) and a.index(1000 - a[i] - a[j]) != i and a.index(1000 - a[i] - a[j]) != j:
                existance = 1

if existance:
    print('Yes')
else:
    print('No')