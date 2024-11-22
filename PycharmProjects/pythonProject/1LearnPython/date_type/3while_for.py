import random

sum = 0
for i in range(1, 11, 2):  # (1,3,5,7,9) 左闭右开
    sum += i
print(sum)

for n in range(1, 1001):
    if (n == 1):
        n += 1
        continue
    elif (n == 2):
        print(n)
    else:
        isPrime = True
        for i in range(2, n):
            if (n % i) == 0:
                isPrime = False
                break
        if (isPrime):
            print(n)
    n += 1
