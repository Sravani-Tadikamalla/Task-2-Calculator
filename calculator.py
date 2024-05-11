def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def get_float_input(prompt):
    """Function to get float input from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
