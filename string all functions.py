

str="Hello, how are you?"
print(str.upper()) #HELLO, HOW ARE YOU?
print(str.lower())#hello, how are you?
print(str.swapcase())#hELLO, hOW ARE YOU?
print(str.count('a'))#1
###String Methods
str="we are learning string methods"
print(str.endswith("methods")) #True
print(str.startswith("methods")) #False
print(str.isupper()) #False
print (str.islower()) #True
print("Forest".isnumeric()) #False
print("12345".isnumeric()) #True
print("For45".isalnum()) #True
print("1234".isdigit())
print("   ".isspace())
print(str.capitalize())
print("khushi".find('u'))  #letter not present(-1)  
print('#'.join('khushi'))
name='khushi hii welcome'
print(name.replace('k','g'))
print(name.split())
print(name.title())


