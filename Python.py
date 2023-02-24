#!/usr/bin/env python
# coding: utf-8

# In[1]:


price =10
price=20
rating =1.4
print(rating)


# In[2]:


full_name = 'John Smith'
age=20
is_new =True
print(full_name)
print(age)
print("Is this new patient?", is_new)




# In[3]:


name = input ('what is your name? ')
print('Hi '  + name)


# In[4]:


name = input ('what is your name? ')
favourite_color = input(' which is your favourite color? ')
print (name + ' likes '  + favourite_color)


# In[5]:


birth_year =int(input( 'Birth Year:  '))
current_year =int(input('Enter Current year'))
age = 2023 -int(birth_year) 
print(age)


# In[7]:


weight_lbs =input('Enter your Weight(lbs):  ')
weight_kg =int(weight_lbs)*0.4
print(weight_kg)


# In[8]:


course ='Python for Beginners'
print(course)


# In[9]:


course =''' hi

my name is parwinder

I am 24 years old

'''
print (course)
 


# In[10]:


course ="Python's course  for Beginners"

print(course[0])


# In[11]:


course ="Python's course  for Beginners"

print(course[-1])


# In[12]:


course ="Python's course  for Beginners"

print(course[:5])


# In[13]:


course ="Python's course  for Beginners"

print(course[2:5])


# In[14]:


course ='Python for Beginners'
another = course[:]

print(another)


# In[15]:


name ='Jennifer'
print(name[1:-1])


# In[16]:


First = 'Parwinder'
Last = 'Maan'
message =f" first + '['+ last +']' is a code"
msg = f'{First} [{Last}] is a coder'
print(msg)


# In[17]:


course = 'Python for Beginners'
print(len(course))


# In[18]:


course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course)
print(course.find('P'))
print(course.find('o'))
print(course.find('Beginners'))
print(course.replace('Beginners','Absolute Beginners')) 
print(course.replace('P','J'))
print('Python' in  course)
print('python' in  course)


# In[19]:


print (10+3)
print (10-3)
print(20*3)
print(10/3)
print(10//3)
print(10%3)
print(10**3)


# In[20]:


x=10
x=x+3
x+=3
x-=3
print(x)


# In[21]:


x =(10+3)*2**2
print(x)


# In[22]:


x=(2+3)* 10 -3
print(x)


# In[23]:


x=2.9
print(round(x))
print(abs(x))
print(abs(-2.9))


# In[24]:


import math
print(math.ceil(2.9))
print(math.floor(2.9))


# In[25]:


is_hot =True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")


# In[26]:


is_hot =False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")


# In[27]:


is_hot =False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")


# In[28]:


is_hot =False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")


# In[29]:


is_hot =True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")


# In[30]:


is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


# In[31]:


house_price =1000000
has_good_credit =True
if has_good_credit:
    down_payment =0.1 * price
else:
    down_payment =0.2 *price
print(f"Down Payment: {down_payment}")


# In[32]:


has_high_income =True
has_good_credit =True


if has_high_income and has_good_credit:
    print("eligible for loan")

    


# In[33]:


has_high_income =False
has_good_credit =True


if has_high_income and has_good_credit:
    print("eligible for loan")

    


# In[34]:


has_high_income =False
has_good_credit =True


if has_high_income or has_good_credit:
    print("eligible for loan")

    


# In[35]:


has_high_income =True
has_good_credit =False


if has_high_income or has_good_credit:
    print("eligible for loan")

    


# In[36]:


has_good_credit =True
has_criminal_record =False



if has_good_credit and not has_criminal_record:
    print("eligible for loan")

    


# In[37]:


temperature =35
if temperature>30:
    print("It's a hot day")
else:
    print("It's not hot day")


# 
# 

# In[38]:


name = 'Parwinder'

if len(name)<3:
    print("name must be of 3 characters")
elif len(name)>50:
    print("name must be at least 50 characters")
else:
    print("name looks good")


# In[39]:


i=1
while i <=5:
    print(i)
    i = i+1
print("Done")


# In[40]:


i=1
while i <=5:
    print('*' *i)
    i = i+1
print("Done")


# In[41]:


secret_number =9
i=0
while i < 3:
    guess = int (input ('Guess:  '))
    i  +=1
    if guess == secret_number:
        print('YOU WON!')
        break
        
else:
    print('You failed')
    


# #for loops >string:- it is a collection of characters.
# we use for loop to iterative over collection of characters 
# and in each iteration variable will hold one item

# In[42]:


for item in 'Python':
    print(item)


# In python we define list by using square brackets:
# >it could be list of numbers ,list of emails ,list of names

# In[43]:


for item in ['Pam','Babal','Veer']:
     print(item)


# In[44]:


for item in [1,2,3,4,5]:
    print(item)


# In[45]:


for item in range(10):
    print(item)


# for counting rather using 1,2,3,4,5,6,7,8,9,10 upto so on we could use range for this for example range upto(10)

# In[46]:


for item in range (5,10):
    print (item)


# for two steps forward we could use (5,10,2):
#     it will print 5,7,9

# In[47]:


for item in range (5,10,2):
    print(item)


# In[48]:


prices = [10,20,30]
sum=0
for price  in prices:
    sum +=price
print(f"sum:{sum}")


# nested loops in python means:- Adding one loop instead of another loop
# #with the help of this we could easily generate coordinates as we know its combination of (x,y) and(0,0) and so on....

# In[49]:


for x in range(4):
    for y in range (3):
        print(f'({x},{y})')


# In[50]:


numbers=[5,2,5,2,2]
for x_count in numbers:
    print('x' * x_count)
    

    


# numbers=[5,2,5,2,2]
# for x_count in numbers:..>x_count here we defined a variable called output and intially we set this as empty string and we use another loop for count in range of x_count and here we use range function to generate a sequence of numbers from 0 upto x_count and then in first iteration range generate numbers 0,1,2,3,4,5 upto X_count.
# *and in inner loop we excute this 5 times and now each iteration append AN X to our output variable.so we set
# Output +='x' and then after this inner loop we simply print(output )
# with this we'll print 5 x's on the first row. then we go to the second iteration of our outer loop.
# 

# In[51]:


numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for x in range(x_count):
        output+='x'
    print(output)


# lists ---In this we willl took closure look on the lists like list of names,
# in b/w the square brackets there we have our items in b/w the square brackets  
# 

# In[52]:


names=['John','Bob','Mosh','Sarah','Mary']
print(names)


# and here, we have type out square brackets and specify an index.

# In[53]:


names=['John','Bob','Mosh','Sarah','Mary']
print(names[0])


# In[54]:


names=['John','Bob','Mosh','Sarah','Mary']
print(names[-1])


# In[55]:


names=['John','Bob','Mosh','Sarah','Mary'] 
print(names[2:4])
print (names)


# in the upper code we get values mosh and sarah because it print the values upto 4 without including value of 4 item.
# ###### and for replacing the number we will use simply names[0]=Jon

# In[56]:


numbers=[2,4,6,1,9]
print(max(numbers))


# for finding the largest number in list use max function.

# In[57]:


numbers=[2,5,6,8,10]
max=numbers[0]
for number in numbers:
    if number > max:
        max=number
print(max)
     
  


#  list methods: In this we can add new numbers in the list, and we can delete any number from the list ,and we could insert any number in the middle of the list.
#  mor adding new number in the list at the end we use append
#   like numbers.append(20)
#   for adding new number in the list in the middle we use insert 
#   for example numbers.insert(30)
#   for deleting any number from the list we use remove 
#   for example numbers.remove (4)enter which number we want to remove from the list.
#   and if we want to remove all the numbers from th list we use clear for that.and thia method doesn't take any value.
#   and we use pop for removing letter from the end of the list.

# In[58]:


numbers = [5,2,1,7,4 ]
numbers.append(20)
print(numbers)


# In[59]:


numbers = [5,2,1,7,4 ]
numbers.insert(0,10)
print(numbers)


# In[60]:


numbers = [5,2,1,7,4 ]
numbers.insert(3,10)
print(numbers)


# In[61]:


numbers = [5,2,1,7,4 ]
numbers.clear()
print(numbers)


# In[62]:


numbers = [5,2,1,7,4 ]
numbers.pop()
print(numbers)


# numbers = [5,2,1,7,4 ]
# print(numbers.index(50))
# this will show error like 50 is not in the list instead of this we have another method for this.

# In[63]:


numbers =[5,2,1,7,4]
print(50 in numbers)


# In[64]:


numbers =[5,2,1,7,4]
print (numbers.sort())


# with this method it doesn't return any value instead of using this we will use another method for this

# In[ ]:


numbers =[5,2,1,5,7,4]
numbers.sort()
numbers.reverse()
print(numbers)


# In[19]:


numbers =[5,2,1,5,7,4]
numbers2 =numbers.copy()
numbers.reverse()
print(numbers)


# In[ ]:


n=[2,3,5,7,6,8,5,9,4]
result=[*set(n)]
print('numbers after removing duplicacy',result)


# In[ ]:


numbers =[2,2,5,6,4,3,8,4]
uniques =[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# #tuples

# In[ ]:


numbers=(1,2,3)
print(numbers[0])


# #UNPACKING ----and next define tuples are called coordinates.and here we pass values

# In[ ]:


coordinates =(1,2,3)
x,y,z=coordinates
print(y)


# #unpacked this list into three variables.

# #DICTIONARIES--DICTIONARIES IN PYTHON we use in various situations where we want to store information that comes as key value pairs. here's. like 
# name=pam
# email-pam@gmail.com
# phone no-6453
# in this names are keys and each key has some values.so, this is called key value pairs.

# In[66]:


customer ={
    "name":"parwinder",
    "age":24,
    "is_verified":True}
                                 
print(customer["name"])


# #Here we are going to check this key-pair 

# In[65]:


customer ={
     "name":"parwinder",
     "age":24,
     "is_verified":True}
                                  
print(customer.get("birthdate" ))


# it is print this key-pair doesn't contain this value

# In[ ]:


customer ={
     "name":"parwinder",
     "age":24,
     "is_verified":True}
                                  
print(customer.get("birthdate","August 17 1998"))


# instead of getting none we will add default value thn it will print that.

# In[ ]:


customer ={
     "name":"Parwinder Maan",
     "age":24,
     "is_verified":True}
customer["name"] =  "Pam Maan"
print(customer["name"])


# here we could easily add new key in this .

# In[ ]:


customer ={
     "name":"Parwinder Maan",
     "age":24,
     "is_verified":True}
customer["birthdate"] =  "17 august 1998"
print(customer["birthdate"])


# In[ ]:


phone=input("Phone:  ")
digits_mapping ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "is_verified":True,
} 
output =""
for ch in phone:
    output += digits_mapping.get(ch,"!") +" "
print(output)


# In[17]:


## my list="India is my country"
#Q1 country my is India
#Q2 aidnI si ym yrtcuon 
#Q3 yrtnuoc tearg ym si aidnI
#Q4 make a list with alternate words

mylist =['India ','is ','my ','country ']
re=(mylist [::-1])
st=''.join(re)
print(st)


# In[63]:


#Q3.yrtnuoc tearg ym si aidnI
my_list= "India is my country"
re=my_list[::-1]
ra=re.split(" ")
ra1=ra[::-1]
tn=' '.join(ra1)
print(tn)
# new=(tn)
# st=(new[::-1])
# i=''.join(st)
# print(re1)


# In[3]:


#Q.2 aidnI si ym yrtcuon
my_list=['India ', 'is ', 'my ', 'country ']
my_list1=my_list.copy()
my_list1.reverse()
st=''.join(my_list1)
print(st)


# In[65]:


my_list= "India is my great country"
re=my_list[::-1]
print(re)


#  #EMOJI CONVERTER 

# In[13]:


message = input(">")
words=message.split(' ')
emojis = {
    ":)": "😄",
    ":(": "😒"
    
}
output=""
for word in words:
    output += emojis.get(word, word) + " "
print(output)


# #Functions
# #for printing a greeting messages
# #naming a variable with lower case characters and  naming u r variable also apply here in this we defining a function grret_user and it is followed by colon (:)and whenever we add colon at the end of the line so we defining a block of code and the n we press enter the next line is intended so  any code we will write here that is belong to that function
# 

# In[16]:


def greet_user():
    print('Hi there!')
    print('welcome aboard')
    
    
print("Start")
greet_user()
print("Finish")

#put these two lines in functions and here we use def reserve keyword for defining a function then function name here greet is the function name


# Execution of these two lines which we enter in the function is depend on the function 
# *and important thing is that we could call this after define it we can't call this before defining  

# In[25]:


def greet_user(first_name,last_name):#passing parameters in paranthesis,,,and we could pass more than one parameter at same time
   # name='Pam' we don't need to print name here because we used it as parameters
    print(f'Hi {first_name}{last_name}!')# f string
    print('welcome aboard')
    
    
print("Start")
greet_user("PAM ","Maan")#if we remove this name from here it will show an error
greet_user("Babl ","Maan")
print("Finish")


# In[28]:


def greet_user(first_name,last_name):
    print(f'Hi {first_name}  {last_name}!')
    print('welcome aboard')
    
    
print("Start")
greet_user(" Maan "," Pam ")#if we change the position it will print it like that 
print("Finish")


# #In this we will learn how we could value even we change values bt get actual result which we want for that we will use different keyword argument

# In[32]:


def greet_user(first_name,last_name):
    print(f'Hi {first_name} {last_name}!')
    print('welcome aboard')
    
    
print("Start")
greet_user(first_name="PAM",last_name="Maan")#here we ae going to use keyword argument for these positional argument
print("Finish")


# def greet_user(first_name,last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('welcome aboard')
#     
#     
# print("Start")
# greet_user(first_name="PAM","Maan")
# #this keyword argument always come after positional argument
# print("Finish")
# 

# In[41]:


def square(number):
    print(number* number)#if we use print while using return value thenn python retuen none value by default
     #by default all values in python return None value for this we could use return thn it will not return None 

#result=square(3)#we could also pass this argument simply instead of using separate variable.
print(square(3))


# In[42]:


def square(number):
       return(number* number)
   
   
print(square(3))


# In[74]:


#creating a reusable function
def emoji_converter(message):
    words=message.split(' ')
    emojis = {
          ":)": "😄",
          ":(": "😒"
    
         }
    output=""
    for word in words:
        output += emojis.get(word ,word) + " "
    return (output )

message  = input(">")
print(emoji_converter(message))




# In[77]:


try:
    age = (input('Age: '))
    print(age)
except ValueError:
        print('Invalid value')


# In[85]:


try:
    age = int(input('Age: '))
    print(age)
except ValueError:
        print('Invalid value')


# In[82]:


age = int (input('Age: '))
print(age)
#in this if we will enter any non-numeric value than it will print value  error.
#for solving this problem we will use another method which i had already done in the upper codes by using try and except


# In[90]:


try:
    age = int(input('Age: '))
    income =20000
    risk = income / age
    print(age)
##we cant divide this with zero it will return an error regarding to division because we cant divide any number by zero
#for solving this we have to use another except      
except ZeroDivisionError:
    print('Age cannot be 0.')
except ValueError:
        print('Invalid value')
        


# 

# In[92]:


#comments in python
#nnnnnnnnnnn
#we could write anything in the comments about our code by using#and then write anything 
#it doesn't effect our code
#nnnnnnnnnnn


#we also talk about the bad comments here
#like (sky is blue) it is obivous which i'm going to print in the next line
print("sky is blue")



#we could add comments in front of the functions
#calculates and returns the square of the num
def  square number():
    return number*number

#these kind of comments are looking bad because we know this is going to be done



# ## classes:- classes are extremely important in python --in this video 
# 

# In[2]:


#Numbers 
#string
#booleans
#---
#Lists
#Dictionaries


# In[11]:


class Point:
    def __init__(self, x, y):#this method is used to construct and to create an object.
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")

#to create an object we use name of the calss
#for methods
#point1 = Point()
#point1.x=10
#point1.y=20
#print(point1.y)
#point1.draw()

#point2=Point()
#point2.x =1

#print(point2.x)
#point2.draw()


point = Point(10, 20)
print(point.x)



# In[10]:


print("mosh")
print('0----')


# In[5]:


class Person:
    def __ init__(self, name):
        self.name = name
        
    def talk(self):
        print( 'talk')

        
person_1 = Person("Parwinder Maan")
print(self.name)
parwinder.talk()



# In[2]:


#Inheritance
class Mammal:
    def walk(self):
        print("walk")
        
        
class Dog(Mammal):
    pass


class Cat(Mammal):
     def be_annoying(self):
            print("annoying")

dog1 = Dog()
dog1.walk()

    


# In[3]:


class Employee:
    pass
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Parwinder'
emp_1.last = 'Maan'
emp_1.email = 'Parwinder.Maan@gmail.com'

emp_2.first = 'Gurpreet'
emp_2.last = 'Thind'
emp_2.email = 'Gurpreet.Thind@gmail.com'

print(emp_1.first)
print(emp_2.email)
print(emp_1.email)


#add data manually
 


# In[12]:


class Employee:
    def __init__(self, first, last, pay): #instance variable
        self.first = first
        self.last = last
        self. pay = pay
        self.email = first + '_' + last + '@gmail.com'
        
        
        
        
        
emp_1 = Employee('Parwinder','Maan', ' 50000')
emp_2 = Employee('Gurpreet','Thind','60000')

print('{} {} {}'.format(emp_1.first, emp_1.last, emp_1.pay))


# In[16]:


class Employee:
    def __init__(self, first, last, pay): #instants variable
        self.first = first
        self.last = last
        self. pay = pay
        self.email = first + '_' + last + '@gmail.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
        
emp_1 = Employee('Parwinder','Maan', ' 50000')
emp_2 = Employee('Gurpreet','Thind','60000')

print(emp_1.email)
#print(emp_2.fullname())

emp_1.fullname()
print(Employee.fullname(emp_1))


# In[ ]:




