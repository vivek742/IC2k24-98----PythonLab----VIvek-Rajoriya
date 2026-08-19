count = 0


def fibonacci_loop(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


def fibonacci_recursive(n):
    global count

    count = count + 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive number.")
else:
    print("Fibonacci using loop:")
    fibonacci_loop(n)

    print("\nFibonacci using recursion:")

    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    count = 0

    for i in range(n):
        fibonacci_recursive(i)

    print("\nNumber of recursive function calls:", count)
