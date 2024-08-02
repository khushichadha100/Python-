def write_record(file, roll, name, marks):
    with open(file, 'ab') as f:
        # Convert roll and marks to bytes
        roll_bytes = roll.to_bytes(4, 'big')
        marks_bytes = marks.to_bytes(1, 'big')

        # Truncate or pad name to 20 characters
        name_bytes = name.encode('utf-8')[:20] + b'\x00' * (20 - len(name.encode('utf-8')))

        # Write the record to the file
        f.write(roll_bytes + name_bytes + marks_bytes)

def display_records(file):
    with open(file, 'rb') as f:
        while True:
            # Read a record
            record_data = f.read(25)
            if not record_data:
                break

            # Unpack the record
            roll, name, marks = int.from_bytes(record_data[:4], 'big'), record_data[4:24].decode('utf-8').rstrip('\x00'), int.from_bytes(record_data[24:], 'big')
            
            # Display the record
            print(f"Roll Number: {roll}, Name: {name}, Marks: {marks}")

def search_record(file, roll):
    with open(file, 'rb') as f:
        while True:
            # Read a record
            record_data = f.read(25)
            if not record_data:
                break

            # Unpack the record
            current_roll = int.from_bytes(record_data[:4], 'big')

            # Check if the roll number matches
            if current_roll == roll:
                return current_roll, record_data[4:24].decode('utf-8').rstrip('\x00'), int.from_bytes(record_data[24:], 'big')
    return None

def update_record(file, roll, new_marks):
    with open(file, 'r+b') as f:
        while True:
            # Read a record
            record_data = f.read(25)
            if not record_data:
                break

            # Unpack the record
            current_roll = int.from_bytes(record_data[:4], 'big')

            # Check if the roll number matches
            if current_roll == roll:
                # Update the marks
                f.seek(-1, 1)
                f.write(new_marks.to_bytes(1, 'big'))
                break

def delete_record(file, roll):
    records = []
    with open(file, 'rb') as f:
        while True:
            # Read a record
            record_data = f.read(25)
            if not record_data:
                break

            # Unpack the record
            current_roll = int.from_bytes(record_data[:4], 'big')

            # Check if the roll number matches
            if current_roll != roll:
                records.append(record_data)

    # Write the remaining records back to the file
    with open(file, 'wb') as f:
        for record in records:
            f.write(record)

# Example usage
file_path = "student_records.dat"

# Add records
write_record(file_path, 101, "John Doe", 85)
write_record(file_path, 102, "Jane Smith", 92)

# Display all records
print("All Records:")
display_records(file_path)

# Search for a record
search_roll_number = 18
search_result = search_record(file_path, search_roll_number)
if search_result:
    print(f"\nRecord Found: Roll Number {search_result[0]}, Marks: {search_result[2]}")

# Update the marks of a record
update_roll_number = 102
new_marks = 95
update_record(file_path, update_roll_number, new_marks)
print(f"\nUpdated Marks for Roll Number {update_roll_number}")

# Display all records after update
print("\nAll Records after Update:")
display_records(file_path)

# Delete a record
delete_roll_number = 101
delete_record(file_path, delete_roll_number)
print(f"\nRecord Deleted: Roll Number {delete_roll_number}")

# Display all records after delete
print("\nAll Records after Delete:")
display_records(file_path)
