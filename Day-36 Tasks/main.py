# Write a Rust program that takes user input and determines its type based on the following rules:

# If the input is a positive integer, print "Positive Integer."
# If the input is a negative integer, print "Negative Integer."
# If the input is zero, print "Zero."
# If the input is a floating-point number, print "Floating-Point Number."
# If the input is a string containing only alphabetic characters (letters), print "Alphabetic String."
# If the input is an empty string, print "Empty String."
# For any other type of input, print "Other."
# Your program should use a match statement to categorize the input based on its type, and within each case of the match statement, you should use if-else statements to further refine the categorization.
# /////////////////////////////////////////////////////

# # If the input is a positive integer, print "Positive Integer."
# # Enter something:
# # 42
# # Output: Positive Integer


# num = int(input("Enter Positive Integer"))

# if num > 0:
#     print("Positive Integer")

# # else:
# #     print("False")

# /////////////////////////////////////////////////
# # If the input is a negative integer, print "Negative Integer."
# # Enter something:
# # -7
# # Output: Negative Integer

# num = int(input("Enter Negative Integer"))
# if num < 0:
#     print("Negative Integer")
# else:
#     print("false")

# //////////////////////////////////////////////
# # If the input is zero, print "Zero."
# # Enter something:
# # 0
# # Output: Zero

# num = int(input("Enter Zero"))
# if num == 0:
#     print("Zero")
# # elif num == 40:
# #     print("not")
# # elif  num > 40:
# #     print("yes")
# # else:
# #     print("rong")
# ////////////////////////////////////////////////////////
# # If the input is a floating-point number, print "Floating-Point Number."
# # Enter something:
# # 3.14
# # Output: Floating-Point Number


# user_input = input("Enter Floating-Point Number: ")
# try:
#     my_float = float(user_input)
#     print("Floating-Point Number")
# except ValueError:
#     print("wrong")
# if user_input == float:
#     print("yes")

# ///////////////////////////////
# # If the input is a string containing only alphabetic characters (letters), print "Alphabetic String."
# # Enter something:
# # Hello
# # Output: Alphabetic String

# user_input = input("Enter Alphabetic String: ")
# if user_input.isalpha():
#     print("Alphabetic String")
# else:
#     print("wrong")

# ///////////////////////////////


# # If the input is an empty string, print "Empty String."
# # For any other type of input, print "Other."
# # Enter something:
# # Output: Empty String

# user_input = input("Enter Empty String : ")
# if user_input == "":
#     print("Empty String")
# else:
#     print("Other")

# ///////////////////////////////


# Your program should use a match statement to categorize the input based on its type, and within each case of the match statement, you should use if-else statements to further refine the categorization.
# Enter something:
# true
# RT LT F—

# user_input = input("Enter something: ")

# match user_input:
#     case "":
#         print("Empty String")
#     case str() if user_input.isalpha():
#         print("Alphabetic String")
#     case str():
#         print("Other String")
#     case int():
#         print("Integer")
#     case float():
#         print("Floating-Point Number")
#     case _:
#         print("Other")


# ///////////////////////////////


# Enter something:
# 42
# Output: Positive Integer


# Enter something:
# -7
# Output: Negative Integer

# Enter something:
# 0
# Output: Zero

# Enter something:
# 3.14
# Output: Floating-Point Number

# Enter something:
# Hello
# Output: Alphabetic String

# Enter something:

# Output: Empty String

# Enter something:

# true

# RT LT F—
