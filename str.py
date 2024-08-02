# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:21:51 2023

@author: lenovo 2020
"""

#Converts the first character to upper case
txt = "hello, and welcome to my world."
x=txt.capitalize()
print (x)
#Converts a string into upper case
txt="hello"
x=txt.upper()
print(x)
#Converts string into lower case
txt="Hello, And Welcome To My World!"
x=txt.casefold()
print(x)
#Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("o")
print(x)
#Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith("?")
print(x)
#Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
#Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
#Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
#Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)
#Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)
#Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)
#Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)
#Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)