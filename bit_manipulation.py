def isOdd(x : int):

    return x & 1 == 1 # check if LSB is 1 if it is then x is odd


def countBits(x : int):
    count = 0
    while x:
        if x & 1 == 1:
            count += 1
        x >>= 1 # right shift
    return count



if __name__ == "__main__":
    print(isOdd(4))
    print(isOdd(9))

    print(countBits(7))
    print(countBits(9))
    print(countBits(32))
    print(countBits(2))