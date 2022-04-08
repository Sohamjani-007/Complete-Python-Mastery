# PYTHON NOTES BY SOHAM.J





## CONTROL FLOW:
# LOOPS - Iterables
# for num in range(1,20,3):
#     print('Attempt', num, (num + 1) * ".")
# --------------------------------
# for x in range(5):
#     for y in range(3):
#         print(f"{x}, {y}")
# --------------------------------
# command = ""
# while command.lower() and command != "QUIT":
#     command = input(">" )
#     print("ECHO:", command)
# --------------------------------
# count = 0
# for num in range(1,10,1):
#     if num % 2 == 0: # This is because 2 // 2 = 0. Remaninder of all 2,4,6,8.
#         count += 1
#         print(num)
# print(f"We have total of {count} even numbers")







## FUNCTIONS
# def greet(first_name, last_name): #first_name and last_name are parameters
#     print(f"Hi {first_name} {last_name}")
# greet("Soham", "Jani") # Soham Jani here is an argument



# Keyword Arguments(*args)
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# multiply(2, 3, 4, 8)


# (**args) = For key pair values in dict
# def user_name(**user):
#     return(user["name"])

# user_name(name="Soham", num=1)

# Scope Global and Local variables.
# ex1
# def greet(name):
#     message = "a" = local variable in def
# greet("Soham")

# ex2
# message = "a"
# def greet(name):
#     global message
#     message = "b"
# greet("Soham")
# print(message)



# FIZZBUZZ
# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         return("FizzBuzz")
#     elif input % 3 == 0:
#         return("Fuzz")
#     elif input % 5 == 0:
#         return("Buzz")
#     else:
#         return("NO FIZZBUZZ")
# print(fizz_buzz(7))









## DATA STRUCTURES:

# LISTS = [list() function]
# letters = ["a", "b", "c"]
# matrix = [[0,1], [2,3]]
# zeros = [0] * 10
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("hello world")
# print(len(chars), zeros, matrix, combined, numbers, chars)
# EX2)
# numbers = list(range(20))
# print(numbers[::2], numbers[::-1])
# EX3)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first, second, *others, last = numbers # = LIST UNPACKING.
# print(others, last)
# EX4)
# letters = ["a", "b", "c"]
# items = ["0", "1"]
# index, letter = items # Here, letter and index both go to the loop i.e for index, letter in letters.
# for index, letter in enumerate(letters): # here, enumerate unpacks the tuple and iterate it.
#     print(index, letter)
# EX5)
# letters = ["a", "b", "c", "d"]
# Add
# letters.append("e")
# Remove
# letters.pop(0)
# letters.remove("b")
# del letters[0:2]
# letters.clear()
# print(letters)
# EX6)
# finding_items = ["a", "b", "c", "d"] # FINDING ITEMS
# print(finding_items.count("e"))
# if "e" in finding_items:
#     print(finding_items.index("e"))
# EX7)
# sorting = [1, 32, 21, 14]  # SORTING LISTS
# sorting.sort(reverse=True)
# print(sorting)
# --------------

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 11),
#     ("Product3", 13),
# ]

# def sort_item(item):
#     return item[1] # Because the items are tuple, we are returning the item[1] ie 10,9,11 ie its price.
# items.sort(key=sort_item)
# print(items)
# OR
# items.sort(key=lambda item:item[1]) # (key=lambda paramter:expression) 
# print(items)
# OR
# prices = list(map(lambda item: item[1], items))
# print(prices)
# ---#OR-------------------
# filtered = list(filter(lambda item: item[1] >= 10, items)) # FILTERED PRICES
# filtered = [item for item in items if item[1] >= 10] # FILTERED WITH LIST COMPREHENDED
# print(filtered)
# ---#OR-------------------
# [expression for item in items] # This is called # LIST COMPREHENSION
# prices = [item[1] for item in items]
# print(prices)



# HOW TO ZIP
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(list(zip("abc", list1, list2))) # Because zip creates object therefore it also needs to put it in a list.



# STACKS
# LIFO, append, pop, [-1], and Falsy value to True.
# browsing_session = []
# browsing_session.append(1)
# browsing_session.pop()
# if not browsing_session: # To check if the stack is empty or not (FALSY : TO STOP THE ERROR ON LAST PAGE)
#     browsing_session[-1]  (LAST PAGE)



# QUEUE.
# FIFO works here.
# from collections import deque
# queue =  deque([]) # What if, there is a list of 1000 items, we cannot FIFO there, thats why we need deque.
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue: # That means we have no items in list.
#     print("empty")



# TUPLES - [tuple() function] + Tuple doesn't have a tuple comprehension ## READ GENERATOR EXPRESSION.
# point = (1, 2, 3)
# print(point[0:2])
# x, y, z = point
# if 10 in point:
#     print("exists")
# point[0] = 10



# Swapping in easy way.
# x = 10
# y = 11
# x, y = y, x # here y, x is a tuple which unpacks the x, y on left side.
# # a, b = 1, 2 # here 1, 2 is a tuple which unpacks the a, b on left side.
# print(y)



# Arrays - Use when there is a large number of sequence list.
# from array import array
# numbers = array("i", [1, 2, 3]) # Here, "i" is a typecode which indicates the type of list.
# numbers[0] = 1.0 # this cannot be added into a list cause its floating type not a int.



# SETS -[set() function]- A collect with no duplicates.
# numbers = [1, 1, 2, 3, 4]
# first = set(numbers) # Here you made a set by removes the duplicate and then made a union in next step.
# second = {1, 5}
# print(first | second) # This gives a union of both sets.
# print(first & second) # This gives a comman of both sets. 
# print(first - second) # This simple subtracts the value.
# print(first ^ second) # This removes the same value from both.
# # A set does not support indexing.But you can check by condition.
# if 1 in first:
#     print("Yes")
# numbers = [1, 1, 2, 3, 4]
# for x in numbers:
#     print(x - 2)
    #OR
# values = [(x - 2) for x in numbers] # SET COMPREHENSION
# print(values)



# DICTIONARY -[dict() function]- {Key:Value} pairs. Like a phonebook = [name => contact].
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))
# del point["x"]
# print(point)
# for key in point:
#     print(key, point[key])
#     #OR
# for x in point.items(): # This gives a tuple therefore change the x to (key, value)
#     print(x)
#     #OR
# for key, value in point.items():
#     print(key, value)
# DICTIONARY COMPREHENSION - [expression for item in items] 
# values = {}
# for x in range(5):
#     print(x * 2)
# values = {(x * 2) for x in range(5)} # DICTIONARY COMPREHENSION
# values = {x: x * 2 for x in range(5)} # KEY:VALUE = x: x*2
# print(values)



# GENERATOR EXPRESSIONS
# from sys import getsizeof
# values = (x * 2 for x in range(100000)) # Here, inspite of comrehensioning a tuple we produced Generator Expression.
# print(getsizeof(values)) # It stores large volume of values in short memory therefore it doesn't suit the len() function.



# UNPACKING OPERATOR.
# values = [1, 2, 3, 4]
# print(*values) # Whenever there is a asterix mark as show the list is unpacked automatically in output.
# EX2)
# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)
# EX3)- UNPACKING IN DICTIONARY.
# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = {**first, **second, "z": 1}
# print(combined) - # NOTE - the x value is changed because if you have multiple items with same key, the last value will be used.


# EXCERCISE- TO FIND THE MOST REPEATED CHARACTER IN THE TEXT.
####*********  VERY IMPORTANT **********########
# from array import array

# sentence = "This is a common interview question"
# char_frequency ={}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# char_frequency_sorted = sorted(
#     char_frequency.items(), 
#     key=lambda kv:kv[1], 
#     reverse=True)

# print(char_frequency_sorted[0])









##  Handling Exceptions :

# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) :
#     print("Please enter a valid number")  
# else:                                       # This else is just like (FOR ELSE)
#     print("Expression continues")
# finally:                                    # finally clause is always executed and used to release external resources. eg: DATABASE CONNECTION, NETWORK CONNECTION etc. 
#     file.close()

    #OR
        
# try:
#     with open("app.py") as file:            # Here, {with} is doing the same work as finally, releases external resources.
#     print("Opened)
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) :
#     print("Please enter a valid number")  
# else:                                       # This else is just like (FOR ELSE)
#     print("Expression continues")




# RAISING EXCEPTIONS:

# def calculator_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0") # We raised a ValueError.     
#     else:
#         return 10 / age
# try:
#     calculator_xfactor(-1)
# except ValueError as error:
#     print("error")


# IS RAISING EXCEPTIONS A GOOD PRACTISE? Lets find out by a test below.
# TEST 1 - CODE 1
# from timeit import timeit

# code1 = """
# def calculator_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0")      
#     else:
#         return 10 / age
# try:
#     calculator_xfactor(-1)
# except ValueError as error:
#    pass                                       # pass is asentence that doesnt do anything.
# """


#     # AND 

# code2 = """
# def calculator_xfactor(age):
#     if age <= 0:
#         return None     
#         return 10 / age

#     calculator_xfactor(-1)
#     if xfactor == None:
#         pass
# """
# print("TEST-1:", timeit(code1, number=10000))
# print("TEST-2:", timeit(code2, number=10000))

# RESULTS - If you are building a simple application for few users then raising few exception wont affect the performance.
#           but if are building performance application then its better to use exception when its necessary. 









## CLASSES:
# class Point:
#     def draw(self):
#         print("draw")

# point = Point()
# print(type(point))
# print(isinstance(point, Point))



# CONSTRUCTOR: - special method
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point {self.x}, {self.y}")

# point = Point(1, 2)
# point.draw()



# CLASS VS INSTANCE ATTRIBUTE:
# class Point:
#     default_color = "red"
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point {self.x}, {self.y}")

# Point.default_color = "yellow"

# point = Point(1, 2)
# print(point.default_color)
# point.draw()

# another = Point(3, 4)
# print(Point.default_color)
# another.draw()



# CLASS VS INSTANCE METHOD:
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod 
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#             print(f"Point {self.x}, {self.y}")

# point = Point.zero()
# point.draw()



# MAGIC_METHODS: search for python 3 magic methods on Google.
## __init__
## __str__ 
#____THIS ARE THE TWO USEFUL MAGIC METHODS____
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         return f"({self.x}, {self.y})"

#     @classmethod 
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#             print(f"Point {self.x}, {self.y}")

# point = Point.zero()
# print(point)



# COMPARING OBJECTS:
# class Point:
#     def __init__(self, x, y):                                 # Constructor than magicmethod
#         self.x = x
#         self.y = y
    
#     def __eq__(self, another):
#         return point.x == another.x and point.y == another.y  # equal than magicmethod

#     def __gt__(self, another):
#         return point.x > another.x and point.y > another.y    # greater than magicmethod
     
#     def __lt__(self, another):
#         return point.x < another.x and point.y < another.y    # Less than magicmethod
    
#     def __add__(self, another):                               # Arithematic than magicmethod
#         return point.x + another.x, point.y + another.y

# point = Point(10, 20)
# another = Point(1, 2)
# print(point == another)
# print(point > another)
# print(point < another)
# combined = point + another
# print(combined)



# Making Custom Containers:

# class TagCloud:
#     def __init__(self):
#         self.__tags = {} 

#     def add(self, __tags):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):                                      # get 
#         return self.__tags.get(tag.lower(), 0)
    
#     def __setitem__(self, tag, count):                               # set
#         self.__tags[tag.lower()] = count

#     def __len__(self):                                               # len(cloud) - for tghe length
#         return len(self.__tags)

#     def __iter__(self):                                              # iter(cloud) - for iteration 
#         return iter(self.__tags)

# cloud = TagCloud() # setting variable of class
# cloud["python"] = 10 # get
# print(cloud.__tags) # private member
# len(cloud) # len
# iter(cloud) # iter
# cloud.add("Soham")
# cloud.add("soham")
# cloud.add("soham")
# print(cloud.__tags) # add
# print(cloud.__tags["PYTHON"]) #private members - using double underscores eg. __tags we have a private membership.
# print(cloud.__dict__) 


# PROPERTIES:- Looks like a regular attribute outside, but internally it reads getter and setter.  
# class Product:
#     def __init__(self, price):
#         self.price= price                     # here we set the price attribute
    
#     @property                                 
#     def price(self):
#         return self.__price
    
#     @price.setter                             # if @price.setter is commented out then it doesnt set the and change the value of the attribute.                                     
#     def price(self, value):                   # and therefore a Attribute error is throw
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value
    
# ##  price = property(get_price, set_price) - instead of this line to call a property object, we put the @property on top of get_price.

# product = Product(-10)
# # product.price = -10
# print(product.price)

# INHERITANCE.
# class Animal(object):                         # Animal: Parent, Base.
#     def __init__(self):
#         self.age = 1
    
#     def eat(self):
#        print("eat")

# class Mammal(Animal):                         # Mammal: Child, sub.
#     def walk(self):
#         self.walk = "walk"
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         self.swim = "swim"
#         print("swim")

# m = Mammal()
# m.eat()
# print(m.age)                                 
# print(isinstance(m, object))                 # isinstance = compares the point-object to Base class.
# o = object()                                 # Object class is the Base class of all Class.
# issubclass(Mammal, Animal)                   # issubclass = compares the subclass to its Base class.
# issubclass(Mammal, object)



# METHOD OVERRIDING: 
# class Animal(object):                         
#     def __init__(self):
#         print("Animal Constructor Called")
#         self.age = 1
    
#     def eat(self):
#        print("eat")

# class Mammal(Animal):
#     def __init__(self):                       # Whenever a new method is places in subclass, the Baseclass method stoped working = Method Overriding.
#         super().__init__()                      # a super() inbuild function solves the overriding to get access to Base. So, super() + .__init__() method
#         print("Mammal Constructor Called")     
#         self.weight = 20
                            
#     def walk(self):
#         self.walk = "walk"
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         self.swim = "swim"
#         print("swim")

# m = Mammal()
# m.eat()
# print(m.age) 
# print(m.weight)                              # AttributeError: 'Mammal' object has no attribute 'age' = Because of Method Overiding.                             
# print(isinstance(m, object))                 
# o = object()                                  
# issubclass(Mammal, Animal)                   
# issubclass(Mammal, object)



# MULTI-LEVEL INHERITANCE.
# example - ANIMAL(object) (def eat) --> BIRDS(ANIMAL) (def fly)--> CHICKEN(BIRDS) but a chicken cannot fly, so here its a problem of understanding too many Inheritance.
# NOTE - ALWAYS KEEP THE INHERITANCES LESS SAME GOES FOR MULTIPLE INHERITANCE.


# MULTIPLE INHERITANCE.
# # example1
# class Employee():
#     def greet(self):
#         print("Hello Employee")

# class Person():
#     def greet(self):
#         print("Hello Person")

# class Manager(Employee, Person):       # MULTIPLE INHERITANCE - here Employee is first in order therefore Hello Employee will be the output.
#     pass                               # If the ordering i.e (Person, Employee) is changed then the program works differently.

# manager = Manager()
# manager.greet()

# # SO WHY DOES PYTHON HAVE MULTIPLE INHERITANCE ? 
# # example2
# class Flyer:
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# class FlyingFish(Flyer, Swimmer):       # Here, a good example of multiple inheritance.
#     pass


# A GOOD EXAMPLE OF INHRITANCE:
# ----------------------------------------------------------
# class InvalidOperationError(Exception):
#     pass

# class Stream:
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False
 
# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")
# ---------------------------------------------------------------

# ABSTRACT BASE CLASSES:
# from abc import ABC, abstractclassmethod

# class InvalidOperationError(Exception):
#     pass

# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False

#     @abstractclassmethod              # Abstract provides common interface across different kind of Stream.
#     def read(self):                   # For example this will indicate to (def read) all across the Streams the same. 
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from memory stream")

# stream = MemoryStream()
# stream.open()



# POLYMORPHISM:
# from abc import ABC, abstractclassmethod


# class UIControl(ABC):
#     @abstractclassmethod
#     def draw(self):
#         pass

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox")

# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDownList")

# def draw(controls):                                # In this example, the draw func is talking many different form = Polymorphism.
#     for control in controls:                       # It simple iterates and calls the draw method, of each control object.
#         control.draw()
                                          

# ddl = DropDownList()
# txt = TextBox()
# draw([ddl, txt])




# DUCKTYPING: - In this case, it only looks for the existence of draw method.

# class TextBox:
#     def draw(self):
#         print("TextBox")

# class DropDownList:
#     def draw(self):
#         print("DropDownList")

# def draw(controls):                                
#     for control in controls:                       # It simple iterates and calls the draw method, of each control object.
#         control.draw()                             # draw method - Python assumes its a UI control.
                                          

# ddl = DropDownList()
# txt = TextBox()
# draw([ddl, txt])




# BUILD-IN TYPES:
# class Text(str):                                     # str Class is a build-in type class and gives all the additional feature.
#     def duplicate(self):
#         return self + self                           # self + self concatinating a string with itself.
    
# text = Text("SOHAM")                                 # Text("Soham") == Text(str)
# print(text.duplicate())                              # Output => SohamSoham


# class TrackableList(list):                           
#     def append(self, object):                        # Overriding
#         print("Append Called")                       # This is like login append message. If user appends something.
#         return super().append(object)                # Due to super() we are just appending here and not replacing.

# track = TrackableList()
# track.append("1")




# DATA CLASSES - Helps when there is no behaviour, no methods but only have data. USE NAMED TUPLE.
# from collections import namedtuple


# Point = namedtuple("Point", ["x", "y"])                 # Point (on the left) represents same like a class. ("Point" = name, ["x", "y"]=atributes)
# p1 = Point(x=1, y=2)
# print(p1.x)
# p2 = Point(x=1, y=2)
# print(p1 == p2)









## MODULES: 
# from sales import calc_shipping, calc_tax                # (Press Crl + Space) to know the functions or modules. 
# from sales import *                                      # Do not put asteris it is a bad practise It overides all.       
# import sales

# calc_shipping()
# calc_tax()
# sales.calc_shipping



# COMPILED PYTHON FILES: pycache file creation.



# MODULE SEARCH PATH :
# import sales
# import sys

# print(sys.path)



# PACKAGES: Is a container for one or more modules i.e PACKAGE -> DIRECTORY -> MODULES.
# import ecommerce.sales                # Approch 1
# from ecommerce.sales import calc_tax  # Approch 2
# from ecommerce import sales           # Approch 3


# ecommerce.sales.calc_tax()            # Approch 1
# calc_tax()                            # Approch 2
# sales.calc_shipping                   # Approch 3




# SUB-PACKAGES: DICRECTORY INTO DICRECTORY 
# from ecommerce.shopping import sales



# INTRA-PACKAGE REFERENCES: SUB-DICRECTORY 
# from ecommerce.customer import contact          # ABSOLUTE IMPORT EXAMPLE:
# from ..customer import contact                  # RELATED IMPORT EXAMPLE: (Look at sales.py)

# contact.contact_customer()




# THE DIR FUCNTION: - USED FOR DEBUGGING WHEN WORKING ON A LARGE PROJECT.
# from ecommerce.shopping import sales

# # print(dir(sales))
# print(sales.__file__)
# print(sales.__name__)
# print(sales.__package__)



# EXECUTING MODULES AS SCRIPTS:-                 # LOOK (sales.py) for reference.
# from ecommerce.shopping import sales








## PYTHON STANDARD LIBRARY:                     # This section can always be refered. No need to memorise anything.

# WORKING WITH PATHS:                           # (search for pathlib on Google)
# from pathlib import Path

# path = Path("ecommerce/__init__.py")          # EXAMPLES:
# path.__exists__()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.py")
# print(path)
# path = path.with_suffix(".txt")
# print(path)



# WORKING WITH DIRECTORIES:
# from pathlib import Path

# path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
# for p in path.iterdir():                      # iterdir - helps to iterate through 1000 of files.
#     print(p)
# paths = [p for p in path.iterdir()]           # In List Comprehension.
# print(paths)




# WORKING WITH FILES:
# from pathlib import Path
# from time import ctime
# import shutil

# path = Path("ecommerce/__init__.py")
# source = Path("ecommerce/__init__.py")
# target = Path() / "__init__.py"

# shutil.copy(source, target)

# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))

# with open("__init__.py", "r") as file:
#     ...

# print(path.read_text())
# path.write_bytes()
# path.write_text("...")




# WORKING WITH ZIP FILES:
# from pathlib import Path
# from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("ecommerce").rglob("*.*"):
#         zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size)
#     print(info.compress_size)
#     zip.extractall("extract")



# WORKING WITH CSV(COMA SEPARATED VALUE) FILES:
# import csv

## TO WRITE
# with open ("data.csv", "w") as file:      
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "production_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])


# ## TO READ
# with open ("data.csv") as file:
#     reader = csv.reader(file)
#     ##print(list(reader))
#     for row in reader:
#         print(row)
    

# SOON TO BE UPDATED------------------------------->