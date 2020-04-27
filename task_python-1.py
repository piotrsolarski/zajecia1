def is_prime(num):
    count = 0
    for i in range(2, num - 1):
        if num % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def myprimef(num):
    primes = []
    for i in range(num):
        if is_prime(i):
            primes.append(i)
    return primes


print(myprimef(100))
