# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Check for division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Display results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Division: {division}")
