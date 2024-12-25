n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

left = 1
right = 1000000000

def count_print(sec: int):
    ans = 0
    for i in range(len(a)):
        ans += sec // a[i]
    return ans

while (left < right):
    answer = (left + right) // 2
    prints = count_print(answer)
    if prints >= k: # k枚プリントできる最小値を求めるため
        right = answer
    elif prints < k:
        left = answer + 1

print(left)