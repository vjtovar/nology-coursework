#Classes and Object oriented programming
#Static instance method
class Person:
    name = "Ben"
    age = 37
    def intro(self):
        print(f"My name is {self.name} and I am {self.age} years old")

ben_person = Person()  
print(ben_person.name)
ben_person.intro()

#Dynamic instance method
class Cat:
    def __init__(self, name = "Boots", breed = "Alley Cat", age = 7):
        self.name = name
        self.breed = breed
        self.age = age
    def meow(self):
        return "{} goes 'MEEEOOOOWWWWW".format(self.name)

zeal = Cat("Zeal", "Street Cat", 2)
ardor = Cat("Ardor", "Street Cat", 2)
boots = Cat()


def main():
    print(zeal.name)
    print(ardor.name)        
    print(boots.name)
    print(zeal.meow())


if __name__ == "__main__":
    main()

#Class method
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18    

person1 = Person("BEN", 37)
person2 = Person.fromBirthYear("Allen", 1982)
person3 = Person.fromBirthYear("Val", 2012)     

def main():
    print(person1.name)
    print(person2.name)
    print(person1.age)
    print(person2.age)
    print(person3.age)
    print(person1.isAdult(person1.age))
    print(person3.isAdult(person3.age))

if __name__ == "__main__":
    main()    

#Getters and Setters
import math                

class Circle:
    def __init__(self, radius = 0):
        self._radius = radius

    @property
    def radius(self):
        print("getter method is called")
        return self._radius 

    #setter
    @radius.setter
    def radius(self, value):
        if value.isdigit():
            print("radius was set with the setter")
            self._radius = value
        else:
            print("radius must be an integer")  

    def get_area(self):
        return pow(int(self._radius), 2) * math.pi               

new_circle = Circle(10)   
user_r = input("Please enter radius: ")
new_circle.radius = user_r       

def main():
    print(new_circle.radius)
    print(new_circle._radius)
    print("radius = ", new_circle.radius)
    print("The area of the circle is:", new_circle.get_area())

if __name__ == "__main__":
    main()   

#Inheritance
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name}") 

class Coach(Person): 
    def __init__(self, first_name, last_name, cohort): 

        super().__init__(first_name, last_name) 
        self.cohort = cohort  
    def welcome(self):
        print(f"Welcome to the {self.cohort}. I am your coach {self.first_name} {self.last_name}") 


ben_person = Person("Ben", "Bruton")
ben_coach = Coach("Benjamin", "Bruton", "ASML")

def main():
    print(ben_person.first_name)
    ben_person.print_name()
    print(ben_coach.first_name)
    ben_coach.welcome()
   

if __name__ == "__main__":
    main()   



#Polymorphism
class Bird:
    def __init__(self, name = ""):
        self.name = name
        
    def flight(self):
        print("There are many kinds of birds. Some birds fly. Some cannot.")
        
class Sparrow(Bird):
    def __init__(self, name):
        super().__init__(name)
        
    def flight(self):
        print(f"A {self.name} can fly.")
        
class Ostrich(Bird):
    def __init__(self, name):
        super().__init__(name)
        
    def flight(self):
        print(f"An {self.name} cannot fly.")
        
bird = Bird()
sparrow = Sparrow("sparrow")
ostrich = Ostrich("ostrich")

def main():
    bird.flight()
    sparrow.flight()
    ostrich.flight()

    
if __name__ == "__main__":
    main()  

# __Str__ & __add__ magic method
class Wallet:
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"   

    def __add__(self, value2):
        return Wallet(self.value + value2.value)       


my_wallet = Wallet(5000)
another_wallet = Wallet(100)
third_wallet = my_wallet +another_wallet
print(another_wallet)
print(my_wallet.value)     
print(third_wallet)  


# Classes
# 1. Create a Rectangle class with height and width fields
# 2. Create getters & setters for the fields. Create a method get_area()
# 3. Instantiate a rectangle in the main function and print its area
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

# OOP
# 1. Create a Vehicle parent class with fields and a method
# 2. Create a Car child class with extra fields and override the parent method
# 3. Instantiate both in the main function and call their methods
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
