# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the sum of primes in a range
def sum_of_primes(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_sum += num
    return total_sum

# Get input from the user
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Calculate and print the sum of prime numbers in the range
result = sum_of_primes(start_range, end_range)
print(f"The sum of prime numbers between {start_range} and {end_range} is: {result}")
