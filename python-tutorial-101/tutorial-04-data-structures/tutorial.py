# Tutorial 4: Data Structures

# 1. List Operations
fruits = ['apple', 'banana', 'orange']
fruits.append('kiwi')
fruits.insert(1, 'pear')
print(f"List operations: {fruits}")

# 2. List Comprehensions
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# 3. Tuple Unpacking
coordinates = (4, 5)
x, y = coordinates
print(f"Unpacked coordinates: x={x}, y={y}")

# 4. Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")

# 5. Dictionary Methods
student = {'name': 'Alice', 'age': 21}
print(f"Keys: {student.keys()}")
print(f"Get age: {student.get('age')}")

# 6. Nested Structures
school = {
    'class1': ['Alice', 'Bob'],
    'class2': ['Charlie', 'Dana']
}
print(f"Nested structure: {school}")

# 7. Stack/Queue with Lists
stack = []
stack.append(1)  # push
stack.append(2)
print(f"Stack pop: {stack.pop()}")

queue = []
queue.append(1)  # enqueue
queue.append(2)
print(f"Queue dequeue: {queue.pop(0)}")

# 8. Dictionary Comprehensions
square_dict = {x: x**2 for x in range(5)}
print(f"Dictionary comprehension: {square_dict}")

# 9. Data Structure Conversion
tuple_from_list = tuple([1, 2, 3])
list_from_tuple = list((1, 2, 3))
print(f"Conversions: {tuple_from_list}, {list_from_tuple}")

# 10. Real-world Application
inventory = {
    'apples': 50,
    'oranges': 25,
    'bananas': 30
}
print(f"Inventory: {inventory}")