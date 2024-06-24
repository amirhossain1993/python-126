'''
# The Largest Value :

num1= 10
num2= 20
num3= 15
if num1 >= num2 and num1 >= num3:
    larges = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
    
print("The Largest Number is :", largest)
'''


### Using Loops (while and for)
'''
i = 1
while i <10:
    print(i, "I Love Bangladesh")
    i +=1
'''
'''
i = 1
while i <10:
    print(i, "Abdullah Al Ahnaf")
    i += 2
'''


'''
# Even And Odd Number Using while loop home work

i = 1
while i < 10:
    print(i)
    i += 2     # Odd Number
    

i = 2
while i < 10:
    print(i)
    i += 2     # Even Number
'''



# break and continue command

'''
i = 1
while i < 10:
    print(i)
    if i == 7:
        break    # i er valu 7 asa matroi break kore dise
    i += 1
'''

'''
i = 0
while i < 10:
    i += 1
    if i == 7:
        continue   # i er valu 7 , continue syntex ti 7 ke bad diee onno sokol valu print korbe
    print(i)
'''



# else Statement
'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")   
'''


###  For Loops is very usefull loops for django

'''
# Print each fruit in a area list:

areas = ["Mirpur-1","Mirpur-2","Mirpur-10","Postogola","Jatrabari","Sympur"]
for x in areas:
    print(x)
'''

# For loop: Looping Through a String [Loop through the letters in the word "banana":]

'''
for y in "banana":
    print(y)
'''

'''
for x in "I am happy":
    print(x)
'''

# For loop: The break Statement (Exit the loop when x is "orange":)

'''
fruits = ["banana","apple","mango", "orange","watermelon","jackfruit","lychee"]
for x in fruits:
    print(x)
    if x == "orange":
        break   # "orange" aser por break hobe , er porer fruits gulo print hobe na [print syntex ti if condition er age ase]
'''

# For loops: Exit the loop when x is "banana", but this time the break comes before the print:

'''
fruits = ["banana","apple","mango", "orange","watermelon","jackfruit","lychee"]
for x in fruits:
    if x == "orange":
        break  # "orange" er agge porjonto print korce [ print syntex ti break er pore]
    print(x)   
'''


# For Loops: The continue Statement [Do not print banana:]

'''
fruits = ["banana","apple","mango", "orange","watermelon","jackfruit","lychee"]
for x in fruits:
    if x == "orange":
        continue   #"orange" bade sobgulo print hobe , [if x == "orange"]
    print(x) 
'''

# For loops : The range() Function

'''
for x in range(10):
    print(x)   # 0 to 9 porjonto print korbe [range(10)]
'''

# For loops : The range() Function : Using the start parameter:

'''
for x in range(2,8):
    print(x)
'''   
    
# For loops : The range() Function : Increment the sequence with 3 (default is 1):

'''
for x in range(2,40,4):
    print(x)   # 1st vali is starting value, 2nd valu is ending value, 3rd valu is increment value
'''

# Else in For Loop : Print all numbers from 0 to 5, and print a message when the loop has ended:

'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")    
'''

# Else in For Loop : Break the loop when x is 3, and see what happens with the else block:

'''
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
'''

# Nested Loops : Print each adjective for every fruit: loop er vetore loop

'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''

# For loop : The pass Statement [for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.]

'''
for x in [0, 1, 2]:
  pass
'''


# Python Functions: function syntex or function key word "def" = define function full meaning 

'''
# Creating a Function
def my_function():
  print("Hello from a function")
  
# Calling a Function

def my_function():
  print("Hello from a function")

my_function()
'''

'''
def my_function():
    print("Welcome Our New Website")
    
my_function()
'''

'''
def home():
    print("Welcome to our new House")
    
home()
'''

'''
def add(x , y):
    z = x + y
    print(z)
    
add(5 , 8)
add(10 , 35)
add(100 , 200)
'''

# Python Functions: Arguments : 

'''
def my_document(name):
  print("Enter your" + name)

my_document(" First Name:")
my_document(" Last Name:")
my_document(" Email:")
my_document(" Phone Number:")
'''


### Python Casting / Type Casting :

'''
# Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
# w = int ("Hellow World")   # it is not woked, because truth universal values

print(type(x))
print(type(y))
print(type(z))
print(type(w))
'''

'''
#Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(type(x))
print(type(y))
print(type(z))
print (type(w))
'''

'''
#Strings: [note: Any number can be type changed, but no string type massage can be type changed]

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
# w = int ("Hellow World")   # it is not woked, because truth universal values

print(type(x))
print(type(y))
print(type(z))
print(type(W))
'''


### Python String Formatting : F-Strings : f-strings (formatted string literals) are a way to embed expressions inside string literals in Python, using curly braces {}. They provide an easy and readable way to format strings dynamically. 

'''
price = 59
txt = f"The price is {price} taka"    # price = 56 int value ti txt string vlaue er modhee automatically aner jonno f-string use kora hocee
print(txt)
'''







