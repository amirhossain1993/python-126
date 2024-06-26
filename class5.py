# For loop : Even number

'''
for x in range(2,20,2):
    print(x)
'''

# For Loop : Odd Number

'''
for x in range(1,20,2):
    print(x)
'''

# Function : Addion

'''
def add(x, y):
    Z = x + y
    print(Z)
    
add(20, 10)
'''

# Function : Subtraction

'''
def add(x, y):
    Z = x - y
    print(Z)
    
add(30, 10)
'''


### Python Strings

# Strings are Arrays : index number 0 thake count hobee

'''
a = "Hello, World!"
print(a[1])

a = "Hello, World!"
print(a[5])

a = "Hello, World!"
print(a[6])

a = "Hello, World!"
print(a[8])
'''

# Looping Through a String

'''
for x in "banana":
  print(x)
'''

# String Length : Length er counting 1 thake start hoee

'''
a = "Hello, World!"
print(len(a))
'''

# Check String : To check if a certain phrase or character is present in a string, we can use the keyword in. That is true or false condition

'''
txt = "The best things in life are free!"
print("free" in txt)
'''

# Print only if "free" is present:

'''
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
'''

# Check if NOT : To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.That is true or false condition.

'''
txt = "The best things in life are free!"
print("expensive" not in txt)
'''

'''
txt = "The best things in life are free!"
print("life" not in txt)
'''

### Slicing Strings :

# Slicing : Specify the start index and the end index, separated by a colon, to return a part of the string.Get the characters from position 2 to position 5 (not included):

'''
b = "Hello, World!"
print(b[2:5])  # [ 2no index = l and 5no index = (n-1 = 4no index) = o]
'''

'''
b = "Hello, World!"
print(b[:8])   # [initial value is 0, so 0no index = H and 8no index = w]
'''

'''
b = "Hello, World!"
print(b[3:])   # [ 3no index = l and last index nai , so ses porjonto print korbe]
'''

# Negative Indexing:

'''
b = "Hello, World!"
print(b[-5:-2])
'''


### Modify Strings:

# Upper Case:

'''
a = "Hello, World!"
print(a.upper())
'''

# Lower Case:

'''
a = "Hello, World!"
print(a.lower())
'''

# Remove Whitespace: The strip() method removes any whitespace from the beginning or the end:

'''
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
'''

# Replace String: The replace() method replaces a string with another string:

'''
a = "Hello, World!"
print(a.replace("H", "J"))
'''

## String Concatenation: To concatenate, or combine, two strings you can use the + operator.

'''
a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = " World"   # To add a space between them
c = a + b
print(c)


# To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
'''


### String Format: F-Strings

'''
age = 36
txt = f"My name is John, I am {age} years old."
print(txt)


price = 50
txt = f"This book price is {price} taka."
print(txt)
'''

### Escape Character :

'''
txt = 'It\'s alright.'   # \'	Single Quote
print(txt) 


txt = "This will insert one \\ (backslash)."   # \\	Backslash
print(txt)


txt = "Hello\nWorld!"   # \n	New Line
print(txt)


txt = "Hello\rWorld!"   # \r	Carriage Return
print(txt) 


txt = "Hello\tWorld!"    # \t	Tab
print(txt) 


#This example erases one character (backspace):

txt = "Hello \bWorld!"     # \b	Backspace
print(txt) 
'''

### String Methods :

# capitalize() Method:
'''
# The first letter of word will be capitalized / Upper case the first letter in this sentence
txt = "hello, and welcome to my world."
x = txt.capitalize()  
print (x)
'''

# casefold() Method:
'''
# Each letter will be lowercase / Make the string lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()  
print(x)
'''

# center() Method :
'''
# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle
txt = "banana"
x = txt.center(20)
print(x)
'''

# count() Method :
'''
# Return the number of times the value "jackfruit" appears in the string
txt = "I love jackfruits, jackfruit are my favorite fruit and jackfruit is bangladeshi fruit."
x = txt.count("jackfruit")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")   # Return the number of times the value "apple" appears in the string
print(x)
'''

# endswith() Method:
'''
# Check if the string ends with a punctuation sign (.)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

txt = "Hello, welcome to my world"
x = txt.endswith(".")
print(x)
'''

# find() Method:
'''
# Where in the text is the word "welcome"? / At what index does the word start?
txt = "Hello, welcome to my world."

x = txt.find("welcome")
print(x)

x = txt.find("my")
print(x)

x = txt.find("world")
print(x)

x = txt.find("Hello")
print(x)
'''


# format() Method : 
'''
# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format
txt = "For only {price:.2f} taka!"
print(txt.format(price = 49))
'''


# index() Method:
'''
# Where in the text is the word "welcome"? / At what index does the word start?
txt = "Hello, welcome to my world."

x = txt.index("welcome")
print(x)

x = txt.index("Hello")
print(x)

x = txt.index("world")
print(x)

x = txt.index("my")
print(x)
'''


# join() Method:
'''
# Join all items in a tuple into a string, using a hash character as separator
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)
'''


# ljust() Method :
'''
# Return a 20 characters long, left justified version of the word "banana"
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# Return a 10 characters long, left justified version of the word "apple"
txt = "apple"
x = txt.ljust(10)
print(x, "is my favorite fruit.")
'''


# lower() Method :
'''
# Lower case the string
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
'''


# upper() Method :
'''
# Upper case the string
txt = "Hello my frinds"
x = txt.upper()
print(x)
'''


# lstrip() Method :
'''
# Remove spaces to the left of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "     banana"
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "banana    "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = "banana"
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
'''

# partition() Method :
'''
# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match", 
# 2 - the "match", 
# 3 - everything after the "match"]

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "An emotional congregation packed into a Walton church for the last time"
x = txt.partition("packed")
print(x)
'''


# replace() Method :
'''
# Replace the word "bananas"
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
'''

# split() Method :
'''
# Split a string into a list where each word is a list item:

txt = "welcome to the jungle"
x = txt.split()
print(x)  # ['welcome', 'to', 'the', 'jungle']
'''


# plitlines() Method :
'''
# Split a string into a list where each line is a list item:
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)    # ['Thank you for the music', 'Welcome to the jungle']
'''

# strip() Method :
'''
# Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")    # of all fruits banana is my favorite
'''

# title() Method :
'''
# Make the first letter in each word upper case:
txt = "Welcome to my world"
x = txt.title()
print(x)       # Welcome To My World
'''

# zfill() Method :
'''
# Fill the string with zeros until it is 10 characters long
txt = "50"
x = txt.zfill(10)
print(x)            # 0000000050
'''


### Lists type data :
'''
# List items are ordered, changeable, and allow duplicate values.List items are indexed, the first item has index [0], the second item has index [1] etc.

mylist = ["apple", "banana", "cherry","Orange","Jackfruit","Mango","Litchi","Black Berry","Lemon"]
print(mylist[3])

mylist = ["apple", "banana", "cherry","Orange","Jackfruit","Mango","Litchi","Black Berry","Lemon","Watermelon"]
print(mylist[5])
'''


### List Length :
'''
# Print the number of items in the list:
thislist = ["apple", "banana", "cherry","Orange","Jackfruit","Mango","Litchi","Black Berry","Lemon","Watermelon"] 
print(len(thislist))
'''


### List Items - Data Types :
'''
# List items can be of any data type : String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["apple", "banana", "cherry",1, 5, 7, 9, 3,True, False, False]

print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))
'''


### Access List Items :
'''
# Positive Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of positive Indexes : index 0 thake start , so 2no index is "cherry" and 5no index = (n-1)= 4no index is "kiwi" [Note: The search will start at index 2 (included) and end at index 5 (not included)]
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])  # Initial index valu 0 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
'''

'''
positive index    0        1         2         3        4        5        6
              ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
negetive index    -7       -6        -5        -4       -3      -2       -1
'''

'''
# Range of Negative Indexes :
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
'''

'''
# Check if Item Exists :
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''


### Change List Items :
'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"   # 1 is the index number
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]   # 1 & 3 is index number
print(thislist)


# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)   # ['apple', 'blackcurrant', 'watermelon', 'cherry']


# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)      # ['apple', 'watermelon']


# Insert Items : Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)      # ['apple', 'banana', 'watermelon', 'cherry']
'''


### Add List Items :

'''
# Append Items : To add an item to the end of the list, use the append() method

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)    # ['apple', 'banana', 'cherry', 'orange']

# Insert Items : To insert a list item at a specified index, use the insert() method

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)    # ['apple', 'orange', 'banana', 'cherry']


# Extend List : To append elements from another list to the current list, use the extend() method

list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)      # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list2.extend(list1)
print(list2)  
'''


### Remove List Items :

'''
# Remove Specified Item : The remove() method removes the specified item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)    # ['apple', 'cherry']

# If there are more than one item with the specified value, the remove() method removes the first occurrence

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)   # ['apple', 'cherry', 'banana', 'kiwi']


# Remove Specified Index : The pop() method removes the specified index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)   # ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)    # ['apple', 'banana']


# The del (Delet keyword) keyword also removes the specified index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely : Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist


# Clear the List : The clear() method empties the list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
'''


### Loop Lists :

'''
# You can loop through the list items by using a for loop
thislist = ["appel","Banana","Cherry"]
for x in thislist:
  print(x)
'''

'''
# Loop Through the Index Numbers: You can also loop through the list items by referring to their index number.Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
'''

