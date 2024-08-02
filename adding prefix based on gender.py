# Function to prefix Mr./Ms. based on gender
def add_prefix(name, gender):
    if gender.upper() == 'M':
        return "Mr. " + name
    elif gender.upper() == 'F':
        return "Ms. " + name
    else:
        return "Invalid gender"

# Get input from the user
name = input("Enter a name: ")
gender = input("Enter the gender (M/F): ")

# Call the function to add the prefix
result = add_prefix(name, gender)

# Display the result
print("Result:", result)

