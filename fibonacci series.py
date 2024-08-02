# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get input from the user
term_count = int(input("Enter the number of terms in the Fibonacci series: "))

# Display the Fibonacci series
if term_count > 0:
    print("Fibonacci Series:")
    for i in range(1, term_count + 1):
        print(fibonacci(i), end=" ")
else:
    print("Invalid input. Please enter a positive integer for the number of terms.")

