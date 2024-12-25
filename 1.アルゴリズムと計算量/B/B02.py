a, b = list(map(int,input().split()))
existance = 0
for i in range(a, b+1):
    if 100 % i == 0:
        existance = 1

if existance == 0:
    print('No')
else:
    print('Yes')