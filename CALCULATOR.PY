def calculator():
    print("Welcome to the Calculator!")
    print("\n ===Calculator Menu=== ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Choose an operation (1-5): ")
    print(f"Operation selected: {choice}")

    if choice == '5':
        print("Exiting the calculator.")
        break

    try: 
        num1_input = input("Enter the first number: ")
        print(f"You entered: {num1_input}")
        num1 = float(num1_input)

        num2_input = input("Enter the second number: ")
        print(f"You entered: {num2_input}")
        num2 = float(num2_input)

    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == '1':
        operator = '+'
        rusult = num1 + num2
    elif choice == '2':
        operator = '-'
        result = num1 - num2
    elif choice == '3':
        operator = '*'
        result = num1 * num2

    elif choice == '4':
        operator = '/'
           if num2 == 0: 
            print("Syntax Error!! Division by zero is not allowed.")
            continue
        result = num1 / num2
        
