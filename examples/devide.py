# divide.py

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

if __name__ == "__main__":
    try:
        # Input from the user
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        # Calculate the division
        result = divide_numbers(num1, num2)

        # Display the result
        print("The result of dividing {num1} by {num2} is {result}")
    except ValueError:
        print
        ("Invalid input. Please enter numeric values.")

        print ('devide is mathemetical function')