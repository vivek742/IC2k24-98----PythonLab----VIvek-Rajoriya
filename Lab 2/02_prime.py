def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

limit = int(input("Enter the limit: "))

if limit < 2:
    print("Enter a limit of at least 2.")
else:
    print("Prime numbers up to", limit, ":")

    for i in range(2, limit + 1):
        if is_prime(i):
            print(i, end=" ")

    print()
