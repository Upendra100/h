from re import findall

# 1. Write a program to find the length of the string without using inbuilt function
sentence = "Hello world this is python and python is programming language"
leng=0
for char in sentence:
    leng=leng+1
print(leng)


# 2. Write a program to reverse a string without using any inbuilt functions.
string='testyantra'
rev=''
for word in string:
    rev=word+rev
print(rev)


# 3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".
string="Hello World"
old="World"
new="Universe"
r=string.replace("World","Universe")
print(r)
#    OR
# words=string.split()
# result=''
# for i in words:
#     if i == old:
#         i=new
#         result=word+i
# print(result)

# 4. How to convert a string to a list and vice-versa.

#String to list
word="python"
a=list(word)
print(a)

#list to string
listword=["p","y","t","h","o","n"]
string = "".join(listword)
print(string)


# 5. Convert the string "Hello welcome to Python" to a comma separated string.
string='Hello welcome to Python'
words=string.split()
x=",".join(words)
print(x)


# 6. Write a program to print alternate characters in a string.
sentence = "Hello world this is python and python is programming language"
print(sentence[::2])


# 7. Write a Program to print ascii values of the characters present in a string
string='Hello welcome to Python'
d={}
for char in string:
    d[char]=ord(char)
print(d)


# 8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.

def ul(char):
    if ord('a')<=ord(char)<=ord('z'):
        print(chr(ord(char)-32))
    elif ord('A')<=ord(char)<=ord('Z'):
        print(chr(ord(char)+32))

ul('c')


# 9. Write a program to swap two numbers without using the 3rd variable.
a=10
b=20
a,b=b,a
print(a,b)


# 10. Write a program to merge two different lists.
l1=[1,2,3,4]
l2=[5,6,7,8]
l=l1+l2
print(l)


# 11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)
path = r"C:\Users\Upendra\Desktop\Python\data\access.log"
def random_line(n):
    with open(path) as file:
        for index, line in enumerate(file,start=1):
            if line.strip():
                if line:
                    if n==index:
                        return line
random_line(6)


# 12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)
path = r"C:\Users\Upendra\Desktop\Python\data\access.log"
def random_line(a,b):
    with open(path) as file:
        for index,line in enumerate(file,start=1):
            if a <= index <= b:
                print(index,line)
random_line(10,15)



# 13 Program to print the last "N" lines of a file.

path = r"C:\Users\Upendra\Desktop\Python\data\access.log"
def last_n(num):
    with open(path) as file:
        count=0
        for line in file:
            count += 1
        file.seek(0)
        a=count-num
        for index,line in enumerate(file,start=1):
            if a<index<=count:
                print(index,line)
last_n(2)



# 14. Write a program to check if the given string is Palindrome or not without using reversed method.
def palindrome(string):
    string='malayalam'
    rev=''
    for word in string:
        rev=word+rev
    if rev==string:
        return "string is palindrome"
    else:
        return "string is not palindrome"


# 15. Write a program to search for a character in a given string and return the corresponding index.
# or
# WAP to linear search
string='malayalam'
# char = input("Enter a character: ")           
for index,value in enumerate(string):
    if char in value:
        print(index)


# 16. Write a program to get the below output
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

sentence = "hello world welcome to python programming hi there"
d={}
words=sentence.split()
for word in words:
    key="".join(word[0])
    if key not in d:
        d[key]=[word]
    else:
        d[key].append(word)
print(d)

# 17 WAP to replace all the characters with - if the character occurs more than once in a string

string='hellohai'
for char in string:
    if string.count(char) > 1:
        string=string.replace(char,"-")
print(string)


# 18 write a decorator that returns only positive values of subtraction
def positive(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)   # address of the main function
        return abs(result)
    return wrapper

@positive      # sub = positive(sub)
def sub(a,b):
    return a-b
sub(10,20)


# 19 How to get the count of the number of instances of a class that is being created.
class Sample:
    count = 0

    def __init__(self):
        Sample.count += 1
        print(Sample.count)

s1=Sample()  #1
s2=Sample()  #2
s3=Sample()  #3


# 20. Write a function which takes a list of strings and integers.If the item is a string it should print as is 
# and if the item is integer or float it should reverse it.
 
l=['hello','world',15.87,'hi']
d={}
for word in l:
    if isinstance(word,str):
        print(word)
    elif isinstance(word,(int,float)):
        print(str(word)[::-1])
print(d)


# 21 Write a class named Simple and it should have iteration capability.

class Sample:
    def __init__(self,element):
        self.element = element
    def __iter__(self):
        return iter(self.element)

a=[1,2,3,4]
s = Sample(a)
for item in s:
    print(item)

# 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a

class Custom:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __getitem__(self,key):
        return self.__dict__[key]

d=Custom(10,20)
#d1["a"]
d.a


# 23 Write a python program to get the below output
# o/p should be "iH woH era uoy"

sentence = "Hi How are you"
words=sentence.split()
new=''
for word in words:
    new = new+word[::-1]+" "
print(new)


# 24 Write a python program to get the below output
# o/p should be "ouy era woH iH"

sentence = "Hi How are you"
print(sentence[::-1])


# 25 Write a lambda function to add two numbers (a, b)

add = (lambda num1,num2: (num1+num2))
print(add(10,20))


# 26. What is the output of the following
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])    # [[1, 2, 3], [4, 5, 6]]
print((a, b))    # ([1, 2, 3], [4, 5, 6])


# 27. How to remove duplicates from the list without using inbuilt functions**
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
def remove_dup(items):
    d={}
    for item in items:
       if item not in d:
           d[item]=1
       else:
           d[item] += 1
    for key,value in d.items():
        if value==1:
           return(key)
print(remove_dup(items))


# 28 Find the longest word in the sentence

sentence = "python is programming language and it is scripting language"
longest=''
words=sentence.split()
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)

# 29 write a program to reverse the values in the dictionary if the value is of type String
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
for k,v in d.items():
    if isinstance(v,str):
        d[k]=v[::-1]
print(d)                               # Append in d while gives the result


# 30 write a program to get 1234     # And by using join
t = ('1', '2', '3', '4')
s=''
for num in t:
    s += num
print(s)


# 31 How to get the elements that are in list b but not in list a.    # And by using difference
a = [1, 2, 3] 
b = [1, 2, 3, 4] 

for item in b:
    if item not in a:
        print(item)


# 32 A function takes variable number of positional arguments as input. How to check if 
# the arguments that are passed are more than 5
def func(*args,**kwargs):
    if len(args) + len(kwargs)>5:
        return True
    return False
func(1,2,3,4,a=2,b=4)


# 33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file
# Assume Below is the contents of the log file

file=r"C:\Users\Upendra\Desktop\Python\data\Interview_que_33.txt"
d={}
with open(file) as f:
    for line in f:
        if line.strip():
            name=line.split(":")
            if name[0] not in d:
                d[name[0]] = 1
            else:
                d[name[0]] += 1

print(d)


# 34 Write a function to reverse any iterable without using reverse function.     ##Ask
string="Bangalore"
rev=''
for char in string:
    rev=char+rev
print(rev)


# 35 Write a function to print the below output.

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX

def func(string, value):
    if value == 0:
        return(string [1::2])
    elif value == 1:
        return(string[::2])

print(func("TRACXN",0))
print(func("TRACXN",1))


# 36 Sum all the numbers in the below string.
s = "Sony12India567Pvt2ltd"
result = findall(r"\d",s)
sum=0
for num in result:
    if isinstance(num,str):
        n=int(num)
        sum=sum+n
print(sum)


# 37 Write a program to sum all the numbers in below string.
# eg.12+567+2
s = "Sony12India567Pvt2ltd"
result=findall(r"\d+",s)
sum=0
for num in result:
    if isinstance(num,str):
        n=int(num)
        sum=sum+n
print(sum)


# 38 Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']
joiner =''.join(a)
result=findall(r"\d+",joiner)
n=[]
for num in result:
    if isinstance(num,str):
        n.append(int(num))
print(n)

#####=====================================#####
for item in a:
    if isinstance (item,(int,float)):
        print(item)
        

# 39 Program to print the number of occurrences of characters in a String without using inbuilt functions.
string = "programming"
d={}
for char in string:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

print(d)


# 40. Program to print only the repeated characters and count of the same.
string = "programming"
d={}
for char in string:
    if string.count(char)>1:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
print(d)


# 41. Write a program to get alternate characters of a string in list format.
sentence = "hello world this is python language"
l=list(sentence[::2])
print(l)

# 42. Write a program to get square of list of number's using lambda function.
num=[1,2,3,4,5]
sq = lambda num : num**2
for n in num:
    print(sq(n))
#      OR
print(list(map(sq,num)))

# 43. Write a function that accepts two strings and returns True if the two strings are anagrams of each other.
l=["silent","listen"]
def anagram(l):
    if sorted(l[0].lower()) == sorted(l[1].lower()):
        return "True"
    else:
        return "False"
print(anagram(l))


# 44. Write a program to iterate through list and build a new list, only if the items of the list has even 
# number of characters.
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
l=[]
for name in names:
    if len(name)%2==0:
        l.append(name)
print(l)


# 45. Write a program to iterate through list and build a new dictionary, only if the items of the list has 
# even number of characters.
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
d={}
for name in names:
    if len(name)%2==0:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
print(d)


# 46. Write a program which squares the numbers in a list using map object**
a = [1, 2, 3, 4, 5]
sq = lambda num : num**2
print(list(map(sq,a)))


# 47. Count number of lines in a file without loading the file to the memory

path = r"C:\Users\Upendra\Desktop\Python\data\access.log"
count=0
with open(path) as file:
    for line in file:
        count += 1
print(count)


# 48 Printing line and line no's
file=r"C:\Users\Upendra\Desktop\Python\data\Interview_que_33.txt"
with open(path) as file:
    for index,line in enumerate(file):
        print(index,line)


# 49 Write a Program to print the sum of entire list and sum of only internal list**
l = [[1,2,3],[4,5,6],[7,8,9]]
a=[]
out_sum=0
for item in l:
    inner_sum = 0
    for i in item:
        inner_sum += i
        out_sum += i
    a.append(inner_sum)
print(out_sum)
# print(a)

# OR
# inner_sum=[sum(l) for item in l]
# external_sum=[sum(inner_sum)]

# 50 Write a program to reverse the list as below**
words = ["hi", "hello", "python","testing"]
# for word in words:
print(words[-1:-len(words)-1:-1])


# 51 Write a program to update the tuple**
# o/p (1, 2, 3, 4, 100, 200, 300)
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
print(t1+t2)


# 52 Write a program to replace value present in nested dictionary.**
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"
old="nose"
new="net"
for key,value in d.items():
    if isinstance(value,dict):
        for k,v in value.items():
         if v==old:
                value[k] = new
                
print(d)


# 53 Write a program to count the number of white spaces in a file.
sentence = "hello world this is python language"
result = findall(r"/s",sentence)
print(len(result))


# 54 Grouping anagrams.
words=['eat','ate','tea','hello','silent','listen']
d={}
for word in words:
    key=''.join(sorted(word))
    if key not in d:
        d[key]=[word]
    else:
        d[key].append(word)
print(d)


# 
# 55, 56, 57, 58 are thoery question
# 
# Q.56 property_decorator.py file


# 59 Write a list comprehension to get a list of even numbers from 1-50
even_=list([num for num in range(1,50) if num%2==0])
print(even_)


# 60 Find the longest non-repeated substring in the below string
sentence = "python is programming language and programming is fun"
longest=""
words=sentence.split()
for word in words:
    if len(word) > len(longest) and sentence.count(word)==1:
        longest=word
print(longest)


# 61 Write a program to find the duplicate elements in the list without using inbuilt functions
sentence = ["python", "is", "programming", "language", "and", "programming", "is", "fun"]
d={}
for word in sentence:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for key,value in d.items():
    if value>1:
       print(value)

# Using inbuilt function     # Right
# l=[]
# for word in sentence:
#     if sentence.count(word)>1 and word not in l:
#         l.append(word)
# print(l)


# 62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

d={}
for name in names:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
print(d)


# 63 Write a function to check if the number is Prime
def prime(num):
    if num <=1:
        return (f"{num} is not Prime Number")
    else:
        for i in range(2,num):
            if num%i==0:
                return (f"{num} is not Prime Number")
                break
            else:
                return (f"{num} is Prime Number")
                break
print(prime(17))


# 64 How to create a tuple of numbers from 0 to 10 using range function
for num in range(1,10):
    print(num)
    # OR
print(tuple(range(10)))


# 65 Write a program to find the largest number in the list without using any inbuilt functions
l=[4,7,3,45,89,32,6,64]
largest=0
for num in l:
    if num>largest:
        largest=num
print(largest)

# 66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) 
# should return 2

digit=3572
print(digit % 10)

#######      Reverse numbers without using convert to string     #########
rev=0
while digit>0:
    ld=digit%10
    rev=rev*10+ld
    digit=digit//10
print(rev)


# 67 Write a program to find most common words in a given list.**
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]

d={}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
sor = sorted(d.items(), key=lambda item:item[-1])   # value is [-1]   # item is key and value and item is 
print(sor[-1])                                                        # accept only one key or value


# 68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and 
# returns the last n elements from the given sequence, as a list.

# list=["hello","world","this","is"]
# s="helloworldthisis"
# tup=("helloworldhi")
# def tail(sequence,num):
#     if isinstance(sequence, (list,tuple,str)):
#        return list(sequence[-num:])

# print(tail(s,3))


# 69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square 
# and False if it's not.

num=36
def is_perfect_square(num):
    for i in range(1,num):
        if i*i==num:
            return(f"{num} is Perfect square of {i}")
    else:
        return (f"{num} is not Perfect square")
print(is_perfect_square(num))


# 70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

d={}
for name in names:
    if names.count(name)>1:
        if name not in d:
            d[name] = 1
        else:
            d[name] += 1
print(d)


# 71 Write a program to count the number of occurrences of each word in a file.
file=r"C:\Users\Upendra\Desktop\Python\data\Interview_que_33.txt"
d={}
with open(file) as f:
    for line in f:
        sp=line.split()
        for match in sp:
            if match not in d:
                d[match] = 1
            else:
                d[match] += 1
print(d)


# 72 Write a program to count the number of occurrences of vowels in a file.
file=r"C:\Users\Upendra\Desktop\Python\data\Interview_que_33.txt"
count=0
with open(file) as f:
    for line in f:
        for vow in line:
            if vow in ("aeiou"):
                count=count+1
print(count)

# 73 Write a program to print all numeric values in a list      # Ask
items = ['apple', 1.2, 'google', '12.6', 26, '100']
for item in items:
    if isinstance(item,(int,float)):
        print(item)


# 74   Triangle

# 75 Write a program count the occurrence of a particular word in the file
file=r"C:\Users\Upendra\Desktop\Python\data\Interview_que_33.txt"
word="is"
count=0
with open(file) as f:
    for line in f:
        sp=line.split()
        for match in sp:
            if match == word:
              count += 1
print(count)


# 76 Write a program to map a product to a company and build a dictionary with company and list of products pair
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 
                'iOS', 'Google Drive', 'One Drive']

# Pre-defined products for different companies
apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}
# ------------------------------------------------------



# 77 Write a program to rotate items of the list      # Using num of last digit rotate
names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
key=2

for i in range(key):
    element = names.pop()
    names.insert(0, element)
    print(names)


# 78 Write a program to rotate characters in a string



# 79 Write a program to count the number of white spaces in a given string
string='Hello welcome to Python'
count=0
for char in string:
    if " " == char:
        count += 1
print(count)


# 80 Write a program to print only non-repeated characters in a string
string="python is programming language and programming is fun"
l=[]
words=string.split()
for word in words:
    if string.count(word)==1:
        l.append(word)
print(l)














# linear search   search line by line or one char to other char





# 89 Write a program to get the below output
# o/p:[1, 2]
    # [3, 4]
    # [5, 6]
    # [7, 8]
    # [9]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(a), 2):
    print(a[i : i+2])