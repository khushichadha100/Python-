# Dictionary of months and their corresponding days
months_dict = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Ask the user to enter a month
user_month = input("Enter a month name: ")

# Check if the entered month is in the dictionary
if user_month in months_dict:
    print(f"The month {user_month} has {months_dict[user_month]} days.")
else:
    print("Invalid month name. Please enter a valid month.")

# Print all keys in alphabetical order
print("\nAll months in alphabetical order:")
for month in sorted(months_dict.keys()):
    print(month)

# Print months with 31 days
print("\nMonths with 31 days:")
for month, days in months_dict.items():
    if days == 31:
        print(month)

# Print key-value pairs sorted by the number of days in each month
print("\nMonths and their days sorted by the number of days:")
sorted_months = sorted(months_dict.items(), key=lambda x: x[1])
for month, days in sorted_months:
    print(f"{month}: {days} days")
