import array as arr
from math import sqrt, floor, ceil
from functools import reduce

my_nums = [1,2,3,4,5]
print(type(my_nums))

my_nums.insert(1, 7)
print(my_nums)

my_nums.pop(2)
print(my_nums)

print(my_nums[-3::])

my_word = "example string"
print(my_word[-3:-1:])

my_arr = arr.array('i', [1,2,3,4,5])
print(type(my_arr))

fruits = iter(["apple", "banana", "peach", "cherry"])
print(next(fruits))
print(next(fruits))
print(next(fruits))

my_tuple = (1,2,3,4,5)
my_other_tuple = 1,2,3,4,5
print(type(my_other_tuple))

my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)

changing_tuple = ([1,2,3], [4,5,6])
changing_tuple[0].append(4)
print(changing_tuple)

my_tuple = 123, 321, "hello!"
x, y, z = my_tuple
print(x)
print(z)
print(y)

my_dictionary = {
    "first_name": "barack",
    "last_name": "Obama",
    "address": "123 Maint st.", 
}
print("My name is", my_dictionary["first_name"])
print(my_dictionary.keys())
print(my_dictionary.values())

for k, v in my_dictionary.items():
    print(k, v)
    

for i in my_dictionary:
    print(i)

fruits = iter(["apple", "banana", "cherry"])
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        break

fruits = iter(["apple", "banana", "cherry"])
for fruit in fruits:
    if fruit == "cherry":
        print(fruit)
        break  

fruits = iter(["apple", "banana", "cherry"])
for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)  


words = "this is a string"
for letter in words:
    print(letter)    

for n in range (1, 10):
    if n % 2 == 0:
        print(n)

x = 0
while x < 10:
    print(x)
    if x == 5:
        break
    x +=1

x = 0
while x < 10:
    x += 1
    if x == 6:
        continue
    print(x)

#Lists
#1 Create a 10x10 multidimensional array of zeros
#2 Iterate over the array to creat a multiplication table
#3 For example: the value at multi_table[5][5] the table should be 25
#4 Print the table
multi_dim = [[0] * 10 for i in range(10)]
for i in range(0,10):
    for j in range(0,10):
        multi_dim[i][j] = (i+1)*(j+1)        
for i in multi_dim:
    print(i)

#Tuples
#1 Create a dictionary with tuple keys
#2 The keys will be the following historical figures
#3 The values will be the country they're from
#4 Match them to their respective countries in your dictionary keys: ('Vladimir lenin', 'Thomas Jefferson', 'Barack Obama', 'Tsar Nicola'III, 'John Curtin') Values: "Russia", "US", "Australia"
historical_figures = {"Vladimir lenin", "Thomas Jefferson", "Barack Obama", "Tsar Nicola III", "John Curtin"}
a, b, c, d, e = historical_figures
my_dictionary = {
    a: "Russia",
    b: "US",
    c: "US",
    d: "Russia",
    e: "Australia", 
}
# del my_dictionary["John Curtin"]
print(my_dictionary)


#Dictionaries
#Use the Cars dictionary example below to create an array of customer dictionaries
#Loop based on user input and store the inputs as first_name, last_name
#Print the array of dictionaries when the user exits
customers = []
while True:
    user_input = input("Enter another name?: (Yes/No) ")
    user_input = user_input[0].lower()
    if user_input == "n":
        break 
    else:
        first_name, last_name = input("Enter your name (first/last): ").split()
        customers.append({"first name": first_name, "last name": last_name})
    for c in customers:
        print(c["first name"], c["last name"])


#Loops
# The fizz buzz: If a number modulo 3 and 5 is 0, then output fizzbuzz
# If a number modulo 3 is 0, then output fizz
# If a number mudulo 5 is 0, then output buzz
# otherwise output the number
for number in range(51):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    else:
        print(number)

#List
# write a list comprehension that creates a new list with the square root of each number from the original list.
old_list = [9,64,121,81, 169,225, 256, 1337]
new_list = list(map(lambda x: floor(sqrt(x)), old_list))
# print(new_list)
new_list = reduce(lambda a,b: a+b, old_list)
print(new_list)


# ENTRY POINTS
def ran_function():
    print("Hello World!")

print("demo")

if __name__ == "__main__":
    ran_function()


# 1.  Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.
import sys

sys.setrecursionlimit(3000)


def fib(n, memo = {}):
    if (n in memo): return memo[n]
    if (n <= 2): return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
print(fib(64))

print(sys.getrecursionlimit())
