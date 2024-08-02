# Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:")
for row in nested_list:
    print(row)

# Length
my_list = [1, 2, 3, 4, 5]
print("\nLength of the list:", len(my_list))

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("\nConcatenated List:", concatenated_list)

# Membership
if 3 in my_list:
    print("\n3 is present in the list")
else:
    print("\n3 is not present in the list")

# Iteration
print("\nIterating through the list:")
for item in my_list:
    print(item)

# Indexing
print("\nIndexing example:")
print("Element at index 2:", my_list[2])

# Slicing
print("\nSlicing example:")
print("Elements from index 1 to 3:", my_list[1:4])


# Add
numbers = [1, 2, 3]
print("\nOriginal List:", numbers)

# Append
numbers.append(4)
print("After Append:", numbers)

# Extend
numbers.extend([5, 6, 7])
print("After Extend:", numbers)

# Delete
del numbers[1]
print("After Deleting element at index 1:", numbers)
