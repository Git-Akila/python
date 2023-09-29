#First Program
print("This is sparta!!!")
This is sparta!!!
#Variables
var1="John"
print(var1)
John
var1="Sam"
print(var1)
Sam
var1="Matt"
print(var1)
Matt
#Data-Type
a=10
type(a)
int
a=10.5
type(a)
float
a="sparta"
type(a)
str
a=True
type(a)
bool
a=3+4j
type(a)
complex
#Arithmetic Operators
a=10
b=20
print(a+b)
30
print(a-b)
-10
print(a*b)
200
print(a/b)
0.5
#Relational Operators
a=10
b=20
a>b
False
a<b
True
a==b
False
a!=b
True
#Logical Operators
a=True
b=False
a&b
False
b&a
False
b&b
False
a&a
True
a|b
True
b|a
True
a|a
True
b|b
False
#Strings
my_string="My name is John"
my_string[0]
'M'
my_string="My name is John"
my_string[-1]
'n'
my_string[0:4]
'My n'
len(my_string)
15
my_string.lower()
'my name is john'
my_string.upper()
'MY NAME IS JOHN'
my_string.replace('y','a')
'Ma name is John'
new_string = "hello hello world"
new_string.count("hello")
2
s1 = 'This is sparta!!!'
s1.find('sparta')
8
s1.find('b')
1
fruit = 'I like apples, mangoes, bananas'

fruit.split(',')
['I like apples', ' mangoes', ' bananas']
#Tuples in Python
tup1=(1,"a",True,2,"b",False)
tup1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-afd04ff38ac4> in <module>
----> 1 tup1

NameError: name 'tup1' is not defined
tup1[0]
1
tup1[-1]
False
tup1=(1,"a",True,2,"b",False)
tup1[1:4]
('a', True, 2)
tup1[1:4]
('a', True, 2)
tup1[2]="hello"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-49-2fc16622751e> in <module>
----> 1 tup1[2]="hello"

TypeError: 'tuple' object does not support item assignment
tup1[6]=3+4j
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-50-3b75c4b77e6a> in <module>
----> 1 tup1[6]=3+4j

TypeError: 'tuple' object does not support item assignment
min(tup1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-52-ce68c930ff7f> in <module>
----> 1 min(tup1)

TypeError: '<' not supported between instances of 'str' and 'int'
tup1=(1,"a",True,2,"b",False)
len(tup1)
6
tup1 = (1,"a",True)
tup2 = (4,5,6)
tup2+tup1
(4, 5, 6, 1, 'a', True)
tup1 = ('sparta',300)
tup2 = (4,5,6)
tup1*3 + tup2
('sparta', 300, 'sparta', 300, 'sparta', 300, 4, 5, 6)
tup1=(1,2,3,4,5)
min(tup1)
1
tup1=(1,2,3,4,5)
max(tup1)
5
cmp(tup1,tup2)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-34-e27d9faf1f7f> in <module>
----> 1 cmp(tup1,tup2)

NameError: name 'cmp' is not defined
#List in Python
 
l1=[1,"a",2,"b",3,"c"]
l1=[1,"a",2,"b",3,"c"]
l1[1]
'a'
l1=[1,"a",2,"b",3,"c"]
l1[2:5]
[2, 'b', 3]
l1=[1,"a",2,"b",3,"c"]
l1[0]=100
l1
[100, 'a', 2, 'b', 3, 'c']
l1=[1,"a",2,"b",3,"c"]
l1.append("Sparta")
l1
[1, 'a', 2, 'b', 3, 'c', 'Sparta']
l1
[100, 'a', 2, 'b', 3, 'c', True]
l1=[1,"a",2,"b",3,"c"]
l1.pop()
l1
[1, 'a', 2, 'b', 3]
l1
[1, 'a', 2, 'b', 3]
l1=[1,"a",2,"b",3,"c"]
l1.insert(1,"Sparta")
l1
[1, 'Sparta', 'a', 2, 'b', 3, 'c']
l1 = ["mango","banana","guava","apple"]
l1.sort()
l1
['apple', 'banana', 'guava', 'mango']
l1 = [1,2,3]
l2 = ["a","b","c"]
l1+l2
[1, 2, 3, 'a', 'b', 'c']
l1 = [1,"a",True]
l1*3
[1, 'a', True, 1, 'a', True, 1, 'a', True]
#Dictionary in Python
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit.keys()
dict_keys(['Apple', 'Orange', 'Banana', 'Guava'])
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit.values()
dict_values([10, 20, 30, 40])
fruit["Apple"]
10
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit["Mango"]=50
fruit
{'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40, 'Mango': 50}
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40,"Mango":50}
fruit["Apple"]=100
fruit
{'Apple': 100, 'Orange': 20, 'Banana': 30, 'Guava': 40, 'Mango': 50}
fruit1={"Apple":10,"Orange":20}
fruit2={"Banana":30,"Guava":40}

fruit1.update(fruit2)

fruit1
{'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit.pop("Orange")
fruit
{'Apple': 10, 'Banana': 30, 'Guava': 40}
#Set in Python
s1={1,"a",True,2,"b",False}
s1
{1, 2, False, 'a', 'b'}
s1={1,"a",True,2,"b",False}
s1.add("Hello")
s1
{1, 2, False, 'Hello', 'a', 'b'}
s1={1,"a",True,2,"b",False}
s1.update([10,20,30])
s1
{1, 10, 2, 20, 30, False, 'a', 'b'}
s1={1,"a",True,2,"b",False}
s1.remove("b")
s1
{1, 2, False, 'a'}
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

s1.intersection(s2)
{5, 6}
