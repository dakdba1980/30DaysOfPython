# Day 2: 30 Days of python programming

first_name = 'Anil'
last_name = 'Dasari'
full_name = 'Anil Kumar Dasari'
country = 'India'
city = 'Hyderabad'
age = 25
is_married = False
is_true = True
is_light_on = True
skills = ['Python', 'JavaScript', 'HTML', 'CSS']
person_info = {
    'first_name': first_name,
    'last_name': last_name,
    'full_name': full_name,
    'country': country,
    'city': city,
    'age': age,
    'is_married': is_married,
    'is_true': is_true,
    'is_light_on': is_light_on,
    'skills': skills
}

# Printing variables
print(first_name)  # Output: Anil
print(last_name)   # Output: Dasari
print(full_name)   # Output: Anil Kumar Dasari
print(country)     # Output: India
print(city)        # Output: Hyderabad
print(age)         # Output: 25
print(is_married)  # Output: False
print(is_true)     # Output: True
print(is_light_on)  # Output: True
print(skills)      # Output: ['Python', 'JavaScript', 'HTML', 'CSS']
print(person_info)  # Output: {'first_name': 'Anil', 'last_name: 'Dasari', 'full_name': 'Anil Kumar Dasari', 'country': 'India', 'city': 'Hyderabad', 'age': 25, 'is_married': False, 'is_true': True, 'is_light_on': True, 'skills': ['Python', 'JavaScript', 'HTML', 'CSS']}

# declare multiple variables in one line
a, b, c = 5, 10, 15
print(a, b, c)  # Output: 5 10 15

# Check the data type of all your variables using type() built-in function
print(type(first_name))  # Output: <class 'str'>
print(type(last_name))   # Output: <class 'str'>
print(type(full_name))   # Output: <class 'str'>
print(type(country))     # Output: <class 'str'>
print(type(city))        # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(is_married))  # Output: <class 'bool'>
print(type(is_true))     # Output: <class 'bool'>
print(type(is_light_on))  # Output: <class 'bool'>
print(type(skills))      # Output: <class 'list'>
print(type(person_info))  # Output: <class 'dict'>

# Using the len() built-in function, find the length of your first name
print(len(first_name))  # Output: 4

# Compare the length of your first name and your last name
print(len(first_name) == len(last_name))  # Output: False (4 != 6)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print(total)  # Output: 9

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print(diff)  # Output: 1

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print(product)  # Output: 20

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)  # Output: 1.25

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)  # Output: 4

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)  # Output: 625

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)  # Output: 1

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
import math
radius = 30
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
print(area_of_circle)  # Output: 2827.4333882308138
print(circum_of_circle)  # Output: 188.49555921538757

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

# Print the values of the variables
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
