#                                    About String


# Using single quotes
str1 = 'Hello Python'
print(str1)
# Using double quotes
str2 = "Hello Python"
print(str2)
# Using triple quotes
str3 = '''''Triple quotes are generally used for  
    represent the multiline'''
print(str3)
# /////////////////////////////////////////////////////////////

# Strings indexing and splitting
str = "HELLO"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
# revers
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])
# It returns the IndexError because 6th index is not
print(str[6])
# /////////////////////////////////////////////////////////////

# Strings have a bunch of methods available.
text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)

# capitalize() Converts the first character to upper case
text = "Hello, World!"
casefolded_text = text.casefold()
print(casefolded_text)

# casefold() Converts string into lower case
text = "ThIs Is A sTrInG WiTh MiXeD CaSe"
casefolded_text = text.casefold()
print(casefolded_text)

# center() Returns a centered string
text = "Python"
centered_text = text.center(12, '*')
print(centered_text)

# count() Returns the number of times a specified value occurs in a string
text = "apple apple orange apple banana"
count_apple = text.count("apple")
print(count_apple)  # Output: 3

# encode() Returns an encoded version of the string
text = "Hello, World!"
encoded_text = text.encode(encoding="utf-8")
print(encoded_text)

# endswith() Returns true if the string ends with the specified value
text = "Hello, World!"
result = text.endswith("Hello", 0, 5)
print(result)  # Output: True

# expandtabs() Sets the tab size of the string
text = "Hello\tWorld"
expanded_text = text.expandtabs(4)
print(expanded_text)

# find(substring): Searches the string for a specified substring and returns the position of where it was found.
text = "Hello, World!"
position = text.find("World")
print(position)  # Output: 7

# format(*args, **kwargs): Formats the string by replacing placeholders with specified values.
name = "Alice"
age = 30
formatted_text = "My name is {} and I am {} years old.".format(name, age)
print(formatted_text)
# Output: My name is Alice and I am 30 years old.

# format_map(mapping): Formats the string by replacing placeholders with values from a mapping.
data = {"name": "Bob", "age": 25}
formatted_text = "My name is {name} and I am {age} years old.".format_map(data)
print(formatted_text)
# Output: My name is Bob and I am 25 years old.

# index(substring): Searches the string for a specified substring and returns the position of where it was found (raises an exception if not found).
text = "Hello, World!"
position = text.index("World")
print(position)  # Output: 7

# isalnum(): Returns True if all characters in the string are alphanumeric.
text = "Hello123"
result = text.isalnum()
print(result)  # Output: True

# isalpha(): Returns True if all characters in the string are alphabetic.
text = "Hello"
result = text.isalpha()
print(result)  # Output: True


# isascii(): Returns True if all characters in the string are ASCII characters.
text = "Hello"
result = text.isascii()
print(result)  # Output: True

# isdecimal(): Returns True if all characters in the string are decimal digits.
text = "12345"
result = text.isdecimal()
print(result)  # Output: True

# isdigit(): Returns True if all characters in the string are digits.
text = "12345"
result = text.isdigit()
print(result)  # Output: True

# isidentifier(): Returns True if the string is a valid Python identifier.
text = "my_var"
result = text.isidentifier()
print(result)  # Output: True

