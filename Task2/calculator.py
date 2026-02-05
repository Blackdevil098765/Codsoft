print("--- Welcome to the Simple Calculator ---")

# 1. Prompt the user for input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

# 2. Prompt for the operation choice
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter choice (1/2/3/4): ")

# 3. Perform calculation and display the result
if choice == '1':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == '2':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == '3':
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == '4':
    # Check for division by zero
    if num2 == 0:
        print("\nError! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

else:
    print("\nInvalid choice. Please select a valid operation (1-4).")
