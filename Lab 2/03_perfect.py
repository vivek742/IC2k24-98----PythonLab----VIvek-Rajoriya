def is_perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    if is_perfect(num):
        print(num, "is a perfect number.")
    else:
        print(num, "is not a perfect number.")


limit = int(input("Enter the limit: "))

if limit <= 0:
    print("Please enter a positive limit.")
else:
    print("Perfect numbers up to", limit, "are:")

    for i in range(1, limit + 1):
        if is_perfect(i):
            print(i, end=" ")

    print()