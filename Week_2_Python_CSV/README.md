# Python Challenges

### Overview
Python challenges for classes, OOP, entry points, named tuples, lists, tuples, dictionaries, loops, types, strings, control flow, functions, and LAMBDA methods

### Specifications
1. Install python
2. Set up virtual environment
3. Use python to solve challenge questions

### Python Installation 
1. Python3 - Download the latest version of python from the python site. run: ```brew install python3```. This should also install pip3. To check Python version, run: ```python3 --version```.
2. pip3 - To check if pip3 is already installed, run: ```pip3 --version```. The output should
be similar to pip 22.2.1.

### Virtual Environment Installation
1. Install virtual env package: ```pip3 install virtualenv```
2. Make directory for env: ```mkdir python-virtual-environments && cd python-virtual-environments```
3. Create environment: ```python3 -m venv env```
4. Activate environment: ```source env/bin/activate```. (env) indicates environment is active. 
5. run: ```python3 filename.py``` to print to terminal


### Challenges


#### Lists
1. Create a 10x10 multidimensional array of zeros
2. Iterate over the array to creat a multiplication table
3. For example: the value at multi_table[5][5] the table should be 25
4. Print the table

```
multi_dim = [[0] * 10 for i in range(10)]
for i in range(0,10):
    for j in range(0,10):
        multi_dim[i][j] = (i+1)*(j+1)        
for i in multi_dim:
    print(i)
``` 

1. Write a list comprehension that creates a new list with the square root of each number from the original list.

```
old_list = [9,64,121,81, 169,225, 256, 1337]
new_list = list(map(lambda x: floor(sqrt(x)), old_list))
print(new_list)

new_list = reduce(lambda a,b: a+b, old_list)
print(new_list)
```

1. Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.

```
import sys

sys.setrecursionlimit(3000)


def fib(n, memo = {}):
    if (n in memo): return memo[n]
    if (n <= 2): return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
print(fib(64))

print(sys.getrecursionlimit())
```

#### Tuples
1. Create a dictionary with tuple keys
2. The keys will be the following historical figures
3. The values will be the country they're from
4. Match them to their respective countries in your dictionary keys: ('Vladimir lenin', 'Thomas Jefferson', 'Barack Obama', 'Tsar Nicola'III, 'John Curtin') Values: "Russia", "US", "Australia"
historical_figures = {"Vladimir lenin", "Thomas Jefferson", "Barack Obama", "Tsar Nicola III", "John Curtin"}

```
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
```

#### Dictionaries
1. Use the Cars dictionary example below to create an array of customer dictionaries
2. Loop based on user input and store the inputs as first_name, last_name
3. Print the array of dictionaries when the user exits

```
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
```        


#### Loops
1. The fizz buzz: If a number modulo 3 and 5 is 0, then output fizzbuzz
2. If a number modulo 3 is 0, then output fizz
3. If a number mudulo 5 is 0, then output buzz
4. otherwise output the number

```
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
```        

#### Types
1. Use input() to grab a number value from the user and cast that number to a float.

```
my_input = int(input("Enter a number: "))
new_float = float(my_input)
print(new_float)
```

2. Divide the new float by a number and cast the result into an int

```
result_int = (new_float / 2)
print(int(result_int))
```

3. Use input() to grab the name of a user and print('Hello[name]!')

```
my_name = str(input("Enter your name: "))
print('Hello {}!'.format(my_name))
```

#### Strings
1. Create two strings, f_name & i_name, to store the first and last name of your coach
2. Extract the first character of each string to get their initials and store them as a variable
3. Join the two intials with a period and print the new value.

```
f_name = "Ben"
l_name = "Bruton"
f_initial = f_name[0]
l_initial = l_name[0]
initials = f_initial + "." + l_initial
print(initials)
```


#### Control Flow
1. Create a variable age
2. Write an elif block that indicates which grade a person will go into based upon the age variable
3. print the result with different ages

```
age = int(input("Enter your age: "))
if age < 5:
    print("no school")
elif age >= 18:
    print("18 or older, go to university")
else: 
    print("grade = {} - 5".format(age))
```    

#### Functions
1. Write a function called 'my_first_function'.
2. Your function will take in a string as an argument
3. Your function should print in the following format: 'I love {argument}!'

```
def my_first_function(str_1):
    print("I love " + str_1)
my_first_function("burgers!") 
```   


#### Lambdas
1. You are given the following list: [2, 5, 7 , 32, 100, 9, 56, 74, 97, 22, 13, 80]
2. Use a lambda function to filter out all the even values

```
list_numbers = [2,5,7,32,100,9,56,74,97,22,13,80]
evens = list(filter(lambda x: x % 2 == 0, list_numbers))
odds = list(filter(lambda x: x % 2 != 0, list_numbers))
print(list_numbers)
print(evens)
print(odds)
```

3. Use a lambda map function to multiply all the values by 3

```
modified_list = list(map(lambda x: (x * 3), list_numbers))
print(modified_list)
```

4. Use a lambda function to reduce the list and find the sum of all the values in the list

```
sum1 = reduce(lambda a, b: a + b, list_numbers)
print(sum1)
```

#### Advanced Functions
1. Declare a function called is_palindrome
2. Your function should take in a String and return True/False depending on whether the given String is a palindrome. (Remember built-in String methods)
3. Declare a new function that takes in a list of strings and uses the is_palindrome function to return a list of True/False

```
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
```   

1.  Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.

```
list_string_nums = [6, 90, 56, 57.88, "strings", "booleans"]
nums_only = list(filter(lambda x: isinstance(x, (int, float)), list_string_nums))
print(nums_only)
```

#### Named_Tuples
1. You own a stationery store and you want an app to organise pens
2. Create a namedtuple Pen class with attributes: size(int), inkcolour(string), and beveled(bool)
3. Instantiate three different kinds of pens with different attributes
4. Print your namedtuple class instances in the following format Standard Pen: size = 2, ink = "black", isbeveled = True

```
Pen = namedtuple("Pen", "size, inkcolor, beveled")
small = Pen(2, "Red", False)
medium = Pen(3, "Blue", True)
large = Pen(4, "Black", True)
print(f"Standard Pen: size = {small.size}, ink= {small.inkcolor}, isbeveled = {small.beveled}")
print(f"Standard Pen: size = {medium.size}, ink= {medium.inkcolor}, isbeveled = {medium.beveled}")
print(f"Standard Pen: size = {large.size}, ink= {large.inkcolor}, isbeveled = {large.beveled}")
```

1. You have the following two points: (2,1), (4,7)
2. Instantiate the points as a Point namedtuple class
3. Create a function to calculate the slope based on the two points
4. Print the result in the following format: '(p2.y - p1.y) / (p2.x - p1.x) = slope'

```
Point = namedtuple("Point", ['x', 'y'])
p1 = Point(2, 1)
p2 = Point(4, 7)
print(p1)
print(p2)

def slope(p1, p2):
    return(p2.y - p1.y)/(p2.x - p1.x)
print(f"{slope(p1,p2)} = slope")
```

#### Classes
1. Create a Rectangle class with height and width fields
2. Create getters & setters for the fields. Create a method get_area()
3. Instantiate a rectangle in the main function and print its area

```
class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def height(self):
        print("getter method is called for height")
        return self._height

    @property
    def width(self):
        print("getter method is called for width")
        return self._width

    #setter
    @height.setter
    def height(self, value):
        if value.isdigit():
            print("height was set with the setter")
            self._height = value
        else:
            print("height must be an integer")  

    @width.setter
    def width(self, value):
        if value.isdigit():
            print("width was set with the setter")
            self._width = value
        else:
            print("width must be an integer")    

    #getter
    def get_area(self):
        return int(self._height * self._width)  

new_rectangle = Rectangle(10, 5)   

def main():
    print(new_rectangle._height)
    print(new_rectangle.width)
    print("height = ", new_rectangle.height)
    print("widht = ", new_rectangle.width)
    print("The area of the rectangle is:", new_rectangle.get_area())

if __name__ == "__main__":
    main() 
```    

#### OOP
1. Create a Vehicle parent class with fields and a method
2. Create a Car child class with extra fields and override the parent method
3. Instantiate both in the main function and call their methods

```
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print_car(self):
        print(f"My vehicle is a {self.make} {self.model}") 

class Car(Vehicle): 
    def __init__(self, make, model, color): 

        super().__init__(make, model) 
        self.color = color 
    def this_car(self):
        print(f"My car is a {self.color} {self.make} {self.model}.") 


main_vehicle = Vehicle("Hyndai", "Sonata")
my_car = Car("Tesla", "Model 3", "Blue")

def main():
    print(main_vehicle.make)
    main_vehicle.print_car()
    print(my_car.make)
    my_car.this_car()
   

if __name__ == "__main__":
    main()   
```    




