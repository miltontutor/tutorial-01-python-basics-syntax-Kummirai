# Tutorial 2: Control Flow

# 1. if statement
age = 18
if age >= 18:
    print("You are an adult")

# 2. if-else statement
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. if-elif-else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")

# 4. Nested conditionals
x = 10
y = 5
if x > y:
    print("x is greater than y")
    if x > 0:
        print("x is positive")
    else:
        print("x is negative")

# 5. for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 6. while loop
count = 0
while count < 5:
    print(count)
    count += 1

# 7. break statement
for num in range(10):
    if num == 5:
        break
    print(num)

# 8. continue statement
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# 9. Nested loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 10. Loop else clause
for num in range(3):
    print(num)
else:
    print("Loop completed")