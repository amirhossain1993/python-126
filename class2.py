# Brackets name
"""
() = Parentheses or Round Bracket
{} = Braces or Curly Brackets
[] = Square Brackets or Box Brackets
"""





#git initprint("Hello, World!")         

"""
This is comment
This is comment
This is comment
This is comment
This is comment
This is comment
"""

#print("Hello, world!")




# x is number and y is name
#x = 5
#y = "Abdullah Al Ahnaf"
#print(x)
#print(y)






# variable changing valu
#x = 5
#y = 5000
#z = 500
#p = 4500
#print(x + y)
#print(x + y + z)
#print(x + y +z + p)

#x = 5
#y = 5000
#z = 500
#p = 4500
#name = 'Jamal'      # string variable single quotation
#name1 = "Kamal"     # string variable double quotation
#name2 = "'Rokon'"   # string variable triple quotation but ata use kora uchit noee

#print(x + y , name)          # print er some ee string variable name comma (,) diee likte hoee
#print(x + y + z , name1)
#print(x + y +z + p , name2)


# aki variable ee akadhi valu use kora jaee and variable ter type ber korarr upaee [print(type(variable name))]
#name5 = "Jamal" , "Kamal"
#print(name5)
#print(type(name5))





#Legal variable names:
# variable use korar somee related name use kora dorka/projon jano variable name dhakhe buja jaee ata ki nirdess kora hoise
"""
myvar = "John"        # sobgulo small letter 
my_var = "Kamal"      # majhe underscore (_)
_my_var = "Jakir"     # prothom e and majkhane o underscore (_)
myVar = "Jibon"       # prothom e small letter and pore capital letter
MYVAR = "Nazrul"      # sobgulo capital letter
myvar2 = "Masud"      # sobgulo small letter er pore number
MYVAR3 = "Al-Amin"    # sobgulo capital letter er pore number
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print(MYVAR3)

"""





#Illegal variable names:
"""
2myvar = "John"     # prothom ee number use kora jabe na
my-var = "John"     # majkhane e high-pan (-) use kora jabe na
my var = "John"     # majkhane e space ( ) use kora jabe na 

print(my var)
"""


#Multipal variable
#x, y, z = "Orange" , "Mango" , "Banana"
#print(x)
#print(y)
#print(z)





#Local Variable: Function er bahiererr variable ti function er bahire are use kora jai nee and function use korarr somee (def) use korte hoee
"""
x = "Awesome"

def myfunc():
    
    x = "Fantastic"
    print(" Python is " + x)
    
myfunc()

print(" Python is " + x)

"""


# Function er bahire global variable use korle ta print hoee na , ata local variable hesabiee kaj kore
"""
global x
x = "Awesome"

def myfunc():
    
    x = "Fantastic"
    print(" Python is " + x)
    
myfunc()

print(" Python is " + x)
"""


#Function er vitore global variable use korle ta print hoee  , ata tokhon global variable hesabiee kaj kore

"""
x = "Awesome"

def myfunc():
    global x
    x = "Fantastic"
    print(" Python is " + x)
    
myfunc()

print(" Python is " + x)
"""


#Global Variable: Function er bahiererr variable ti function er bahire are use kora gasee
"""
def myfunc():
    global x
    x = "Fantastic"
        
myfunc()

print(" Python is " + x)
"""


#Data Type
"""
a = "Hello World"	                            # str	
b = 20	                                        # int	
c = 20.5	                                    # float	
d = 1j	                                        # complex	
f = ["apple", "banana", "cherry"]	            # list	
j = ("apple", "banana", "cherry")	            # tuple	
k = range(6)	                                # range	
l = {"name" : "John", "age" : 36}	            # dict	
m = {"apple", "banana", "cherry"}	            # set	
n = frozenset({"apple", "banana", "cherry"})	# frozenset	
o = True	                                    # bool	
p = b"Hello"	                                # bytes	
q = bytearray(5)	                            # bytearray	
r = memoryview(bytes(5))	                    # memoryview	
s = None	                                    # NoneType

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

print(f)
print(type(f))

print(j)
print(type(j))

print(k)
print(type(k))

print(l)
print(type(l))

print(m)
print(type(m))

print(n)
print(type(n))

print(o)
print(type(o))

print(p)
print(type(p))

print(q)
print(type(q))

print(s)
print(type(s))

"""



