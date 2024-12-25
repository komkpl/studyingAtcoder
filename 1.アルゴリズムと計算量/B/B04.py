n = input()
n = n[::-1]
sum = 0
for i in range(len(n)):
    sum += int(n[i]) * (2**i)
print(sum)