n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
q = int(input())

x = [0 for i in range(q)]
for i in range(q):
    x[i] = int(input())

for i in range(q):
    left = 0
    right = n-1
    while True:
        mid = (left + right) // 2
        if a[mid] < x[i]:
            left = mid
            if mid == n-1:
                print(n)
                break
            if a[mid+1] > x[i]:
                print(mid+1)
                break
            elif mid+1 == n-1:
                print(n)
                break

        else:
            right = mid
            if mid == 0:
                print(mid+1)
                break
            if a[mid-1] < x[i]:
                print(mid)
                break
            elif mid-1 == 0:
                print(0)
                break