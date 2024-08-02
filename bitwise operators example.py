# Get two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Bitwise AND
bitwise_and_result = num1 & num2
print("Bitwise AND: {}".format(bitwise_and_result))

# Bitwise OR
bitwise_or_result = num1 | num2
print("Bitwise OR: {}".format(bitwise_or_result))

# Bitwise XOR
bitwise_xor_result = num1 ^ num2
print("Bitwise XOR: {}".format(bitwise_xor_result))

# Bitwise NOT (for the first number)
bitwise_not_result_num1 = ~num1
print("Bitwise NOT (num1): {}".format(bitwise_not_result_num1))

# Bitwise NOT (for the second number)
bitwise_not_result_num2 = ~num2
print("Bitwise NOT (num2): {}".format(bitwise_not_result_num2))

# Left shift
left_shift_result = num1 << 1
print("Left shift (num1): {}".format(left_shift_result))

# Right shift
right_shift_result = num2 >> 1
print("Right shift (num2): {}".format(right_shift_result))

