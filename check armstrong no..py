# Function to calculate the power of a number
def power(x, y):
    return x ** y

# Function to count the number of digits in a number
def count_digits(num):
    return len(str(num))

# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    num_digits = count_digits(number)
    temp = number
    sum_digits = 0

    while temp > 0:
        digit = temp % 10
        sum_digits += power(digit, num_digits)
        temp //= 10

    return number == sum_digits

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
    
