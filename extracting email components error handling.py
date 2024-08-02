def extract_email_components(email):
    # Split the email address into username and domain
    username, domain = email.split('@', 1)
    
    # Return a tuple of username and domain
    return username, domain

# Get user input for an email address
email_address = input("Enter an email address: ")

try:
    # Extract components and form a tuple
    email_tuple = extract_email_components(email_address)
    
    # Print the result
    print("Username:", email_tuple[0])
    print("Domain:", email_tuple[1])
    print(email_tuple)
except ValueError:
    print("Invalid email address format")

