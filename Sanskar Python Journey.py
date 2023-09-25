#!/usr/bin/env python
# coding: utf-8

# # STARTING OF PYTHON JOURNEY

# In[ ]:


name='sanskar'
print(name)


# # HOW TO PRINT

# In[ ]:


print("ne")


# In[ ]:


print("india","america",sep='/')


# In[ ]:


print("hello")
print("world")


# In[ ]:


print("hello",end='')
print(5)


# In[ ]:


print("india","sanskar","america",5,7,6,6,7,6)


# In[ ]:


print("hello","sanskar",end='',sep='/')
print("world")


# In[ ]:


print(4)


# In[ ]:


print(1e307)


# In[ ]:


#complex
print(4+5j)


# In[ ]:


print([1,3,4,53,252,3,3532,])


# In[ ]:


#tuple
print((1,2,43,424,234,2,5432,))


# In[ ]:


#sets
print({1,3242,234,2,41,43,111,31,4})


# In[ ]:


''#dict
print({"Name":"Nitish","age":"45","gender":"male"})


# In[ ]:


#c
#int a=5


# In[ ]:


age='4'
print(age)


# In[ ]:


print("sanskar")


# In[ ]:


print("vinayak")


# In[ ]:


name2='sanskargupta'


# In[ ]:


print(name2)


# In[ ]:


#Dynamic Typing No need to Specify Data type
#Static Typing Need to Declare Data type

#Dynamic Binding  #Python is not binded to data type for variable
#Static Binding


# # Special Syntax

# In[ ]:


a = 'sanskarr';b='gupta';c='rohit'
print(a)
print(b)
print(c)


# In[ ]:


a,b,c =4,5,6
print(a)


# In[ ]:


a=b=c=6
print(a)
print(b)
print(c)


# In[ ]:


# Never use keyboards as varibales like if (else etc.
# Pyhton is a case Sensitive programming language.)


# In[ ]:


import keyword
print(keyword.kwlist)


# INDENTIFIERS - A python identifier is a name  used  to identify a variable , function  class , module  or other object.

# In[ ]:


_="NISTISH"
print(_)


# TAKING INPUT

# In[ ]:


input()


# In[ ]:


input(prompt="apna naam bata")


# # First Program for Sum of two numbers.

# Cause of String is Universal Format.

# In[ ]:


first_num = input("Enter the first number")
second_num= input("Enter the second number")
print(first_num)
print(second_num)
result=first_num+second_num
print(result)


# In[ ]:


# TO CHECK TYPE OF SOMETHING
type([1,24,352,52,5235])


# In[ ]:


type(first_num)


# In[ ]:


first_num


# WIll USE TYPE CONVERSION FOR THIS TO CHANGE ONE DATA TYPE TO DIFFERENT DATA TYPE

# In[ ]:


#Imlicit (AUTOMATICALLY DO TYPE CONVERSION)
a=4+5.6
b=4+6+7
print(a)
print(b)


# In[ ]:


#explicit TYPE CONVERSION NOT PERMANT OPERATION TO CHANGE ITS IN VARIABLE 
first_num+second_num


# In[ ]:


# int
a=int(4.5)
b=int('75')
print(a)
print(b)


# In[ ]:


str(5)


# In[ ]:


bool(1)


# In[ ]:


complex(2)


# In[ ]:


list('HELLO')


# In[ ]:


first_num = input("Enter the first number")
second_num= input("Enter the second number")
print(first_num)
print(second_num)
result=int(first_num)+int(second_num)
print(result)


# OR

# In[ ]:


first_num = int(input("Enter the first number"))
second_num= int(input("Enter the second number"))
print(first_num)
print(second_num)
result=first_num+second_num
print(result)


# # LITERALS

# In[ ]:


# Literal is a raw data given in a variable.
# 1. NUMERIC LITERALS 
# 2. STRING LITERALS
# 3.BOOLEAN LITERALS
# 4.SPECIAL LITERALS


# In[ ]:


# STRING LITERALS 
Multiline_str ="""This is a multiline string with more than one line code"""
raw_str = r"raw \n string"
unicode = u"\U0001F600\U0001F606\U0001F923"
print(Multiline_str)
print(raw_str)
print(unicode)


# In[ ]:


# BOOLEAN LITERALS
a= True+4
b=False+10
print("a:",a)
print("b:",b)


# In[ ]:


# SPECIAL LITERAL
a=None
print(a)


# # OPERATORS

# In[ ]:


x=5
y=5
print(x+y)


# In[ ]:


print(x**y) #Modulus


# In[ ]:


print(x // 2) #Interger Division


# In[ ]:


print(x==y) #Comparison Operator


# In[ ]:


# Logical Operators
x= True
y= False
print(x or y)


# In[ ]:


print(x and y)


# In[ ]:


print(not y) #Y is not true.


# In[ ]:


#BITWISE  CONVERTING INTO BIANRY
x=4
y=6
print(x & y) #AND OPERATOR


# In[ ]:


print(x | y ) #OR OPERATOR


# In[ ]:


print(x >>2)
print(y<<5)
print(~x)


# In[ ]:


#ASSIGNMENT OPERATOR
a += 4
#a =a+3
print(a)


# In[ ]:


a -= 4
print(a)


# #INDENTIY OPERATOR

# In[ ]:


a=3
b=4
print(a is b)


# In[ ]:


a=3,6
b=3,6
print(a is not b)


# In[ ]:


x="Delhi"
print("D" not in x)


# In[ ]:


x =(1,432,5,2,343,324,34,14,32)
print(4 in x)


# # IF ELSE FIRST PROGRAM

# In[ ]:


A = "sanskargupta966@gmail.com"
B = "9713492857"
Email = input("Enter your Email")
Password = input("Enter your password")
if Email == A and Password == B:
    print("welcome")
else:
    print("Invalid Credentials")


# In[ ]:


A = "sanskargupta966@gmail.com"
B = "9713492857"
Email = input("Enter your Email")
Password = input("Enter your password")
if Email == A and Password == B:
    print("welcome")
else:
    print("Invalid Credentials")


# In[ ]:


A = "sanskargupta966@gmail.com"
B = "9713492857"
Email = input("Enter your Email")
if '@' in Email:
    Password = input("Enter your password")
    if Email == A and Password == B:   
        print("welcome")
    elif Email == A and Password != B:
            print ("password incorrect")
            Password = input("Enter your Password again")
            if Password == B:
                 print("Finally Correct")
            else:
                print("Still Incorrect")
    else:
            print("InvalidCredentials")
else:
    print("Email is Invalid")


# #LOOPS
# Flipkart Containers Example
# while
# for
# In[ ]:


# while condition:
#     code


# In[ ]:


number =int (input("Enter the number"))
i = 1
while i<11:
    print(number,"*",i,"=", number * i)
    i+=1


# # Making A Guessing Game

# In[ ]:


import random
count=1
random.randint(1,100)
jackpot=random.randint(1,100)
Guess = int (input("chal guess kar"))
while (Guess != jackpot):
        if Guess < jackpot:
            print("Guess Higher")
        else:
            print("Guess Lower")
        Guess =int (input("Chal Dubara guess kar"))
        count +=1
print("badiya Sahi jawab",jackpot)
print("you took",count,"attempts")


# # FOR LOOP

# In[ ]:


#range function (Start, end, step)
range(1,11)


# In[ ]:


list(range(1,11))


# In[ ]:


range(5)


# In[ ]:


list(range(1,12,3))


# In[ ]:


list(range(10,0,-1))


# In[ ]:


#sequence
#string
for i in range(2,13):
    print(i)


# In[ ]:


for i in range(5,100,5):
    print(i)


# In[ ]:


for i in "kolkata":
    print(i)


# In[ ]:


for i in [1,2,4,5]:
    print(i)


# In[ ]:


for i in(1,23,34,2523,5):
    print(i)


# In[ ]:


for i in {1,34,235,24,5433,4254}:
    print(i)


# #NESTED LOOP

# In[ ]:


#*
#**
#***
#****
#*****
#******


# In[ ]:


Rows=int(input("Enter the Rows to Execute"))
for i in range(1,Rows+1):
    for j in range(0 , i):
        print("*",end= " ")
    print(" ")


# # BREAK CONTINUE AND PASS

# In[ ]:


for i in range (1,11):
    if i==5:
        break
    print(i)


# In[ ]:


# To check if the product is in or stock or not if its in then display otherwise skip.
for i in range(1,7):
    if i == 5:
        continue
    print(i)
    print("Hello")


# In[ ]:


# TO Store a loop in  a NUTSHELL
for i in range(1,11):
    pass
# Just Skip this loop


# # BUILT-IN-FUNCTIONS

# In[ ]:


print("Hello World")


# In[ ]:


input("Enter your Name") #String Format


# In[ ]:


a = True
type(a)


# In[ ]:


int(5.6) #float,str,list,tuple


# In[ ]:


abs(-4) #Modulus Function


# In[ ]:


pow(2,-3) #Power Function


# In[ ]:


min([1,24,5,3,32,5,21,342,25,23,13,21,23,34])#Min


# In[ ]:


max("kolkata") #Ascai Value Max


# In[ ]:


c=22/7
round(c,2) #To Reduce Decimal Digits Round Function


# In[ ]:


divmod(5,2)#Div Mod Function for Division and Modulus at once


# In[ ]:


bin(5) #bin/oct/hex


# In[ ]:


a=3
id(a)#id TO know the Allocated Memory address for the Variable.


# In[ ]:


ord('A') # ord Returns the unicode code point for a one-character String or Ascee Value


# In[ ]:


len("Kolkata") # Determine the Length of iterable


# In[ ]:


sum([1,2,3,34,3,4,34,34]) # Sum


# In[ ]:


help('sum') # help


# # BUILT-IN-MODULES

# In[ ]:


# Modules is Similar to Code Library.
# Modules is nothing but a pyhton file which contain functions inside it we can
# import it and can use it functions for the reusability


# In[ ]:


# Math Module
import math
math.pi


# In[ ]:


math.e


# In[ ]:


math.factorial(5)


# In[ ]:


math.ceil(4.5)


# In[ ]:


math.floor(6.9)


# In[ ]:


# random
import random
random.randint(4,400)


# In[ ]:


a =[1,2,34,5,4,525434,24,3,24,]
random.shuffle(a)
a


# In[ ]:


# time
import time
time.time() #timestamp of Seconds of this Year.


# In[ ]:


time.ctime()
#Current time


# In[ ]:


print('hello')
time.sleep(5)
print('world')


# In[ ]:


import os
os.getcwd()


# In[ ]:


# os.listdir()


# In[ ]:


# STRINGS


# In[ ]:


# How to Create String
c="Its raining outside"
print(c)


# In[ ]:


c = str("sanskar")
c


# #  Accessing Substrings From a String (How to Extra Small String from a String)

# In[ ]:


#Concept of Indexing
c ="hello"
print(c)
print(c[4])


# In[ ]:


#Types of Indexing
#Positive Indexing (0 to 5) for hello
#Negative Indexing (-1 to -5) for reverse of hello
print(c[-4])


# In[ ]:


# Slicing To Extract multiple characters from a String at once.
c ="Hello world"
print(c[0:5])


# In[ ]:


print(c[2:])


# In[ ]:


print(c[:4])


# In[ ]:


print(c[1:10:2]) #using steps to skipping the characters


# In[ ]:


print(c[::-1])


# In[ ]:


c="Hello"
print(c)


# c[0]='X' #Strings are immutable Data Types and you can not edit them.

# In[ ]:


c='world'
del c


# In[ ]:


print(c)


# # Won't be delete cause strings are immutable.

# In[ ]:


c='hello'
print(c)
del (c[0])


# # Operations On Strings
# 

# ARITHMETIC OPERATORS

# In[ ]:


#String Concatination
"hello"+"World"
'Helloworld'


# In[ ]:


#Multiply the String
print("*"*50)


# Relational Operator

# In[ ]:


"Hello"=="World"


# In[ ]:


"Hello" != "world"


# In[ ]:


"Mumbai" > "Pune"
# Comparing by Lexiographically means by Dictionary


# In[ ]:


"Kol" < "kol"
#Capital Letters Comes First So they are Small


# In[ ]:


"hello" and "world"
# Empty String " " = False  Non Empty String " wreghr" = True


# In[ ]:


"  " and " world"


# In[ ]:


" " or " world "


# In[ ]:


" hello" or " world"


# In[ ]:


" hello" and " world"


# In[ ]:


not "hello"


# In[ ]:


not ""


# Loops on Strings

# In[ ]:


c= "hello world"
for i in c[2:7:2]:
    print(i)


# In[ ]:


c= "hello world"
for i in c[::-2]:
    print(i)


# Membership Operations

# In[ ]:


'h' in c


# In[ ]:


'H' in c


# # Common Functions

# Len
# max
# min 
# sorted

# In[ ]:


c ="kolkata"
print(c)
len(c)


# In[ ]:


max(c)


# In[ ]:


min(a)


# In[ ]:


sorted(c)


# In[ ]:


sorted(c,reverse=True)


# # Captialize / Title / Upper / Lower / Swapcase

# In[ ]:


c="sanskar gupta Jhon"
c.capitalize()


# In[ ]:


c.title()


# In[ ]:


c.upper()


# In[ ]:


c.lower()


# In[ ]:


"kOLkata".swapcase()


# # Count

# In[ ]:


c.count("s")


# # Find/Index

# In[ ]:


"its raining today".find("g")


# In[ ]:


c.index("s") # Error if Something is not Present


# # Endswith/Startwith

# In[ ]:


"its raining today".endswith("today")


# In[ ]:


"its raining today".startswith("its")


# # Format

# In[ ]:


"hello my name is {} and i am a {}".format("sanskar","coder")


# In[ ]:


"hello my name is {1} and i am a {0}".format("sanskar","coder")


# In[ ]:


"hello my name is {Profession} and i am a {Name}".format(Name="sanskar",Profession="coder")


# # isalnum / isalpha / isdecimal / isdigit / isidentifier

# In[ ]:


c="sanskar"
c.isalnum()


# In[ ]:


c="@anskar"
c.isalnum()


# In[ ]:


"1ansu".isalpha()


# In[ ]:


"20".isdigit()


# In[ ]:


"20.2".isdecimal()


# In[ ]:


"hello_world".isidentifier()


# # Split

# In[ ]:


"hello is the prime minister of india".split()


# In[ ]:


"hello is the prime minister of india".split("of")


# # Join

# In[ ]:


"-".join(['who','is','am'])


# # Replace

# In[ ]:


"My name is Sanskar".replace("Sanskar","gupta")


# # Strip

# In[ ]:


name ="     sanskar              "
name.strip()


# # LISTS AND ARRAY

# #Arrays are homogenous lists are hetrogenous

# # Creating a List

# In[ ]:


l=["1,2,4,5,6,4"]  #Homogenous list


# In[ ]:


l=["sanskar",32,53,"gupta"] #Hertogenous list


# In[ ]:


#Multidimensional list
#2D
l3=[1,24,3,54,3[4,36,3,4,]]

l4=[[[2,43],[3,5]],[[35,56],[355,64]]]


# In[ ]:


l5=list("haldia")
l5


# # Access items from a list

# In[ ]:


l=[12,34,2,34,235,32]
l[4]


# In[ ]:


l[4:7:1]


# In[ ]:


l[::-1]


# In[ ]:


# With MultiDimensional list
l5=[[13,25,24],2,3,[2,4],2,[4,5,3]]
l5[0]


# In[ ]:


t=l5[-3]
t[1]
l5[-3][0]


# In[ ]:


l5[0][2]


# In[ ]:


z=l5[0]
z[2]


# In[ ]:


l5[0][1]


# In[ ]:


l5[-1]


# In[ ]:


x=l5[-1]
x[0]


# In[ ]:


l5[-3]


# In[ ]:


y=l5[-3]
y[1]


# In[ ]:


l5[-1][2]


# In[ ]:


l5[-3][1]


# In[ ]:


#3D List
l7=[[[24,43],[34,35,34]],[[6,65],[25,43],[657,34]]]


# In[ ]:


l7[1][0]


# In[ ]:


l7[0][0][0]


# # Edit in List

# #List in python are mutable

# In[ ]:


l=[1,43,1234,23]
l[0]=100
l


# In[ ]:


l[-2]=500
l


# In[ ]:


l[1:4]=[200,200,200]
l


# # Add in List

# In[ ]:


#append
l=[2,34,532,25,35]
l.append(1000)


# In[ ]:


l


# In[ ]:


l.extend([500,600,700])
l


# In[ ]:


l.append([5,6])
l


# In[ ]:


l.extend("goa")
l


# In[ ]:


l.insert(1,"workd")
l


# # How to Delete in lists

# In[ ]:


l2=[1,14,1,42,42,]
l2


# In[ ]:


del(l2)


# In[ ]:


l


# In[ ]:


del(l[0])


# In[ ]:


l


# In[ ]:


del l[5]


# In[ ]:


l


# In[ ]:


del l[-4]


# In[ ]:


l


# In[ ]:


del l[-4:]


# In[ ]:


l


# In[ ]:


l.remove("workd")


# In[ ]:


l


# In[ ]:


l.pop()


# In[ ]:


l


# In[ ]:


l.clear()


# In[ ]:


l


# # Operations

# In[ ]:


L9=[1,4,5,4,6,4]
L1=[345,34,234,2,4]
L9+L1 #By Concatination


# In[ ]:


L1*3


# In[ ]:


for i in L1:
    print(i)


# In[ ]:


4 in L1


# # Functions

# In[ ]:


len(L1)


# In[ ]:


min(L1)


# In[ ]:


max(L1)


# In[ ]:


sorted(L1)


# In[ ]:


sorted(L1,reverse=True) #Not a Permanent opereation


# In[ ]:


L1


# In[ ]:


L1.sort(reverse=True)
L1


# In[ ]:


L1


# In[ ]:


L1.sort() 


# In[ ]:


L1


# In[ ]:


L1.index(4)


# In[ ]:


"How are You".title()


# # Problem - Changing Sentence into title without using title()

# In[ ]:


sample="sanskar gupta is coder."
#Split changes strings into lists to extract one particular word.
print(sample.split())


# In[ ]:


L1=[]
for i in sample.split():
    L1.append(i.capitalize())
print(" ".join(L1)) #Change list to String.


# In[ ]:


sample1="sanskargupta@gmail.com"
print(sample1[:sample1.find("@")]) #Slicing


# In[ ]:


sample="sanskargupa@gmail.com"
a=sample.find("@")
print(sample[0:a])


# In[ ]:


email=input().split("@")
print(email)


# In[ ]:


string="sanskargupta999@mail.com"
for i in range(0,len(string)):
    if(string[i]=="@"):
        break
    else:
            print(string[i], end="")


# In[ ]:


A=[1,1,2,2,3,3,4,4]
B=[]
for i in A:
    if(i==B[]):
        break
    else:
            print(A[i])


# In[ ]:


A=[1,1,2,2,3,3,4,4]
B=[1,12,24,32,12,34,32,34,342]
C=[]
for i in B:
      if i not in C:
        C.append(i)
print(C)
    
    


# # Tuples

# In[ ]:


# Tuples are Read Only Data Types.


# In[ ]:


T1=()
T1


# In[ ]:


t2=(234,24,1,3423)


# In[ ]:


t2


# In[ ]:


t3=("Hello",234,234,1,41,341,1,1)
t3


# In[ ]:


#2D Tuples
t4=(1,234,12,42,[234,252,3234,24])
t4


# In[ ]:


t5=(1)
t5


# In[ ]:


type(t5)


# In[ ]:


# To Create a Single item Tuple


# In[ ]:


t6=("hello",)
t6


# In[ ]:


type(t6)


# In[ ]:


t7=tuple("Goa",)
t7


# In[ ]:


t8=tuple([1,342,4,2,234])
t8


# In[ ]:


#Access items from Tuples


# In[ ]:


t2


# In[ ]:


t2[0]


# In[ ]:


t2[:2]


# # Edit

# In[ ]:


l=[1,2,4,5]
l[0]=100
l
# But Tuples Does not Support item assignment cause tuples are just like Strings(Immutable). 


# In[ ]:


l1=(1,24,4,24,23,2,23,23)
del l1


# In[ ]:


l1


# # Sets

# In[ ]:


# Sets do not allow duplicates.
# Sets have no indexing.
# Sets don't allow mutable data types.
# Sets itself is a mutable data type.


# In[ ]:


# Creating a Set
S1={}
S1


# In[ ]:


type(S1)


# In[ ]:


S1 =set()
S1


# In[ ]:


type(S1)


# In[ ]:


S1={1,12,4,2134}
S1


# In[ ]:


S2={"Hello",4.5,34242,23,4,True}


# In[ ]:


S2


# In[ ]:


type(S2)


# In[ ]:


S3={3,35,2,3235,32,342,3,432,3,3,3}
S3


# In[ ]:


S4={[1,34,32],"hello"}
#will show error cause its containing list which is Mutable and Sets Can not have mutable data types.


# In[ ]:


S4={(1,234,123,13,1,3),"hello"}


# In[ ]:


type(S4)


# In[ ]:


S4 #Sets have no indexing its use Hasing.
#You can not create 2D 3D OR 4D Sets.


# # Access Items From Sets

# In[ ]:


#You can not Edit Sets but can add items.
s2={2,3,100,5,4,6,7}


# In[ ]:


s2.add(7)


# In[ ]:


s2


# In[ ]:


s1={343,2,5,2,2,5,42,5}


# In[ ]:


s1


# In[ ]:


s1.remove(343)


# In[ ]:


s1


# In[ ]:


s1.pop()


# # Operations

# In[ ]:


# you can not Concatinate ,Multiply in Sets


# In[ ]:


s1


# In[ ]:


s2


# In[ ]:


s1.union(s2)


# In[ ]:


s1.intersection(s2)


# In[ ]:


s1.difference(s2)


# In[ ]:


s2.difference(s1)


# In[ ]:


s1.symmetric_difference(s2)


# In[ ]:


s1.isdisjoint(s2)


# In[ ]:


s1.issubset(s2)


# In[ ]:


s1.issuperset(s2)


# In[ ]:


s1.clear()


# In[ ]:


s1


# # Dictionary

# In[ ]:


A ={"Name":"Sanskar","Age":"21"}


# In[ ]:


print(A)


# In[ ]:


# Dictionary has no indexing
# Dictionary is a mutable types
# Keys -> immutable , value -> they can be mutable
# Keys should be unique


# In[ ]:


# Mutable -> lists/Sets/Dictionary
# Immutable -> Strings/tuples/int/float/boolean/complex


# In[ ]:


# Create A Dictionary
D={}
D


# In[ ]:


D3={"Name":"Sanskar","Age":"21","Marks":{"M1":99,"M2":98,"M3":97}}


# In[ ]:


D3


# # Accessing Items From a Dictionary

# In[ ]:


A


# In[ ]:


A["Name"]


# In[ ]:


D3["Marks"]["M3"]


# # Edit

# In[ ]:


A["Name"]="Gupta"


# In[ ]:


A


# In[ ]:


D.get("Name")


# In[ ]:


D3["Marks"]["M4"]=96


# In[ ]:


D3


# # Delete

# In[ ]:


del A["Name"]


# In[ ]:


A


# In[ ]:


A.clear()


# In[ ]:


A


# # Operation

# In[ ]:


# In Dictionary concatination and Multiplication does'nt work.


# In[ ]:


for i in D3:
    print(i)


# In[ ]:


for i in D3:
    print(i,D3[i])


# In[ ]:


"Rohit" in D3


# In[ ]:


"Sanskar" in D3


# In[ ]:


"Name" in D3


# In[ ]:


D3.Keys()


# In[ ]:


# Python Calls variable as name


# # Mutability / Garbage Collection / Variable Referencing

# # Variable Referencing
# Aliasing
# In[ ]:


a=5
b=a
id(a)


# In[ ]:


id(b)


# In[ ]:


c=b
id(c)


# In[ ]:


del a #you are not deleting the value you are just deleting the reference of the variable


# In[ ]:


id(b)


# In[ ]:


b


# In[ ]:


c


# In[ ]:


del b


# In[ ]:


c


# In[ ]:


a=5
b=a
a


# In[ ]:


a=6
b


# Referecnce Counting

# In[ ]:


import sys
a="corona"
b=a
c=b
id(a)


# In[ ]:


a


# In[ ]:


sys.getrefcount(a)


# In[ ]:


t="wrwrew"
x=t
y=x

y


# In[ ]:


sys.getrefcoun(t)


# # Garbage Collection

# In[ ]:


# Garbage Collector free up the memory by checking if there is any value
# on which no varibale is referencing.


# #Wierd Stuff
# 1.Getrefcount anomaly
# 2.-5 to 256
# 3.Strings

# In[ ]:


a=2
b=a
c=b
sys.getrefcount(a)


# In[ ]:


a=717
b=a
c=b
sys.getrefcount(a)


# In[ ]:


# -5 to 256 value the id will be the same and apart from this the id will
# be different.


# In[ ]:


a="haldia"
b="haldia"
id(a)


# In[ ]:


id(b)


# In[ ]:


a="haldi inst tech"
b="haldi inst tech"
id(a) #Cause Space is not the Valid identifier in this String thats why its
# creating different identifier


# In[ ]:


id(b)


# In[ ]:


a="haldi_inst_tech"
b="haldi_inst_tech"
id(a)


# In[ ]:


id(b)


# # Mutability

# In[ ]:


# Some things About list


# In[ ]:


L=[1,2,3]
id(L)


# In[ ]:


id(1)


# In[ ]:


id(L[0])


# In[ ]:


id(2)


# In[ ]:


id(3)


# In[ ]:


L[2]=1
L


# In[ ]:


id(L[2])


# In[ ]:


# Mutability refers to the ability to change or edit data in it's memory
# location direclty with out changing its address if address id is changed
# then that is immutability.
# Immutable Data Types - String, Int, Float,Bool,Complex, Tuple
# Mutable Data Types - List , Dictionary , Sets


# In[ ]:


a='hello'
id(a)


# In[ ]:


a=a+'hello'
a


# In[ ]:


id(a)


# In[ ]:


T=[1,2,4,5]


# In[ ]:


id(T)


# In[ ]:


T=T+[45,35,3]
T


# In[ ]:


id(T)


# In[ ]:


L=[1,2,3] # Mutable data type


# In[ ]:


id(L)


# In[ ]:


L.append(4)


# In[ ]:


L


# In[ ]:


id(L)


#  Side Effects of Mutation

# In[ ]:


L=[1,2,3] # Mutable data type


# In[ ]:


L1=L


# In[ ]:


L1


# In[ ]:


L


# In[ ]:


id(L)


# In[ ]:


id(L1)


# In[ ]:


L1.append(4) 


# In[ ]:


L1


# In[ ]:


id(L1)


# # Clonning To avoid Edit in Same Referencing Variable by Mistake.

# In[ ]:


L1 = L[:]
id(L)


# In[ ]:


id(L)


# In[ ]:


id(L1)


# In[ ]:


L1.append(5)


# In[ ]:


L1


# In[ ]:


a = (1,2,3,[4,5])
a


# In[ ]:


a[-1][-1]=500


# In[ ]:


a


# In[ ]:


a = [1,2,3,(4,5)]
a[-1][-1]=500


# In[ ]:


a=[1,3]
b=[3,4]

c=(a,b)
c


# In[ ]:


id(a)


# In[ ]:


id(b)


# In[ ]:


id(c)


# In[ ]:


c[0][0] = 100


# In[ ]:


c


# In[ ]:


id(a)


# In[ ]:


id(c)


# In[ ]:


c


# In[ ]:


L =[1,2,3]
id(L)


# In[ ]:


L=L+[4,5]
L


# In[ ]:


id(l) #Id Changes for Concationation in Lists.


# In[ ]:


c[0] =c[0]+[5.6]


# In[ ]:


c


# # Functions

# In[ ]:


#Abstraction And Decomoposition


# In[ ]:


def is_even(i):
    """Input: i, a positive int
    Returns True if i is even, otherwise Falese
    """
    print ("inside is _even")
    return i%2 == 0


# # Creating a function which tells the given no. is odd or even.

# In[ ]:


def is_even(number):
    """
    This function tells if a given number is odd or even
    input - any valid integer
    output - odd /even
    Created By - Sanskar Gupta
    Last edited - 09 Sep 2023
    """
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


# In[ ]:


To Call the Created Function


# In[ ]:


for i in range(4,8):
    print(is_even(i))


# In[ ]:


print(is_even.__doc__) 


# In[ ]:


type.__doc__ 


# In[ ]:


def is_even(i):
    """
    
    This function tells if a given number is odd or even
    input - any valid integer
    output - odd /even
    Created By - Sanskar Gupta
    Last edited - 09 Sep 2023
    
    """
    if type(i) == int:
        if i % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
    else:
        return 'Not allowed'
    


# In[ ]:


is_even(5)


# In[ ]:


is_even("Hello")


# # Parameters Vs Arguments

# In[ ]:


# 1.Default Argumnets
# 2.Positional Arguments
# 3.Keyword Argumnets
# # 4.Arbitary Arguments


# In[ ]:


def power(a,b):
       return a**b


# In[ ]:


power(2,3)


# In[ ]:


#To avoid Crash of the Code by using Default Argument
# Default


# In[ ]:


def power(a=1,b=1):
      return a**b


# In[ ]:


power(4,5)


# In[ ]:


# We Use Keyword argument to avoid from Positional argument Concept


# In[ ]:


power(b=9,a=5)


# # Creating a number which gives the Output by Multiplying all the Input Numbers.

# In[ ]:


def flexi(*number): #Using astrick to make Variable a Tuple.
    product = 1
    print (number)
    print(type(number))
    for i in number:
          product=product*i
    print(product)


# In[ ]:


flexi(3,4,5)


# Global Var And Local Var / Nested Functions

# In[ ]:


#if the variable is created inside the function then it is a local variable
# and if the variable is in the main program then it is a Global Variable
# Example - 1
def f(y):
    x=1
    x +=1
    print(x)
    
x = 5
f(x)
print(x)


# In[ ]:


# Example - 2
def g(Y):
    print(x)
    print(x+1)
    
x = 5
g(x)
print(x)


# In[ ]:


#Example - 3
def  h(y):
    x +=1 #leads to an error without line 'global x' inside h caise u can only
#     use global varibale can not change that variable.
x = 5
h(x)
print(x)


# In[ ]:


#Example - 3
def  h(y):
    global x
    x +=1 # we will use global variable to avoid from error
x = 5
h(x)
print(x)


# In[ ]:


# Inner Function nested Function is always hidden from main Program.


# In[ ]:


def f():
    print('inside f')
    def g():
               print('inside g') 
    g()


# In[ ]:


f()


# In[ ]:


g()


# In[ ]:


def f():
    print('inside f')
    def g():
               print('inside g')
               f()

    g()


# # Everything in Python is an Object

# In[ ]:


def f(num):
    return num**2
f(2)


# In[ ]:


f(4)


# In[ ]:


# By Aliasing using funciton as an object


# In[ ]:


x=f
x(2)


# In[ ]:


x(5)


# In[ ]:


type(x)


# In[ ]:


L=[1,2,3,4]
L


# In[ ]:


L=[12,3,4,x]
L


# In[ ]:


L[-1](3)


# In[ ]:


L=[1,2,3,4,x(5)]


# In[ ]:


L


# In[ ]:


def func_a():
    print('inside func_a')
    
def func_c(z):
    print('inside func_c')
    return z()

print(func_c(func_a))


# In[ ]:


def f():
    def x(a,b):
        return a+b
    return x
val = f()(3,4)
print(val)


# In[ ]:


# Benefits of Functions
# Every code is self contained and used to break the entire logic in pieces
# (Code Modularity)
# Works on the philosophy of write once use forever!(Code Reusability)
# Code is organizaed and coherent (Code Readability)


# # Recursion

# In[ ]:


# Recursion is a code in which function call itself So, that you don't need to
# run the loop to solve any problem.


# In[ ]:


# Iterative Vs Recursive
#         a*b
def multiply(a,b):
    result = 0
    for i in range(b):
        result = result + a
        
    print(result)
    
multiply(3,4) #By Loops


# In[ ]:


# By Recursion (First of all get to know base case and then decompose big
# problem to small)
def mul(a,b):
    if b==1:
        return a
    else:
        return  a+mul(a,b-1)
print(mul(5,6))


# In[ ]:


#Find out the Factorial of a given number using Recursion.


# In[ ]:


def fact(number):
    if number==1:
        return 1
    else:
        # 5=5*4!
        return number*fact(number-1) 
print(fact(5))


# # Palindrome

# In[ ]:


def palin(text):
        if len(text)<=1:
            print("Palindrome")
        else:
            if text[0] == text[-1]:
                palin(text[1:-1])
            else:
                print("Not a palin")
palin("madam")


# In[ ]:


palin("malayalam")


# In[ ]:


palin("python")


# # The Rabbit Problem

# In[ ]:


#Fibbonaci Problem
# 0,1,2,3,4,.....,12
# 0,1,2,3,5......,x


# In[ ]:


def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
print(fib(22))


# In[ ]:


# We will use Memoization to reduce time Complexity for Fibbonaci problem.


# In[ ]:


import time
def memo(m,d):
    if m in d:
        return d[m]
    else: 
        d[m] = memo(m-1,d) + memo(m-2,d)
        return d[m]
start =time.time()
d ={0:1,1:1}
print(memo(500,d))
print(time.time()-start)


# # Power Set

# # {1,2} = { {}, {1} , {2} } Solving this using Recursion

# # Lamda Functions

# In[ ]:


#Anonymous Functions


# In[ ]:


lambda input: expression


# In[ ]:


x=lambda x:x**2
x(9)


# In[ ]:


a=lambda x,y:x+y
a(5,6)


# In[ ]:


# Difference
# 1. Lambda has no return value
# 2. One Line
# 3. Not used for Code Reusability
# 4. No name
type(a)
# Why
# Along with higher order functions


# In[ ]:


b=lambda x:x[0] == "a"
b('applw')


# In[ ]:


b("banana")
False


# In[ ]:


b= lambda x:"Even" if x%2 == 0 else "Odd"
b(3)


# In[ ]:


b(2)


# # Higher Order Function
def return_sum(L):
    even_sum=0
    odd_sum=0
    div3_sum=0
    
    for i in L:
        if i%2 == 0:
            even_sum = even_sum + i
        if i%2 !=0:
            odd_sum = odd_sum + i
    return (even_sum,odd)
Making thia to Higher Order Function
# In[ ]:


def return_sum(func,L):
    result = 0
    for i in L:
        if  func(i):
            result =result+i
    return result
    
L=[11,14,21,23,56,78,45,29,28]
x=lambda x:x%2 == 0
y=lambda x:x%2 != 0
z=lambda x:x%3 == 0
print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))


# Map Function

# In[ ]:


L=[1,2,3,4,5,6,7]
L


# In[ ]:


map(lambda x:x*2,L)  


# In[ ]:


list(map(lambda x:x*2,L))


# In[ ]:


list(map(lambda x: x%2 == 0,L))


# In[ ]:


Students = [
    {
        "name":"jacob martin",
        "father name":"Ros Martin",
        "Address":"123 Hill Street",
    },
    {
        "name": "Angela Stevens",
        "Father name": "Robert Stevens",
        "Address" : "3 Upper Street London",         
    },{
        "name":"Ricky Smart",
        "father name": "William Smart",
        "Address" : "Unknown",
    }
    
]


# In[ ]:


map(lambda student: student["name"],L)


# In[ ]:


map(lambda student: student["name"],Students)


# In[ ]:


list(map(lambda student: student["name"],Students))


# In[ ]:


# Filter Function


# In[ ]:


L


# In[ ]:


list(filter(lambda x:x>4 ,L))


# In[ ]:


fruits =["Apple","Orange","Mango","Guava"]
list(filter(lambda fruit:"e" in fruit, fruits))


# Reduce Functions

# In[ ]:


#import functools
# Reduce the list.


# In[ ]:


L


# In[ ]:


import functools
functools.reduce(lambda x,y:x+y,L)


# In[ ]:


L1=[1,234,2,43,2,5,2,15]


# In[ ]:


L1


# In[ ]:


functools.reduce(lambda x,y: x if x>y else y ,L1)


# In[ ]:


functools.reduce(lambda x,y: x if x<y else y ,L1)


# In[ ]:


# List Comprehension (Create a list from another list programeatically)


# In[ ]:


L


# In[ ]:


L1 = [item *2 for item in L]


# In[ ]:


L1


# In[ ]:


L2 =[i**2 for i in range(10)]


# In[ ]:


L2


# In[ ]:


L3=[i**2 for i in range(10) if i %2!=0]


# In[ ]:


L3


# In[ ]:


fruits


# In[ ]:


L4=[fruit for fruit in fruits if fruit[0]=="O"]


# In[ ]:


L4


# In[ ]:


D = {"Name": "Nitish","Gender":"Male","Age":30}


# In[ ]:


D.items()


# In[ ]:


D1={key:value for key,value in D.items() if len(key) > 3}


# In[ ]:


D1


# In[ ]:


L


# In[ ]:


D2={item:item**2 for item in L}


# In[ ]:


D2


# In[ ]:


D2={item:item**2 for item in L if item%2==0}


# In[ ]:


D2


# # Object Oriented Programming

# In[ ]:


#In Python everything is an Object.


# In[ ]:


# Helps in Planning  of Code to make real world application.
# Generality to Specificy.


# In[ ]:


# We Create our own Data Type to make the particular software better for the real life problem.


# In[ ]:


#Class name should be in pascal case.
# Thisispascalcase.


# In[ ]:


#Data and functions name should be in Snake_Case.
class car:
    color="blue" #data
    model="sports" #data
    def calculate_Avg_Speed(km,time):


# In[ ]:


#Methods are special functions which is return inside of a class.
# Function is outside of the class which can be access by any class and
# method is the function inside the class which can only be accessed by that
# class object.


# In[ ]:


#To declare variables inside the class.
 
class Atm:
 def _init_(self):
     self.pin=""
     self.balance=0
     sbi=Atm()
     #print("Hello")   
     self.menu()
 def menu(self):
     user_input=input("""
     Hello, how would you like to proceed
     1.Enter 1 to create pin
         2.Enter 2 to deposit
         3.Enter 3 to withdraw
         4.Enter 4 to check balance
         5.Enter 5 to exit
         """)
     if user_input=='1':
         self.create_pin()
         print('Create pin')
     elif user_input=='2':
         self.deposit()
     elif user_input =='3':
         self.withdraw()
     elif user_input == '4':
                     print('balance')
     else:
                         print('bye')
 def Create_pin(self):
     self.pin=input("Enter yoour Pin")
     print("Pin Set Successfully")
 def deposit(self):
     temp=input("Enter your Pin")
     if temp==self.pin:
         amount=int input("Enter the amount")
         self.balance=self.balance+amount
         print("Deposit Successful")
     else:
         print("Invalid Pin")
         


# In[ ]:


class Atm:
#Constructor --
#Constructor is a special function or method which is define inside the class 
#which code automatically execute when the object is created inside that class.
    
    def __init__(self): #To Declare Variable inside the class inside the method
#         self.pin=""
#         self.balance=0
        print('hello')
#         self.menu() #To call the menu function
#     def menu(self):
#         pass
sbi=Atm()


# In[ ]:


class Atm:

    def __init__(self): 
        self.pin=""
        self.balance=0
        print('hello')
        self.menu()
    
    def menu(self):
        user_input=input("""
         Hello, how would you like to proceed
        1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
        """)
        if user_input=="1":
            print("Create pin")
        elif user_input=="2":
                print("Withdraw")
        elif user_input=='3':
                print("deposit")
        elif user_input=='4':
                    print("balance")
        else:
                    print("bye")
sbi=Atm()


# In[ ]:


class Atm:

    def __init__(self): 
        self.pin=""
        self.balance=0
        print('hello')
        self.menu()
    
    def menu(self):
        user_input=input("""
         Hello, how would you like to proceed
        1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        else:
                    print("bye")
    def create_pin(self):
        self.pin=input("Enter your Pin")
        print("Pin Set Successfully")
    def deposit(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("Deposit Successful")
        else:
                print("Invalid Pin")
                
    def withdraw(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount<<self.balance:
                self.balance=self.balance-amount
                print("Operation Successsful")
            else:
                    print("insufficient funds")
        else:
                print("Invalid pin")
    def check_balance(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            print(self.balance)
        else:
                print("invalid pin")
        
sbi=Atm()


# In[ ]:


class Atm:

    def __init__(self): 
        self.pin=""
        self.balance=0
        print('hello')
        self.menu()
    
    def menu(self):
        user_input=input("""
         Hello, how would you like to proceed
        1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        else:
                    print("bye")
    def create_pin(self):
        self.pin=input("Enter your Pin")
        print("Pin Set Successfully")
    def deposit(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("Deposit Successful")
        else:
                print("Invalid Pin")
                
    def withdraw(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount<<self.balance:
                self.balance=self.balance-amount
                print("Operation Successsful")
            else:
                    print("insufficient funds")
        else:
                print("Invalid pin")
    def check_balance(self):
        temp=input("Enter your Pin")
        if temp==self.pin:
            print(self.balance)
        else:
                print("invalid pin")
        
sbi=Atm()


# In[ ]:


# Magic Method ( "__ ")[Double Underscore]
# These methods triggers automatically on the given criteria they can not be called
# by the ob.
print(id(self)) #working on with the current object is called self itself.


# # Fraction Class

# In[ ]:


class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        temp_num=self.num*other.den+other.num*self.den
        temp_den=self.den*other.den
    
        return"{}/{}".format(temp_num,temp_den)
    def __sub__(self,other):
        temp_num=self.num*other.den-other.num*self.den
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den
        return "{}/{}".format(temp_num,temp_den)
    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        return"{}/{}".format(temp_num,temp_den)
x=Fraction(4,5)
y=Fraction(6,7)

print(x+y)
print(x-y)
print(x*y)
print(x/y)


# In[ ]:


# __str__ Automatically Call when you put the class object in the print function
# directly .
print(x)
print(y)


# In[ ]:


# Operator Magic Methods Example = __mod__, __pow__


# # Encapsulation

# In[ ]:


# Instance Varibales are those variables who are created inside the constructor
# and their values are also different for every object.
# Data should not be left open when you created a class.
# (To make Private we use __ in python)
# __pin => _Atm__pin
# __balance => _Atm__balance
# sbi.__balance => __balance
# Nothing is pyhthon is truly private
# Merging One Data Member and its two methods together in Encapsulation.


# In[19]:


class Atm:

    def __init__(self): 
        self.__pin=""
        self.__balance=0
        self.sno=Atm.Counter
        Atm.Counter=Atm.Counter+1
        print('hello')
        self.menu()
    
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin Changed")
        else:
            print("Not Allowed") 
    def menu(self):
        user_input=input("""
         Hello, how would you like to proceed
        1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        else:
                    print("bye")
    def create_pin(self):
        self.__pin=input("Enter your Pin")
        print("Pin Set Successfully")
    def deposit(self):
        temp=input("Enter your Pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            self.__balance=self.__balance+amount
            print("Deposit Successful")
        else:
                print("Invalid Pin")
                
    def withdraw(self):
        temp=input("Enter your Pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Operation Successsful")
            else:
                    print("insufficient funds")
        else:
                print("Invalid pin")
    def check_balance(self):
        temp=input("Enter your Pin")
        if temp==self.__pin:
            print(self.__balance)
        else:
                print("invalid pin")
        
sbi=Atm()


# In[20]:


# To Change the pin  and balance variables of method of a class
# by any object can be done by getter and setter they can not be change directly 
# by objects cause they are inside constructor and private cause of __ .


# In[21]:


sbi.get_pin()


# In[22]:


sbi.menu()


# In[31]:


sbi.set_pin(5.6)


# In[32]:


sbi.get_pin()


# In[33]:


# why we using getter setter if we can just directly change the varihales too
# cause by using getter and setter we can apply logic on the changes too.


# In[34]:


sbi


# # Reference Variable

# In[35]:


Atm()


# In[38]:


# sbi=Atm() #Sbi is not the object object is Created at Atm() Step Sbi is
# reference variable and referencing on the actual address of that object.


# # Pass by Reference

# In[ ]:


class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(customer): #Its a function cause outside of the class. 
    if customer.gender=="Male":
        print("Hello",customer.name,"Sir")
    else:
        print("Hello",customer.name,"mam")
    cust2=Customer("Sanskar","Male")
    return cust2
new_cust=greet(cust)
print(cust2.name)

cust=Customer("Nitish","Male")
greet(cust)
print(cust.name)


# In[24]:


#  class ke objects are also mutable like lists, dict and sets.(
class Customer:
    def __init__(self,name):
        self.name=name
def greet(customer):
    print(id(customer))
    customer.name="Nitish"
    print(customer.name)
    print(id(customer))
cust=Customer("Ankita")
print(id(cust))
greet(cust)
print(cust.name)


# In[25]:


# If we are taking a function call and you want to send the list
# to the function then send the clonning of that list so that it can
# avoid permanent changes in the original list by the function.


# In[27]:


def change(L):
    print(id(L))
    L.append(5)
    print(id(L))
L1=[1,2,3,4]
print(id(L1))
print(L1)

change(L1[:])
print(L1)


# # Collection of Objects

# In[ ]:


#We can drop objects of our class in list,dict,tuples.
class Customer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
         print("I am",self.name,"and I am",self.age)
c1=Customer("Nitish",21)
c2=Customer("Sanskar",22)
c3=Customer("Neha",22)
L=[c1,c2,c3]

for i in L:
    print(i.name,i.age)
    i.intro()


# # Static
# 

# In[1]:


# Static Counter or Static/Class Variable is a type of variable which values are
# similar for all the objects Like IFSC Code for the Bank Accounts.
# Its Declare Outside of the Constructor.
# Counter=1
class Atm():
    counter=1
    def _init_(self):
        self.__pin=""
        self.__balance=0
        self.sno=Atm.counter
        Atm.counter=Atm.counter+1
c1=Atm()
c2=Atm()
c3=Atm()


# In[2]:


c1


# In[3]:


c2


# In[4]:


c3


# In[17]:


class Atm:
    __counter=1
    def __init__(self): 
        self.__pin=""
        self.__balance=0
        self.sno=Atm.__counter
        Atm.__counter=Atm.__counter+1
        print('hello')
        self.menu()
    def get_counter(self):
        return Atm.__counter
    def set_counter(new):   #Static Method
        if type(new)==int: 
            Atm.__counter=new
        else:
            print("Not Allowed")
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("Pin Changed")
        else:
            print("Not Allowed") 
    def menu(self):
        user_input=input("""
         Hello, how would you like to proceed
        1.Enter 1 to create pin
            2.Enter 2 to deposit
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exit
        """)
        if user_input=="1":
            self.create_pin()
        elif user_input=="2":
            self.deposit()
        elif user_input=='3':
            self.withdraw()
        elif user_input=='4':
            self.check_balance()
        else:
                    print("bye")
    def create_pin(self):
        self.__pin=input("Enter your Pin")
        print("Pin Set Successfully")
    def deposit(self):
        temp=input("Enter your Pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            self.__balance=self.__balance+amount
            print("Deposit Successful")
        else:
                print("Invalid Pin")
                
    def withdraw(self):
        temp=input("Enter your Pin")
        if temp==self.__pin:
            amount=int(input("Enter the amount"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("Operation Successsful")
            else:
                    print("insufficient funds")
        else:
                print("Invalid pin")
    def check_balance(self):
        temp=input("Enter your Pin")
        if temp==self.__pin:
            print(self.__balance)
        else:
                print("invalid pin")
        
sbi=Atm()
c1=Atm()
c2=Atm()
c3=Atm()


# In[3]:


Atm.get_counter()


# In[4]:


c2.sno


# # Realtionship

# # Aggregation (HAS-A)

# In[10]:


# {Customer => Has - a  Addreess}
class customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pin,new_state)
class address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city
        self.pincode=new_pin
        self.state=new_state
add=address("Kolkata",700156,"WB")
cust=customer("sanskar","Male",add)
cust.edit_profile("Ankit","Gurgaon",122011,"haryana")
print(cust.address)
print(cust.address.city)
print(cust.address.pincode)


# # Inheritance

# In[11]:


# Enhance Code Reusability


# In[7]:


class User:
    def login(self):
        print("Login")
    def register(Self):
        print("Rgister")
class Student(User):
    def enroll(self):
        print("Entroll")
        def review(self):
            print("Review")
stu1=Student()
stu1.login()


# # Inheriting Constructor

# In[26]:


class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
class smartphone(Phone):
    pass
s=smartphone("20000","Xioami","100MP")


# In[27]:


print(s.brand)


# # Inheriting Private Members

# In[31]:


# Child class object can not access hidden members of parent class.


# # Polymorphism

# In[35]:


#Method Overriding
class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
s=SmartPhone(20000,"Apple",13)
s.buy()


# # Example Class Parent

# In[38]:


class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class Child(Parent):
    def show(self):
        print("This is in child class")
son=Child(100)
print(son.get_num())
son.show()


# # Example Class Parent 2

# In[39]:


# # If Child has its own constructor then parent constructor won't
# be execute and if it does not have any constructor then parent's
# constructor will be run at first.
class parent:
    def __init__(self,num):
        self.__num==num
    def get_num(self):
        return self.__num
class Child(parent):
    def __init__(self,val,num):
        self.__val=val
        
        def get_val(self):
            return self.__Val
son=Child(100,10)
print("Parent:Num:",son.get_num())


# # Example 3

# In[49]:


class A:
    def __init__(self):
        self.var1=100
    def display1(self,var1):
        print("class A:",self.var1)
class B(A):
    def display2(self,var1):
        print("class B:",self.var1)
obj=B()
obj.display1(200)


# # Example of Super Keyword

# In[50]:


class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
        super().buy() #By using super we invoke parents
#Constructor it only works inside of the class.
s=SmartPhone(20000,"Apple",13)
s.buy()


# In[54]:


class Phone:
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
class SmartPhone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        print("pehle yahan")
        super().__init__(price,brand,camera) #Transfered
# these values using super keyword to the parent calss.
        self.os=os
        self.ram=ram
        print("inside SmartPhone constructor")
s=SmartPhone(20000,"Samsung",12,"Android",2)
print(s.os)
print(s.brand)


# # Examples on Super

# In[4]:


class Parent:
    def __init__(self):
        self.num=100
class Child(Parent):
    def __int__(self):
        super().__int__()
        self.var=200
    def show(self):
        print(self.num)
        print(self.var)
son=Child()
son.show()


# # Types of Inheritance

# In[7]:


1. Single - Level Inheritance
2. Multi - Level Inheritance
3. Hierarchical Inheritance #One parent Two Childrens
4. Multiple Inheritance #Two parent One Children
5. Hybrid Inheritance #Combination of all Inheritance


# # Multiple Inheritance Example

# In[14]:


class Phone:
    def _init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
class Product:
    def buy(self):
        print ("Product buy method")
class SmartPhone(Phone,Product):
        pass
s=SmartPhone(20000,"Apple",12)
s.buy()


# In[18]:


class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40
class C(B):
    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1()+obj3.m1()+obj3.m2())


# # Polymorphism (Method Overloading)

# In[19]:


class Geometry:
    def area(self,a,b=0):
        if b==0:
            print("Circle",3.14*a*a)
        else:
            print("Rect",a*b)
obj=Geometry()
obj.area(4)
obj.area(4,5)
# Technically Method Overloading does'nt exists in python but
# its still an example of how we can achieve it in python.


# # Operator Overaloading

# In[7]:


# Like doing something else with the operator is called Operator
# Overloading.


# In[8]:


pip install requests


# # Threading

# In[9]:


from time import sleep, time


# In[22]:


start_time=time()
import threading
def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Woken up....{id}")
t1=threading.Thread(target=something,args=[0])
t1.start()
        
end_time=time()
print(f"Main Thread Ended in{end_time-start_time}seconds")

# Do Something


# In[23]:


start_time=time()
import threading
def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Woken up....{id}")
t1=threading.Thread(target=something,args=[0])
t1.start()
t1.join()
end_time=time()
print(f"Main Thread Ended in{end_time-start_time}seconds")

# Do Something 


# In[25]:


start_time=time()
import threading
def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Woken up....{id}")
t1=threading.Thread(target=something,args=[0])
t2=threading.Thread(target=something,args=[1])

t1.start()
t2.start()
t1.join()
t2.join()

end_time=time()
print(f"Main Thread Ended in{end_time-start_time}seconds")

# Do Something


# In[26]:


start_time=time()
import threading
def something(id):
    print(f"Going to sleep...{id}")
    sleep(1)
    print(f"Woken up....{id}")
threads=[threading.Thread(target=something,args=[i]) for i in range(10)]
for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()
      
end_time=time()
print(f"Main Thread Ended in{end_time-start_time}seconds")

# Do Something


# # Synchronize Threads

# In[59]:


import threading
balance=200
lock=threading.Lock()
def deposit(amount,  times,lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance+=amount
        lock.release()
        
def withdraw(amount,  times,lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance-=amount
        lock.release()
deposit_thread=threading.Thread(target=deposit,args=[1, 100000,lock])
withdraw_thread=threading.Thread(target=withdraw,args=[1,  100000,lock])
deposit_thread.start()
withdraw_thread.start()
deposit_thread.join()
withdraw_thread.join()
print(balance)



# # Iterators

# # What is an Iteration?
Iteration is a general term for taking each item of something, one after another.
Any time you use a loop,explicit or implicit, to go over a group of items, that is iteration.
 
# # What is Iterator?
An iterator is an object that allows the programmer to traverse through
a sequence of data without having to store the entire data in the memory.
# In[72]:


L=[x for x in range(1,10000)]
# for i in L:
#     print (i*2)
import sys
print(sys.getsizeof(L)/102)
x=range(1,10000)
# for i in x:
#     print(i*2)
print(sys.getsizeof(x)/102)


# # What is Iterable?
Iterable is an Object, which one can iterate over.
It generates an Iterator when passed to iter() method.
# In[73]:


L=[1,2,3]
type(L)


# In[74]:


# L is an iterable
iter(L)


# In[75]:


type(iter(L))


# In[76]:


#iter(L) ----> iterator


# In[91]:


#Every Iterator is also and Iterable.
#Not all Iterables are Iterators like lists.


# In[92]:


L =[1,2,3]
# l is not an iterator cause iter and then next is not present.
dir(L)


# In[93]:


iter(L)


# In[94]:


dir(iter(L))  # Iter(l) is an iterator.


# In[97]:


T=(1,2,3)
dir(T) #Tuple is an iterbale cause iter is present and
# loops can work on this iterators.


# # Understanding how for Loop Works

# In[98]:


num = [1,2,3]
for i in num:
    print(i)


# In[99]:


num=[1,2,3]
#fetch the iterator
iter_num= iter(num)
#step2 ---> next)
next(iter_num)
next(iter_num)
next(iter_num)
next(iter_num)


# # Making Our Own for Loop

# In[105]:


def mera_khudka_for_loop(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
                break


# In[110]:


a=[1,2,3]
b=range(1,11)
c=(1,2,3)
d={1,2,3}
e={0:1,1:1}
mera_khudka_for_loop(c)


# # A Confusing Point

# In[111]:


num=[1,2,3]
iter_obj=iter(num)
print(id(iter_obj),"Address of iterator 1")
iter_obj2=iter(iter_obj)
print(id(iter_obj2),"Address of iterator 2")


# # Let's Create Own Range() Function 

# In[116]:


class mera_range:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return mera_range_iterator(self)
class mera_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable=iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current=self.iterable.start
        self.iterable.start+=1
        return current
for i in mera_range(1,11):
    print(i)


# # Generators

# In[117]:


# Python generates are a simple way of creating iterators.


# # Example of Python Generator

# In[118]:


def gen_demo():
    yield "first statement"
    yield "Second statement"
    yield "third statement"
gen=gen_demo()
print(gen)


# In[119]:


print(next(gen))


# In[120]:


print(next(gen))


# In[121]:


print(next(gen))


# In[122]:


print(next(gen))


# In[3]:


def square(num):
    for i in range(1,num+1):
        yield i**2
gen=square(10)
print(next(gen))
for i in gen:
    print(i)


# # Range Function Using Generator

# In[4]:


def mera_range(start,end):
    for i in range(start,end):
        yield i


# In[5]:


gen= mera_range(15,26)
for i in gen:
    print(i)


# # Generator Expression

# In[11]:


# list Comprehension
# L=[i**2 for i in range(1,101)]
gen=(i**2 for i in range(1,101))
for i in gen:
    print(i)


# # Practice Example

# In[2]:


pip install opencv-python


# In[18]:


# Converting images into numpy array so that we can train a model on it.
import os
import cv2
def image_data_reader(folder_path):
    for file in os.listdir(folder_path):
        f_array=cv2.imread(os.path.join(folder_path,file))
        yield f_array
gen=image_data_reader('D:/Screenshots/Newfolder')
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)


# In[22]:


import os
import cv2
def image_data_reader(folder_path):
    for file in os.listdir(folder_path):
        f_array=cv2.imread(os.path.join(folder_path,file))
        yield f_array
gen=image_data_reader("D:/Screenshots/Newfolder")

next(gen)


# #  Benefit of Using a Generator

# In[23]:


def mera_range(start,end):
    for i in range(start,end):
        yield 1


# # 2. Memory Efficient

# # 3. Representing Infinite Streams

# In[25]:


def all_even():
    n=0
    while True:
        yield n
        n+=2
even_num_gen = all_even()
next(even_num_gen)
next(even_num_gen)
next(even_num_gen)


# # 4. Chaining Generators

# In[30]:


import math
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))

