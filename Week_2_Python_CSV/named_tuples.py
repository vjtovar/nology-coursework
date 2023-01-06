from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=11, y=22)

print(type(Point))
print(p[0])
print(p[1])

#unpacking
x, y = p
print(x,y)

print(p.x,p.y)

EmployeeRecord = namedtuple("EmployeeRecord", "name, age, title")

emp_rec = EmployeeRecord("Micheal Corleone", 45, "The Godfather")
print(f"{emp_rec.name} is the new {emp_rec.title}")


Parent = namedtuple("Parent", "name children")
vito = Parent("Vito Corleone", ["Sonny", "Michael"])
print(vito.children)

vito.children.append("Fredo")
print(vito.children)

Developer = namedtuple('Developer', "name level language", defaults= ["Junior", "Python"])
dev = Developer("Steve", "Senior")
print(f"{dev.name} is a {dev.level} developer in {dev.language}")

Person = namedtuple("Person", "name age height")
Person._make(["John", 25, 72])
joe_bob = Person("Joe Bob", 30, 72)
print(joe_bob._asdict())

jane = joe_bob._replace(name= "Jane")
print(jane)

ExtendedPerson = namedtuple("ExtendedPerson", [*Person._fields, "weight"])
halfthor = ExtendedPerson("Halfthor", 28, 81, 325)
print(halfthor.weight)

for field, value in zip(halfthor._fields() and zip()):
    print(field, "=", value)

#Pythonic
car = (4, "Gray ", True)
if car[0] == 4 and car[1] == "Gray" and car[2]:
    print("gray sedan selected")
car = namedtuple("Car", "doors color isAvailable")
car = car(4, "Gray", True)

if car.doors == 4 and car.color == "Gray" and car.isAvailable:
    print("Gray Sedan selected")
print(divmod(9,4))    

def custom_divmod(a, b):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(a,b))
print(custom_divmod(9,4))

# Stationary Store
# 1. You own a stationery store and you want an app to organise pens
# 2. Create a namedtuple Pen class with attributes: size(int), inkcolour(string), and beveled(bool)
# 3. Instantiate three different kinds of pens with different attributes
# 4. Print your namedtuple class instances in the following format Standard Pen: size = 2, ink = "black", isbeveled = True
Pen = namedtuple("Pen", "size, inkcolor, beveled")
small = Pen(2, "Red", False)
medium = Pen(3, "Blue", True)
large = Pen(4, "Black", True)
print(f"Standard Pen: size = {small.size}, ink= {small.inkcolor}, isbeveled = {small.beveled}")
print(f"Standard Pen: size = {medium.size}, ink= {medium.inkcolor}, isbeveled = {medium.beveled}")
print(f"Standard Pen: size = {large.size}, ink= {large.inkcolor}, isbeveled = {large.beveled}")


# Slope of a Line
# 1. You have the following two points: (2,1), (4,7)
# 2. Instantiate the points as a Point namedtuple class
# 3. Create a function to calculate the slope based on the two points
# 4. Print the result in the following format: '(p2.y - p1.y) / (p2.x - p1.x) = slope'
Point = namedtuple("Point", ['x', 'y'])
p1 = Point(2, 1)
p2 = Point(4, 7)
print(p1)
print(p2)

def slope(p1, p2):
    return(p2.y - p1.y)/(p2.x - p1.x)
print(f"{slope(p1,p2)} = slope")




    