import time


def triangular_div(n):
    prime_divisor = 2  # minimum prime_divisor
    lst = []  # prime_divisor sheet
    multiplication = 1
    s = n * (n + 1) // 2
    while True:
        if s % prime_divisor == 0:
            s //= prime_divisor
            lst.append(prime_divisor)
        else:
            prime_divisor += 1
        if s == 1:
            for dig in set(lst):
                multiplication *= (lst.count(dig) + 1)
            if multiplication >= 500:
                return True
            else:
                return False


start = time.time()
i = 1
while True:
    if triangular_div(i):
        Tn = ((i+1)*i)//2
        print(Tn)
        break
    i += 1
print(time.time() - start)
