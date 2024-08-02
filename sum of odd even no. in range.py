# Initialize variables for sum of odd and even numbers
sum_odd = 0
sum_even = 0

# Iterate through numbers in the range 1 to 101
for num in range(1, 102):
    # Check if the number is odd or even
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

# Display the results
print("Sum of odd numbers from 1 to 101:", sum_odd)
print("Sum of even numbers from 1 to 101:", sum_even)

