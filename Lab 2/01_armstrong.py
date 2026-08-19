def is_armstrong(num):
    original = num
    total = 0
    digits = len(str(num))

    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number.")
elif is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start < 0 or end < 0 or start > end:
    print("Invalid range.")
else:
    print("Armstrong numbers between", start, "and", end, "are:")

    for i in range(start, end + 1):
        if is_armstrong(i):
            print(i, end=" ")

    print()