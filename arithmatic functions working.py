# Function to perform arithmetic operations
def perform_arithmetic_operations(num1, num2, float1, float2):
    # Addition
    sum_integers = num1 + num2
    sum_floats = float1 + float2

    # Subtraction
    difference_integers = num1 - num2
    difference_floats = float1 - float2

    # Multiplication
    product_integers = num1 * num2
    product_floats = float1 * float2

    # Division
    quotient_integers = num1 / num2
    quotient_floats = float1 / float2

    # Modulus (remainder after division)
    modulus_integers = num1 % num2

    # Display the results
    print("Sum of integers:", sum_integers)
    print("Difference of integers:", difference_integers)
    print("Product of integers:", product_integers)
    print("Quotient of integers:", quotient_integers)
    print("Modulus of integers:", modulus_integers)

    print("\nSum of floats:", sum_floats)
    print("Difference of floats:", difference_floats)
    print("Product of floats:", product_floats)
    print("Quotient of floats:", quotient_floats)

# Get input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
float1 = float(input("Enter the first floating-point number: "))
float2 = float(input("Enter the second floating-point number: "))

# Call the function to perform arithmetic operations
perform_arithmetic_operations(num1, num2, float1, float2)
