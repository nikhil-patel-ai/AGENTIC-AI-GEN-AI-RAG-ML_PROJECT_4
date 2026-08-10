# Python Variables - Practice

# 1. Creating Variables

name = "Nikhil Patel"
age = 21
city = "Maihar"
print(name)
print(age)
print(city)

# 2. Assigning Values

student_name = "Ankit"
student_age = 20
print(student_name)
print(student_age)

# 3. Reassigning Variables

age = 20
print(age)
age = 22
print(age)

# 4. Using Variables in Calculations

num1 = 10
num2 = 20
sum_result = num1 + num2
difference = num2 - num1
product = num1 * num2
division = num2 / num1
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)


# 5. Multiple Assignment

name, age, city = "Nikhil Patel", 21, "Maihar"
print(name)
print(age)
print(city)


# 6. Assigning Same Value to Multiple Variables

a = b = c = 200
print(a)
print(b)
print(c)

# 7. Unpacking Values

numbers = (20, 30, 40)
x, y, z = numbers
print(x)
print(y)
print(z)


# 8. Swapping Variables

a = 50
b = 100
print("Before swapping:")
print("a =", a)
print("b =", b)
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

# 9. Printing Variables with Text

name = "Nikhil Patel"
age = 21
print("My name is", name)
print("My age is", age)

# 10. Using Variables in Expressions

price = 500
quantity = 5
total = price * quantity
print("Total price:", total)

# 11. Checking Variable Type

name = "Ankit"
age = 21
print(type(name))
print(type(age))