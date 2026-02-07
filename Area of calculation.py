# Program to calculate the area of circle, triangle and square

# Circle
radius = float(input("Enter the radius of circle: "))
area_circle = 3.14 * radius * radius
print("Area of Circle:", area_circle)

# Triangle
base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
area_triangle = 0.5 * base * height
print("Area of Triangle:", area_triangle)

# Square
side = float(input("Enter the side of square: "))
area_square = side * side
print("Area of Square:", area_square)