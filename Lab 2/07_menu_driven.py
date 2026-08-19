def armstrong(num):
    original = num
    digits = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    return total == original


def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def perfect(num):
    if num <= 0:
        return False

    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    return total == num


def number_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse


def string_palindrome(text):
    reverse = ""

    for i in range(len(text) - 1, -1, -1):
        reverse = reverse + text[i]

    return text == reverse


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


def patterns(n):
    print("\nStar Pattern")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    print("\nNumber Pattern")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\nCentered Pyramid")

    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


while True:
    print("\n========== MENU ==========")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")
    print("==========================")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))

        if num < 0:
            print("Enter a non-negative number.")
        elif armstrong(num):
            print(num, "is an Armstrong number.")
        else:
            print(num, "is not an Armstrong number.")

    elif choice == 2:
        num = int(input("Enter a number: "))

        if prime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")

    elif choice == 3:
        num = int(input("Enter a number: "))

        if num <= 0:
            print("Enter a positive number.")
        elif perfect(num):
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")

    elif choice == 4:
        num = int(input("Enter a number: "))

        if num < 0:
            print("Enter a non-negative number.")
        elif number_palindrome(num):
            print(num, "is a palindrome.")
        else:
            print(num, "is not a palindrome.")

        text = input("Enter a string: ")

        if string_palindrome(text):
            print("String is a palindrome.")
        else:
            print("String is not a palindrome.")

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        if n <= 0:
            print("Enter a positive number.")
        else:
            fibonacci(n)

    elif choice == 6:
        n = int(input("Enter number of rows: "))

        if n <= 0:
            print("Enter a positive number.")
        else:
            patterns(n)

    elif choice == 7:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
