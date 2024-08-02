# Function to calculate the length of a string
def calculate_length(string):
    return len(string)

# Function to concatenate two strings
def concatenate_strings(string1, string2):
    return string1 + string2

# Function to check if two strings are equal
def are_strings_equal(string1, string2):
    return string1 == string2

# Function to reverse a string
def reverse_string(string):
    return string[::-1]

# Function to display the menu options
def display_menu():
    print("\nMenu:")
    print("1. Calculate the length of a string")
    print("2. Concatenate two strings")
    print("3. Check if two strings are equal")
    print("4. Reverse a string")
    print("5. Exit")

# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

while True:
    # Display the menu
    display_menu()

    # Get the user's choice
    choice = int(input("Enter your choice (1-5): "))

    # Perform operations based on user's choice
    if choice == 1:
        print("Length of string 1:", calculate_length(string1))
        print("Length of string 2:", calculate_length(string2))
    elif choice == 2:
        result = concatenate_strings(string1, string2)
        print("Concatenated string:", result)
    elif choice == 3:
        if are_strings_equal(string1, string2):
            print("The two strings are equal.")
        else:
            print("The two strings are not equal.")
    elif choice == 4:
        print("Reversed string 1:", reverse_string(string1))
        print("Reversed string 2:", reverse_string(string2))
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
