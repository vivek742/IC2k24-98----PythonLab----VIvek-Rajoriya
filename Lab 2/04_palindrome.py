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


num = int(input("Enter a number: "))

if num < 0:
    print("Enter a non-negative number.")
else:
    if number_palindrome(num):
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")

text = input("Enter a string: ")

if string_palindrome(text):
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
