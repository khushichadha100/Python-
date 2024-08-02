# Function to find the smallest and largest numbers in a list
def find_smallest_and_largest(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    smallest = largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

# Get input from the user: a list of numbers
numbers_str = input("Enter a list of numbers separated by spaces: ")
numbers = [float(num) for num in numbers_str.split()]

# Call the function to find the smallest and largest numbers
smallest, largest = find_smallest_and_largest(numbers)

# Display the results
if smallest is not None and largest is not None:
    print("Smallest number: {:.2f}".format(smallest))
    print("Largest number: {:.2f}".format(largest))
else:
    print("The list is empty.")
