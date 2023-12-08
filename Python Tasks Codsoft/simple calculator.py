a= int(input("Enter the num 1: "))  # Getting the first number from the user.
b = int(input("Enter the num 2: "))  # Getting the second number from the user.
if a > 0 and b > 0:  # Checks if numbers are greater than zero.
    print("Select the operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")  
    choice = int(input("Enter your choice: "))  # Getting the operation number
    if choice == 1:
        result = a + b  # Adds two numbers.
    elif choice == 2:
        result = a - b  # Subtracts two numbers.
    elif choice == 3:
        result = a * b  # Multiplies two numbers.
    elif choice == 4:
        if b != 0:  # Check for division by zero.
            result = a / b  # Divides a by b.
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Enter a valid choice")
    
    print("Result:",result)  # Displays the result.
else:
    print("Enter valid numbers")