def calculator(a, b, operation):
    """Returns the result of a basic math operation (+, -, *, /) on a and b."""
    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Error: Division by zero"
    }
    return operations.get(operation, "Invalid operation")

# Get input from the user
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    result = calculator(a, b, operation)
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")
