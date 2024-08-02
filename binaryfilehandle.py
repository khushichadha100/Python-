# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:30:29 2024

@author: lenovo 2020
"""

# Binary file write
file = open('binary_file.bin', 'ab')
file.write(b'Binary data goes here.\n')
file.close()

# Binary file read
file = open('binary_file.bin', 'rb')
content = file.read()
print("File content:\n", content)
file.close()

# Binary file append/update
file = open('binary_file.bin', 'ab')
file.write(b'Additional binary data.\n')
file.close()

# Binary file read after append/update
file = open('binary_file.bin', 'rb')
content = file.read()
print("Updated file content:\n", content)
file.close()
