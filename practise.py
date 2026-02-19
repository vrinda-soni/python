#Q01

a=5
b=10

a,b = b,a 
print(f"a= {a},b= {b}")

#Q02
values=[]

for i in range(5):
    val = input("enter the value:")
    values.append(val)

for v in values:
    print(f"{v}is a type of {type(v).__name__}")

#Q03

ab = 10
cd = 3

print(ab+cd)
print(ab-cd)
print(ab*cd)
print(ab/cd)
print(ab//cd)
print(ab%cd)

#Q04

item1="apple"
price1= 1.50
item2 = "orange"
price2 = 2.535
item3 = "strawberry"
price3 = 64.74

print(f"{item1}: ${price1:.2f}")
print(f"{item2}: ${price2:.2f}")
print(f"{item3}: ${price3:.2f}")

#Q05
import datetime
name = "Alice"
age = 20

year = datetime.date.today().year - age
print(f"Hello {name}! You were born in {year}")

#Q06
i = 6
while i>=1:
    i-=1
    print(i)
print("blast off")

# #Q07
n=4
for i in range(1,n+1):
    print("*",i)

#Q08
score =45
if score<=100 and score>90:
    print("A")

elif score<=89 and score>80:
    print("B")

elif score<=79 and score>70:
    print("C")

elif score<=69 and score>60:
    print("D")

elif score<=59:
    print("F")

else: 
    print("please enter a valid number")



#Q09
age = 8
weekend = True

price =0

if age<=12:
   price = 5

elif age>=60:
    price = 6

elif age>12 and age<=59:
    price = 10

if weekend == True:
    price +=2
 
print("the ticket price is",price)

#Q10

day = "thursday"

match day.lower():
    case "monday"| "tuesday"|"wednesday"|"thursday"|"friday":
        print("weekday")

    case "saturday":
        print("saturday")

    case "sunday":
        print("sunday")



#Q12

list=[]

list.append("milk")
print(list)
list.remove("milk")
print(list)

#Q13
import math

def euc_dist(p1,p2):
 x1,y1 = p1
 x2,y2 = p2 

 distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
 return distance

p1 = (0,0)
p2 = (3,4)
print(euc_dist(p1,p2))


#Q14
sent = "the cat sat on the mat"
split=sent.split()
s = set(split)
unique = sorted(s)

print(unique)

# #Q15
# students = {"Alice":64,"vv":99,"abc":34,"we":75,"cd":34}
# for students,marks in students.items():
#   if marks>=50:
#     print("passed")
# else:
#     print("fail")
   
#     print(f"{students}:{marks}")
 
#     average = sum(marks)/len(marks)
# print(average)

#Q16
import random
count=0
for i in range (100):
  dice1= random.randint(1,6)
  dice2=random.randint(1,6)
 
  if dice1+dice2 ==7:
    count+=1
 
print(count)



#Q018
a=5
b="a"

try:
    print(a/b)

except ZeroDivisionError:
    print("cannot divided by zero")

except Exception as e:
    print("invalid input")

#Q019
file = open("example.txt","r")
try: 
    file= open("example.txt","r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: example.txt does not exist.")

except PermissionError:
    print("permission declined")

#20
class Bankaccount():
    def __init__(self,owner,balance=0):
        self.owner =  "abc"
        self.balance = 1000

    def deposit(self,amount):
        if amount<=0:
            raise ValueError ("deposit must be positive")
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("insufficient balance")
        if amount <=0:
            raise ValueError("withdraw amount should be positive")
        
        def get_balance(self):
            return self.balance
        
        def __str__(self):
            return f"owner: {self.owner}, balance: ${self.balance}"

#Q21
class animal():
    def __init__(self,name):
        self.name = name 

    def speak(self):
        pass

class dog(animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says: woof"
    
class cat(animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says: meow"
    
class bird(animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} says: chi chi"
    
animals= [dog("happy"), cat("michain") , bird ("twerty")]
for a in animals:
    print(a.speak())

#022
from abc import ABC , abstractmethod

class shape(ABC):
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class rectangle(shape):
    def __init__(self,length,width):
        self.length =length
        self.width = width 

    def area(self):
        return self.length * self.width
    
class triangle(shape):
    def  __init__(self,base,height):
        self.base = base
        self.height = height 

    def area(self):
        return 0.5*self.base*self.height 
    
#now for the mixed list 
shapes = [circle(5),rectangle(4,6),triangle(3,4)]

for shape in shapes:
    print(shape.area())

#23
with open ("student.txt","w"):

   with open("student.txt","r") as f:
    for line in f:
        name,grade = line.strip().split(",")
        print(f"{name:<15}{grade:<10}")

#24
# error =0
# warning = 0
# info = 0

# with open("app.log","r") as f:
#     for line in f:




#Q25
# import logging
# log = logging.getLogger(__name__) 




 #Q26
players = [("Alice",98),("Bob",92),("Carol",28),("abc",53),("df",34),("xyz",87),("ld",76),("we",56)]
desc =sorted(players,key=lambda x:x[1],reverse=True)
print(desc)
print(desc[:3])

#Q27 
txt = "HI how are you hope you are doing well this time"
lower=str.lower(txt)
sp = lower.split()
freq = {}
for i in sp:
    freq[i] = freq.get(i,0)+1

print(freq)

#Q28
import random

num = [random.randint(1,101) for _ in range(50)]
print(num)  

min = min(num)
max= max(num)
mean = sum(num)/len(num)

count=0
for n in num:
    if n>75:
        count+=1
print("the minimum value is:", min)
print("the maximum value is:", max)
print("the mean of values is:", mean)
print("the count of the numbers is:", count)


#Q34
class book():
    def __init__(self , title): 
        self.title = "ikigai"
        self.available = True

    def __str__(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} title"
    
class member():
    def __init__(self,name):
        self.name = "abc"

    def __str__ (self):
        return self.name
    
class library():
    def __init__(self):
        self.books=[]
        self.borrowed={}

    #for adding book
    def add_book(self,book):
        self.book.append(book)

    #for borrowing book
    def borrow_book(self,member,title):
        for book in self.books:
            if book.title==title and book.available:
                book.available = False
                self.borrowed.setdefault(member.name,[]).append(title)
                return "borrowed!"
            
        return "books not available"
    
    #return book 
    def return_book(self, member,title):
        if member.name in self.borrowed and title in self.borrowed[member.name]:
            self.borrowed[member.name].remove(title)
            for book in self.books:
                if book.title==title:
                    book.available = True
                return "returned!"
        return "invalid return"
    
    #list available
    def available(self):
        return [str(book)for book in self.books if book.available]
    
