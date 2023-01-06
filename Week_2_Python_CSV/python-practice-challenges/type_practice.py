import math
from math import sqrt as sq
from math import pi as pie
from functools import reduce

sq(25)


# int
num_1 = 5

#float
float_1 = 1.50

#string
str_1 = "this is a string"

bool_1 = True

print(num_1)
print(str_1)
print("Hello World!")
print(type(num_1))
print(type(float_1))
print(float_1 * 50)

new_float = float(num_1)
print(type(new_float))
print(new_float)

a_str = 'hello'
print(a_str[4])

print("life" in "life is but a poor player")

my_str = "hello world!"
for c in my_str:
    print(c)

print(len(my_str))
print(my_str.upper())
print(my_str.replace("hello", "hola"))

print(my_str.capitalize())
my_str_list = my_str.split(" ")
print(my_str_list)

my_str = []
for c in my_str:
    print(c)

x = 5
y = 6
if x == y:
    print("They are equal")
elif x < y:
    print('x is less than')
else:
    print('x is greater')    


is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

x = 3
result = x * 2 + 10 if x % 2 == 0 else x / 2 - 10
print(result)

age = 12 
age_group = "Minor" if age < 18 else "Adult" 


# Types
#1 Use input() to grab a number value from the user and cast that number to a float.
my_input = int(input("Enter a number: "))
new_float = float(my_input)
print(new_float)

#2 Divide the new float by a number and cast the result into an int
result_int = (new_float / 2)
print(int(result_int))


#3 Use input() to grab the name of a user and print('Hello[name]!')
my_name = str(input("Enter your name: "))
print('Hello {}!'.format(my_name))


# Strings
#1 Create two strings, f_name & i_name, to store the first and last name of your coach
#2 Extract the first character of each string to get their initials and store them as a variable
#3 Join the two intials with a period and print the new value.
f_name = "Ben"
l_name = "Bruton"
f_initial = f_name[0]
l_initial = l_name[0]
initials = f_initial + "." + l_initial
print(initials)


#Control Flow
#1 Create a variable age
#2 Write an elif block that indicates which grade a person will go into based upon the age variable
# print the result with different ages
age = int(input("Enter your age: "))
if age < 5:
    print("no school")
elif age >= 18:
    print("18 or older, go to university")
else: 
    print("grade = {} - 5".format(age))



#FUNCTIONS
def example_func():
     print("Helloooooo")
example_func()

def example_func(num_1, num_2):
    return num_1 * num_2
print("25 * 25 is", example_func(25, 25))  

def set_name():
    name = "Val"
    print(name)
set_name() 


def change_name():
    global global_name
    global_name = "Ollie"

global_name = "Rich"
change_name()    
print(global_name)

#LAMBDA
x = lambda a, b, c: a + b - c
print(x(2,2, 5))

def addition(a, b):
    return a + b

# function in a function
def func(n):
    return lambda x: x * n

doubler = func(2)
print(doubler(10))   

tripler = func(3)
print(tripler(10))

def circle_perimeter(radius):
    return 2 * pie * radius
print(circle_perimeter(10))    

another_circle_perimeter = lambda radius: 2 * pie * radius
print(another_circle_perimeter(20))

#Lambda methods
my_list = [2,3,4,5,6,7,8,9,10]

#MAP
modified_list = list(map(lambda x: round(x ** 3.5, 2), my_list))
print(my_list)
print(modified_list)

#FILTER
new_list = range(1, 21)
evens = list(filter(lambda x: x % 2 == 0, new_list))
odds = list(filter(lambda x: x % 2 != 0, new_list))
print(list(new_list))
print(evens)
print(odds)

#REDUCE
new_list = [1,2,3,4,5,6,7,8,9]
new_tuple = (1,2,3,4,5,6,7,8,9)
product_list = list(range(1,10))
sum1 = reduce(lambda a, b: a + b, new_list)
product = reduce(lambda a, b: a * b, list(product_list))
print(sum1)
print(product)


#Args
def my_args(*args):
    for arg in args:
        print(arg)
my_args("This", "is", "the", "first", "argument")

#Kwargs
def my_function(**friend):
    print("My best friends name is {}. He lives at {}".format(friend["name"], friend["address"]))
    print(f"My best friends name is {friend['name']}. He lives at {friend['address']}")
my_function(name = "Joe", address = "123 Main St.")

def keyword_function(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")
keyword_function(firstname = "Herbie", lastname = "Hoover", age = 45, email = "herb.hooves@gmail.com")

def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"My {key} is {value}")
intro(firstname = "Slim", lastname = "Shady", age = 21, number = 1234567890)
intro(firstname = "James", lastname = "Bond", age = 40, email = "james.bond@sas.uk", country = "England")


#FUNCTIONS
# 1. Write a function called 'my_first_function'.
# 2. Your function will take in a string as an argument
# 3. Your function should print in the following format: 'I love {argument}!'
def my_first_function(str_1):
    print("I love " + str_1)
my_first_function("burgers!")    


# Lambdas
# 1. You are given the following list: [2, 5, 7 , 32, 100, 9, 56, 74, 97, 22, 13, 80]
# 2. Use a lambda function to filter out all the even values
list_numbers = [2,5,7,32,100,9,56,74,97,22,13,80]
evens = list(filter(lambda x: x % 2 == 0, list_numbers))
odds = list(filter(lambda x: x % 2 != 0, list_numbers))
print(list_numbers)
print(evens)
print(odds)

#3. Use a lambda map function to multiply all the values by 3
modified_list = list(map(lambda x: (x * 3), list_numbers))
print(modified_list)


#4. Use a lambda function to reduce the list and find the sum of all the values in the list
sum1 = reduce(lambda a, b: a + b, list_numbers)
print(sum1)

# Advanced Functions
#1. Declare a function called is_palindrome
#2. Your function should take in a String and return True/False depending on whether the given String is a palindrome. (Remember built-in String methods)
#3. Declare a new function that takes in a list of strings and uses the is_palindrome function to return a list of True/False
def is_palindrome(str):
    reverse = ''.join(reversed(str))
    if(str == reverse):
        return True
    return False   


str1 = input("Enter the string: ")
palindrome = is_palindrome(str1)
if (palindrome):
    print("True")
else:
    print("False")       

def is_palindrome(palindrome):
    palindrome = palindrome.lower().replace(' ', '')
    return palindrome == palindrome[::-1]
print(is_palindrome("racecar"))    

# 1.  Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.
list_string_nums = [6, 90, 56, 57.88, "strings", "booleans"]
nums_only = list(filter(lambda x: isinstance(x, (int, float)), list_string_nums))
print(nums_only)

# 1.  Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "***********4444"
