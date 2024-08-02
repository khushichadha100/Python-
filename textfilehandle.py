# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:22:49 2024

@author: lenovo 2020
"""

# Text file write
file = open('text_file.txt', 'w')
file.write('Hello, this is a text file.\n')
file.close()

# Text file read
file = open('text_file.txt', 'r')
content = file.read()
print("File content:\n", content)
file.close()

# Text file append/update
file = open('text_file.txt', 'a')
file.write('Appending a new line.\n')
file.close()

# Text file read after append/update
file = open('text_file.txt', 'r')
content = file.read()
print("Updated file content:\n", content)
file.close()

file=open('text_file.txt', 'r+')  
lines = file.readlines()
lines.insert(1,'Inserted line.\n')
file.seek(0)
file.writelines(lines)

# Reading after Insertion
with open('text_file.txt', 'r') as file:
    content = file.read()
    print("Updated file content after insertion:\n", content)

# Deletion
with open('text_file.txt', 'r+') as file:
    lines = file.readlines()
    del lines[2]  # Deleting the third line
    file.seek(0)
    file.writelines(lines)

# Reading after Deletion
with open('text_file.txt', 'r') as file:
    content = file.read()
    print("Updated file content after deletion:\n", content)