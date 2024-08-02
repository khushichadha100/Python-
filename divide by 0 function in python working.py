# Take two numbers as input
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

# Check if the denominator is not zero to avoid division by zero
if denominator != 0:
    # Perform the division
    result = numerator / denominator

    # Check if the result is equal to 1
    if result == 1:
        print("The result of {} / {} is equal to 1.".format(numerator, denominator))
    else:
        print("The result is not equal to 1.")
else:
    print("Error: Division by zero is not allowed.")

