# Task
# 1. Find the area of a rectangle where the length is 5 and the width is 8.
# 2. Find the area of a triangle where the lengths of the three sides are 8, 9, and 10.
# 3. Find the area of a circle where the radius is 3.
# 4. Convert temperatures from Celsius to Fahrenheit and Fahrenheit to Celsius.


# 1. Find the area of a rectangle where the length is 5 and the width is 8.

# Reectangle area calculation
# a = 5
# width = 8
# area_rectangle = a * width
# print("""The area of the rectangle is:""", area_rectangle)


a = 5 
b= 8 
area_ractangle = a*b
print("""The area of rectangle is :""",area_ractangle)

# 2. Find the area of a triangle where the lengths of the three sides are 8, 9, and 10.
a = 8
b = 9
c = 10

#Triangle area calculation
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is:", area)


# 3. Find the area of a circle where the radius is 3.
import math
a = 3
pi = 3.141
area = (math. pi * (3**2)) 
print("""area of circle  """, area)


# 4. Convert temperatures from Celsius to Fahrenheit and Fahrenheit to Celsius.

# Convert temperatures from Celsius to Fahrenheit.
temperatures = 20 
fahrenheit = (1.8 * 20) + 32.
print("""The fahrenheit is : """,fahrenheit)

# Convert temperatures from Fahrenheit to Celsius.
temperatures = 20 
celsius = (20 - 32) * 5/9.
print("""The Celsius is : """, celsius)