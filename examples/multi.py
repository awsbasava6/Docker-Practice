# multiplication.py

def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    # Input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the product
    result = multiply_numbers(num1, num2)

    # Display the result
    print(f"The product of {num1} and {num2} is {result}")
