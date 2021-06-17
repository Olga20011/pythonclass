
x=[100,110,120,130,140,150]
for i in x:
    print(i*5)

def divisible_by_three(n):
    x=range(1,n)
    for i in x:
        if (i%3==0):
            print (i)
divisible_by_three(5) 

def flatten():
    x=[[1,2],[3,4],[5,6]]
    y=list(x)
    print(y)
flatten()    

def smallest():
    x=[2,1,5,6,4,7,8]
    for num in x:
        return x.sort()
smallest()    

def letters(x):
    x=["a","b","a","e","d","b","c","e","f","g","h"]
    y=set(x)
    print(y)

    w=list(y)
    print(w)

letters(['a','b','a','e','d','b','c','e','f','g','h'])    

def divisible_by_seven():
    x=range(100,200)
    for num in x:
        if num%7==0:
            print(num)
divisible_by_seven()            

# students=[{"age":19,"name":"Eunice"},
# {"age":21,"name":"Agnes"},
# {"age":18,"name":"Teresa"},
# {"age":22,"name":"Asha"}]
# for i in students:

import math
    
class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length 

    def area(self,width,length):
        Area=width*length
        return Area

    def perimeter(self,length,width):
        p=2*(length+width)
        return p  

    
# rectangle1=Rectangle(2,10)
# rectangle1.area(2,10)

# rectangle1.perimeter(10,2)
