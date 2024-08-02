# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers and find the larger one
if num1 > num2:
    print("{} is the larger number.".format(num1))
elif num2 > num1:
    print("{} is the larger number.".format(num2))
else:
    print("Both numbers are equal.")

