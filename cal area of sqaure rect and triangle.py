import math

# Function to calculate the area of a square
def area_of_square(side):
    return side ** 2

# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Get user's choice
print("Choose an option:")
print("1. Area of square")
print("2. Area of rectangle")
print("3. Area of triangle")

choice = int(input("Enter your choice (1/2/3): "))

# Perform calculations based on the choice
if choice == 1:
    side = float(input("Enter the side length of the square: "))
    result = area_of_square(side)
    print("Area of the square: ",result)
elif choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    result = area_of_rectangle(length, width)
    print("Area of the rectangle: ",result)
elif choice == 3:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    result = area_of_triangle(base, height)
    print("Area of the triangle: ",result)
else:
    print("Invalid choice. Please choose 1, 2, or 3.")


