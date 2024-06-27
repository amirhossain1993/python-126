### Tuples : Note: ()

'''
# Nite: Unchangeable (Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.)

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))
'''

'''
# Allow Duplicates:Since tuples are indexed, they can have items with the same value
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
'''

'''
# Tuple Length: To determine how many items a tuple has, use the len() function
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
'''

'''
# Create Tuple With One Item : To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
'''

'''
# Tuple Items - Data Types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("aple", "banana", "cherry", 1, 2, 3, 4, 5,True, False, False)

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))
'''

'''
# Change Tuple Values: Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

a = ("apple", "banana", "cherry")
print(type(a))

b = list(a)
print(type(b))

b[1] = "kiwi"
a = tuple(b)
print(type(a))

print(a)



x = ('apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya')
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
'''

'''
# Add Items : Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.Convert the tuple into a list, add "orange", and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)      # ('apple', 'banana', 'cherry', 'orange')
'''


'''
# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)    # ('apple', 'banana', 'cherry', 'orange')
'''


'''
# Remove Items : Note: You cannot remove items in a tuple. uples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)     # ('banana', 'cherry')
'''


### Access Tuple Items :

'''
# Positive Index :You can access tuple items by referring to the index number, inside square brackets
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])        # banana
'''

'''
# Negetive Index : Negative indexing means start from the end. [-1 refers to the last item, -2 refers to the second last item etc.]

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])     # cherry
'''


'''
# Range of Indexes : You can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new tuple with the specified items.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])     # ('cherry', 'orange', 'kiwi')
'''


'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])     # ('apple', 'banana', 'cherry', 'orange')


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])    # ('cherry', 'orange', 'kiwi', 'melon', 'mango')
'''


'''
# Range of Negative Indexes:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])   # ('orange', 'kiwi', 'melon')
'''


'''
# Check if Item Exists: To determine if a specified item is present in a tuple use the in keyword

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
'''


### Unpack Tuples:

'''
# Python, we are also allowed to extract the values back into variables. This is called "unpacking".Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
'''


'''
# Using Asterisk* : If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
'''


### Loop Tuples: 

'''
# You can loop through the tuple items by using a for loop

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
'''



'''
# Loop Through the Index Numbers: Use the range() and len() functions to create a suitable iterable

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
'''


'''
# Using a While Loop : 

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
'''


### Join Tuples:

'''
# Join Two Tuples: 

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)    # ('a', 'b', 'c', 1, 2, 3)
'''


'''
# Multiply Tuples: If you want to multiply the content of a tuple a given number of times, you can use the * operator

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)      # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
'''



## Tuple count() Method:

'''
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)      # 2
'''


## Tuple index() Method: 

'''
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)      # 3
'''



### Sets:   Note : {} 

'''
# Set items are unchangeable, but you can remove items and add new items

thisset = {"apple", "banana", "cherry"}
print(thisset)
'''



'''
# Duplicates Not Allowed:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)    # {'banana', 'apple', 'cherry'}
'''


'''
# The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
'''


'''
# The values False and 0 are considered the same value in sets, and are treated as duplicates

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)    # {'cherry', False, True, 'apple', 'banana'}
'''


'''
# Length of a Set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
'''


'''
# Data Types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"apple", "banana", "cherry",1, 5, 7, 9, 3,True, False, False}

print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))
'''



### Python Collections (Arrays):
'''
There are four collection data types in the Python programming language:

1. List is a collection which is ordered and changeable. Allows duplicate members. []
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members. {}
4. Dictionary is a collection which is ordered** and changeable. No duplicate members. {}
'''


## Access Items:

'''
# You cannot access items in a set by referring to an index or a key.But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
'''


'''
# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
'''


'''
# Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
'''


## Add Set Items:

'''
# Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
'''



'''
# Add Sets: To add items from another set into the current set, use the update() method

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
'''


'''
# Add Any Iterable: The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
'''



## Remove Set Items:

'''
# Remove Item: To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
'''


## Loop Sets:


'''
# Loop Items: You can loop through the set items by using a for loop

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
'''



## Join Sets:

'''
# Join Sets:
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)     # {'c', 1, 2, 3, 'a', 'b'}
'''


'''
# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)    # {1, 2, 'a', 3, 'c', 'b'}
'''


'''
# Join Multiple Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)    # {1, 2, 3, 'cherry', 'apple', 'John', 'bananas', 'c', 'a', 'b', 'Elena'}
'''


'''
# When using the | operator, separate the sets with more | operators

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)    # {'a', 1, 2, 3, 'b', 'c', 'John', 'apple', 'cherry', 'bananas', 'Elena'}
'''


'''
# Join a Set and a Tuple : The union() method allows you to join a set with other data types, like lists or tuples

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)    # {1, 2, 3, 'c', 'a', 'b'}
'''


'''
# Update: 

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)   # {3, 'c', 1, 2, 'a', 'b'}
'''


'''
# Intersection : Keep ONLY the duplicates. The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)    # {'apple'}
'''


'''
# You can use the & operator instead of the intersection() method, and you will get the same result
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
'''














