n = int(input())

ED = 0.001
left = 0.0
right = 100000.0

def is_answer(x: float):
    if abs(n - x*x*x - x) <= ED:
        return True
    return False

while left < right:
    mid = (left + right) / 2
    if is_answer(mid):
        print(mid)
        break
    else:
        if mid*mid*mid + mid < n:
            left = mid
        else:
            right = mid