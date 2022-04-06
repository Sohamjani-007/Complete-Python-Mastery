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


# FUNCTIONS
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


# Handling Exceptions :

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


# CLASSES:
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
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, another):
#         return point.x == another.x and point.y == another.y

#     def __gt__(self, another):
#         return point.x > another.x and point.y > another.y
    
    
#     def __lt__(self, another):
#         return point.x < another.x and point.y < another.y

# point = Point(10, 20)
# another = Point(1, 2)
# print(point == another)
# print(point > another)
# print(point < another)
















