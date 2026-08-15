while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator exited.")
        break

    if choice in ["+", "-", "*", "/"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "+":
            print("Result:", num1 + num2)

        elif choice == "-":
            print("Result:", num1 - num2)

        elif choice == "*":
            print("Result:", num1 * num2)

        elif choice == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
    else:
        print("Invalid choice. Please try again.")