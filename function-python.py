#function python

#simple custom function
def first_function():
    print("hello, good morning")

first_function()

'==================================='

def greet_function(name):
    print("Hey, "+ name +". Good Afternoon!")

greet_function('ukon')

'===================================='
#list function

vowels=['i','u','a','o','e']
vowels.sort(reverse=True)
print('sorted list with reverse : ',vowels)

'====================================='

flowers=['Rose','Lily','Jasmine']
flowers.append('Lotus')
print(flowers)

('=====================================')

#Nested function
def outer_function():
    print("This is the outer function :)")
    def inner_function():
        print("This is the inner function :D")
    inner_function()
outer_function()
#inner function can be called if outer function is called

'==============================================='

#lambda vs function
triple=lambda x: x*3
print(triple(5))

x=3
def triple_function(x):
    return x*3
triple_function(5)

'================================================'

#Square Root math
import math
x=math.sqrt(9)
y=math.sqrt(25)
print(x,y)

#exponential
x=pow(2,3)
y=pow(6,2)
print(x,y)

('================================================')



#Notpure Function
def crop_func(z):
    del z[0]
    return z

def print_val():
    a=[1,2,3]
    b=crop_func(a)
    print(b)
    print(a)

print_val()

#Pure Function
def crop_func(z):
    return z[1:]

def print_val():
    a=[1,2,3]
    b=crop_func(a)
    print(b)
    print(a)

print_val() #values a not changed :)

'================================================='

#Bool Function
a='Hello'
b=15
c=0
sample_list=[]

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(sample_list))

#NUll is False

'======================================'

#Convert List into String
demo=['sun','mon','tue','wed','thu','fri','sat']
con_str=' '.join(demo)
print(con_str)

#Convert list into tuple
list_demo=['sun','mon','tue','wed','thu','fri','sat']
con_tup=tuple(list_demo)
print(con_tup)

#Convert list into set
list_demo=['sun','mon','tue','wed','thu','fri','sat']
con_set=set(list_demo)
print(con_set)

'==========================================================='

#list comprehension

#make list
a=[2,3,5,7,9]
b=[]
for x in a:
    b.append(x*4)
print(b)
#atau
c=[x*4 for x in a]
print(c)

#make even numbers list
even=[i**2 for i in range(10) if i**2%2==0]
print(even)

#make odd numbers list
odd=[i for i in range(20) if i%3==0 and i%5!=0]
print(odd)


'========================================================='

#format function
print('{0} memiliki minat dengan {1}'.format('ukon','desain'))

from datetime import datetime
now=datetime.now()
jam=now.hour
menit=now.minute
detik=now.second
print("sekarang menunjukkan jam {}:{}:{}".format(jam,menit,detik))

'============================================================='

#Recursion Function
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Example Results")
tri_recursion(3)

def factorial(a):
    if a==1:
        return 1
    else:
        return (a * factorial(a-1))
input_number=3
print("The factorial of",input_number,"is",factorial(input_number))

'=========================================================================='

