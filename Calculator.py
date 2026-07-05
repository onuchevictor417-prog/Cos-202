while True:

    print("\n==============================")
    print("   MATHEMATICAL CALCULATOR")
    print("==============================")
    print("SELECT FROM ANY OF THE FOLLOWING FUNCTIONS")
    print("PRESS 1 FOR '+' ADDITION")
    print("PRESS 2 FOR '-' SUBTRACTION")
    print("PRESS 3 FOR '*' MULTIPLICATION")
    print("PRESS 4 FOR '/' DIVISION")
    print("PRESS 5 FOR '%' MODULUS")
    print("PRESS 6 FOR '^' TO THE POWER")
    print("PRESS C TO CLEAR")
    print("PRESS OFF TO EXIT")

    op = input("\nEnter Operation: ").upper()

    if op == "OFF":
        print("Calculator Closed.")
        break

    elif op == "C":
        print("\n" * 50)

    elif op == "1":
        print("YOU'VE SELECTED THE ADDITION OPERATION")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("Answer =", num1 + num2)

    elif op == "2":
        print("YOU'VE SELECTED THE SUBTRACTION OPERATION")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("Answer =", num1 - num2)

    elif op == "3":
        print("YOU'VE SELECTED THE MULTIPLICATION OPERATION")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("Answer =", num1 * num2)

    elif op == "4":
        print("YOU'VE SELECTED THE DIVISION OPERATION")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Answer =", num1 / num2)

    elif op == "5":
        print("YOU'VE SELECTED THE MODULUS OPERATION")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("Answer =", num1 % num2)

    elif op == "6":
        print("YOU'VE SELECTED THE POWER OPERATION")
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        print("Answer =", num1 ** num2)

    else:
        print("Invalid Operation. Please try again.")
