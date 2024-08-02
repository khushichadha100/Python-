def create_csv_file(file_path):
    # Check if the file already exists
    if not file_exists(file_path):
        # Create the CSV file with header
        with open(file_path, 'w') as csvfile:
            csvfile.write("user_id,password\n")
        print(f"CSV file '{file_path}' created successfully.")
    else:
        print(f"CSV file '{file_path}' already exists.")

def add_user_credentials(file_path, user_id, password):
    # Append user credentials to the CSV file
    with open(file_path, 'a') as csvfile:
        csvfile.write(f"{user_id},{password}\n")
    print("User credentials added successfully.")

def search_password(file_path, user_id):
    # Search for the password associated with the given user ID
    with open(file_path, 'r') as csvfile:
        next(csvfile)  # Skip the header
        for line in csvfile:
            current_user_id, found_password = line.strip().split(',')
            if current_user_id == user_id:
                return found_password
    return None

def read_csv_file(file_path):
    # Read and display the contents of the CSV file
    with open(file_path, 'r') as csvfile:
        print("Contents of CSV file:")
        for line in csvfile:
            print(line.strip())

def file_exists(file_path):
    # Check if the file exists
    try:
        with open(file_path, 'r'):
            return True
    except FileNotFoundError:
        return False

# Example usage
file_path = input("Enter the path of the CSV file: ")

# Create or check the existence of the CSV file
create_csv_file(file_path)

# Add user credentials
user_id = input("Enter user ID: ")
password = input("Enter password: ")
add_user_credentials(file_path, user_id, password)

# Search for a password
search_user_id = input("Enter user ID to search for password: ")
found_password = search_password(file_path, search_user_id)

if found_password:
    print(f"Password for user ID '{search_user_id}': {found_password}")
else:
    print(f"No password found for user ID '{search_user_id}'.")

# Read and display the contents of the CSV file
read_csv_file(file_path)

