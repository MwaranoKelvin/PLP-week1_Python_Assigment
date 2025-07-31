def calculator():
    print("Welcome to my Calculator!")
    while True:
        print("\n ===Calculator Menu=== ")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ") #This message prompts the user to select an operation.
        print(f"Operation selected: {choice}") #This message shows the operation selected by the user.

        if choice == '5':
            print("Exiting the calculator. ")
            break

# The following code is used to get the input from the user and perform the selected operation. I will use float to allow the inputs to both. Incase the user enters a decimal number.
        try: 
            num1_input = input("Enter the first number: ")
            print(f"You entered: {num1_input}")
            num1 = float(num1_input)

            num2_input = input("Enter the second number: ")
            print(f"You entered: {num2_input}")
            num2 = float(num2_input)

        except ValueError:
            print("Invalid input! Please enter numeric values.")  #This mesage is displayed if the input is not a number.
            continue

        if choice == '1':
            operator = '+'
            result = num1 + num2
        elif choice == '2':
            operator = '-'
            result = num1 - num2
        elif choice == '3':
            operator = '*'
            result = num1 * num2

        elif choice == '4':
            operator = '/'
            if num2 == 0: 
                print("Syntax Error!! Division by zero is not allowed.") #This message is displayed if the user tries to divide by zero.
                continue
            result = num1 / num2
        else:
            print("Invalid Choice! Please select from the menu.") #This message is displayed if the user enters an invalid choice.
            continue
        print(f"\nYou entered: {num1} {operator} {num2}") #This message shows the operation performed.
        print(f"The result is: {result}")
calculator()