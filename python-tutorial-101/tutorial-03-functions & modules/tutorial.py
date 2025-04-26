# Tutorial 3: Functions & Modules

# 1. Basic Function
def greet(name):
    """Simple greeting function"""
    print(f"Hello, {name}!")

greet("Alice")

# 2. Return Values
def add(a, b):
    """Returns sum of two numbers"""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# 3. Parameters vs Arguments
def describe_pet(pet_name, animal_type="dog"):
    """Demonstrates default parameters"""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Fido")  # Uses default
describe_pet("Whiskers", "cat")  # Overrides default

# 4. Variable Scope
global_var = "I'm global"

def show_scope():
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

show_scope()
# print(local_var)  # Would cause error - out of scope

# 5. Default Arguments
def make_shirt(size="L", message="I love Python"):
    """Shirt with default size and message"""
    print(f"Making a {size} shirt with: '{message}'")

make_shirt()
make_shirt("M")
make_shirt(message="Hello World")

# 6. Variable-length Arguments
def make_pizza(*toppings):
    """Accepts any number of arguments"""
    print("\nMaking pizza with:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'peppers', 'olives')

# 7. Lambda Functions
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Sort list of tuples by second element
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda pair: pair[1])
print(f"Sorted pairs: {pairs}")

# 8. Function Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 9. Module Creation
# See temperature.py and math_ops.py in assignments

# 10. Package Structure
# See assignment 10 for package example