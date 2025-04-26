
# Tutorial 1: Python Basics & Syntax

# 1. Variables and Data Types
name = "Alice"  # String
age = 25        # Integer
height = 5.6    # Float
is_student = True  # Boolean

# 2. Input and Output
print("Hello, World!")
user_input = input("Enter your name: ")
print(f"Welcome, {user_input}!")

# 3. Comments
# This is a single-line comment
"""
This is a
multi-line comment
"""

# 4. Arithmetic Operators
x = 10
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation

# 5. Comparison Operators
print(x > y)   # Greater than
print(x == y)  # Equal to
print(x != y)  # Not equal to

# 6. Logical Operators
print(True and False)  # AND
print(True or False)   # OR
print(not True)        # NOT

# 7. Type Conversion
num_str = "10"
num_int = int(num_str)
print(num_int + 5)

# 8. String Operations
greeting = "Hello"
print(greeting.lower())
print(greeting.upper())
print(len(greeting))
print(greeting + " World!")

# 9. List Basics
fruits = ["apple", "banana", "cherry"]
print(fruits[1])       # Access element
fruits.append("orange") # Add element
print(len(fruits))     # List length

# 10. Dictionary Basics
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
print(person["name"])
person["age"] = 26     # Update value
print(person.keys())   # Dictionary keys