# Get user's age and membership status
age = int(input("Enter your age: "))
is_member = input("Are you a senior member? (yes/no): ").lower()  # Convert to lowercase for case-insensitivity

# Check eligibility for a discount
if (age >= 60 and is_member == 'yes') or (age < 18 and is_member == 'yes'):
    print("You are eligible for a senior or youth discount.")
else:
    print("You are not eligible for a senior or youth discount.")

