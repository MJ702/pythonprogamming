import math


def countPrime(n):
    if n < 2:
        return 0

    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False

    for i in range(2, math.ceil(math.sqrt(n))):
        if isPrime[i]:
            for multiple_of_i in range(i * i, n, i):
                isPrime[multiple_of_i] = False

    return sum(isPrime)


result = countPrime(10)
print(result)
