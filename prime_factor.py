import math


def prime_factorization(number):
    factors = []
    while number % 2 == 0:
        number /= 2
        factors.append(2)

    for odd in range(3, int(math.sqrt(number)+1), 2):
        while number % odd == 0:
            number /= odd
            factors.append(odd)
    if number != 1:  # if n is odd prime number
        factors.append(number)

    return factors


if __name__ == "__main__":
    number = 900
    print(prime_factorization(number))
