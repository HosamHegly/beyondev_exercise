def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def stringPermutation(str, i):
    if i == len(str) - 1:
        print(" ".join(str))
    for j in range(i, len(str)):
        l = [x for x in str]
        l[i], l[j] = l[j], l[i]
        stringPermutation(l, i + 1)


if __name__ == "__main__":
    print("factorial of 10", factorial(10))
    print("factorial of 1", factorial(1))
    print("factorial of 3", factorial(3))
    print("factorial of 5", factorial(5))
    print("factorial of 20", factorial(20))
    print("permutations of abc:")
    stringPermutation("abc", 0)

    print("permutations of abcd:")
    stringPermutation("abcd", 0)
