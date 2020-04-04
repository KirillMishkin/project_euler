import time


def IsPrime(n):
    div = 2
    while n % div != 0:
        div += 1
    return div == n


def number_prime(i):
    num_prime = 0
    while True:
        i += 1
        if IsPrime(i):
            num_prime += 1
            if num_prime >= 10001:
                return print(i)


start = time.time()
number_prime(1)
print(time.time() - start)
