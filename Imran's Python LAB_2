# While Loop Example
counter = 0  
while counter < 5:  
    print(counter)  
    counter += 1  
print()

# Factorial Program 
print("Factorial Program")
user_number = int(input("Enter a positive number: "))
factorial = 1
while user_number >= 1:
    factorial *= user_number
    user_number -= 1
print("Factorial:", factorial)
print()

# For Loop Examples

# 1. List iteration
colors = ["red", "yellow", "blue", "red", "white"]
for color in colors:
    print(color)
print()

# 2. Tuple iteration
fruits = ("apple", "mango", "banana", "kiwi", "tomato")
for fruit in fruits:
    print(fruit)
print()

# 3. String iteration
person_name = "Hassan Bhutta"
for char in person_name:
    print(char)
print()

# For loop using range() with a list
for idx in range(len(colors)):
    print(f"{colors[idx]} \t colors[{idx}]")
print()

# Range Examples

# 1. Single parameter: range(end)
for num in range(5):
    print(num)
print()

# 2. Two parameters: range(start, end)
for num in range(2, 5):
    print(num)
print()

# 3. Three parameters: range(start, end, step)
for num in range(1, 10, 2):
    print(num)
print()

# Loop Control Statements

# Break statement
for num in range(1, 10):
    print(num)
    if num == 5:
        break
print()

# Continue statement
words = ["I", "Am", "Hassan", "Bhutta"]
for word in words:
    if word == "Hassan":
        continue
    print(word)

# Functions

# Basic function definition and call
def displayName():
    print("I am Hassan Bhutta")

displayName()
print()

# Function with string parameters
def showFullName(first, last):
    print(f"Your full name is {first} {last}.")

showFullName("Ali", "Akbar")
showFullName("Ahsan", "Alahi")
showFullName("Daud", "Rasheed")
print()

# Function with integer parameters
def addNumbers(a, b):
    print(a + b)

addNumbers(10, 20)
addNumbers(5, -10)
print()

# Function with list parameter
def calculateListSum(data_list):
    total = 0
    for i in range(len(data_list)):
        total += data_list[i]
    print("Sum =", total)

calculateListSum([10, 20, 30, 40])
calculateListSum([-1, 1, 0, 3, 4])
calculateListSum([1 + 2j, 2 + 5j])
print()

# Function with default parameter
def showCountry(name="Pakistan"):
    print("Your country is", name)

showCountry("India")
showCountry("Australia")
showCountry()
print()

# Function with return statement
def searchValue(search_list, target):
    for i in range(len(search_list)):
        if search_list[i] == target:
            return i
    return -1

values = [5, 10, 15, 0, 12, "1"]
result_index = searchValue(values, 1)
if result_index == -1:
    print("Not Found")
else:
    print("Found at index", result_index)
print()

# Keyword Arguments 
def printThirdNumber(first, second, third):
    print("Third number =", third)

printThirdNumber(third=-1, second=5, first=100)
printThirdNumber(third=1000, second=75, first=2)
print()

# Variable Number of Arguments
def multiplyValues(*args):
    result = 1
    for val in args:
        result *= val
    print("Product =", result)

multiplyValues(10, 5)
multiplyValues(1, 2, 12)
multiplyValues(5, 4, 0)
multiplyValues(10, "* ")
print()

# Classes

# Basic class with class variable
class SampleClass:
    value = 5

instance1 = SampleClass()
print(instance1.value)

# Constructor (__init__) example
class Person:
    def __init__(self, name, age):  # corrected to __init__
        self.name = name
        self.age = age

person1 = Person("Ahmed", 19)
person2 = Person("Fahad", 20)
print(person1.name, person1.age)
print(person2.name, person2.age)

# Class with method
class Person:
    def __init__(self, name, age):  # corrected to __init__
        self.name = name
        self.age = age

    def displayPersonName(self):
        print("Person name is", self.name)

individual = Person("Fahad", 19)
individual.displayPersonName()
