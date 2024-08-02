# Create a list of the first 10 letters of the alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Print the first 3 letters of the list
print("First 3 letters:", alphabet[:3])

# Print any 3 letters from the middle
middle_index = len(alphabet) // 2
print("Any 3 letters from the middle:", alphabet[middle_index:middle_index + 3])

# Print the letters from a particular index to the end of the list
start_index = 7
print(f"Letters from index {start_index} to the end:", alphabet[start_index:])
