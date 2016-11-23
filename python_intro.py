# Python Intro Programming for Biologists
# fall 2016

#Maggi Kraft

#1. Write a loop that prints out the numbers from 20 to 10
#range([start], stop[, step])
for i in reversed(range(10, 21)):
    print(i)
    
# 2. Write a list comprehension that returns the numbers from 20 to 10
list_comprehension = [i for i in reversed(range(10,21))]
list_comprehension

# 3. Write a loop that prints out only the numbers from 20 to 10 that are even
for i in reversed(range(10, 21)):
    if i%2 ==0:
        print(i)

# 4. Write a list comprehension that prints out only the numbers from 20 to 10 that are even        
evensList = [i for i in reversed(range(10,21)) if x % 2 == 0]

# 5. Write a function that calculates whether a number is a prime number (hint: what does 2 % 3 give you?)
#if value is less than 2 it won't run. If value is 2 it is prime. For n in range two 2 x if the remainder of x/n is 0 than it isn't prime. If else, it is prime. (basically if it is divisible by anything in the list, it is not prime)
def prime(x):
    if x < 2:
        return "won't work"
    elif x == 2:
        return "prime: value is 2"  
    for n in range(2, x):
        if x % n ==0:
            return "not prime"
    return "PRIME!!!"

    #checking to see if it works
prime(10)

#6. Write a function that loads a text file, loops over the lines in it, and prints out the # fifth character on the fifth line of that file.
# “Hint” (really, frankly, this is the solution):
# with open("name_of_file") as handle:
#for line in handle:
# Do something

#where x is the name of the file?
def load_func(x):
    with open(x) as f:        
        for i, row in enumerate(f):
            if i == 5:
                print(row[5]) 
                
#7. Write a loop that prints out the numbers from 1 to 20, printing “Good: NUMBER” if the number is divisible by five and “Job: NUMBER” if then number is prime, and nothing otherwise.
#the prime part is refering to the prime number function in question 5
for i in range(20):
    if i%5==0:
        print("Good:", i)
    elif prime(i)=="PRIME!!!":
        print("Job:", i)

#8. A biologist is modelling population growth using a Gompertz curve, which is defined as #y(t) = a.e−b.e−c.t where y is population size, t is time, a and b are parameters, and e #is the exponential function. Write them a function that calculates population size at any #time for any values of its parameters.

#importing the math module to run exponents
import math
from math import exp
#defining the equation population growth
def pop_growth(a,b,c,t):
    pop= a*exp(-b)*exp((-c)*t)
    return pop

#testing to see if the equation population growth works
pop_growth(280,100,.4,30)

# 9. Write a function that draws boxes of a specified width and height that look like #this (height 3, width 5):
#****** 
#*
#*****
#(Hint: what does print("*" + "" + "*"*4) give you?)

def star_box(width, height):
 top_bottom= ("*" + "" + "*"*(width-1))
 print("")
 print(top_bottom)
 for k in range(1, height):
  print("*" + " "*(width-2) + "*")
  print("\n")
 print(top_bottom)

#testing the star box function
star_box(5,4)
 
#10. Implement a point class that holds x and y information for a point in space. Note that I am not asking you to plot that line.
class new_pts:
    def __init__(self,x,y):
     self.x=x, self.y=y
     

#11. Write a distance method that calculates the distance between two points in space.
from math import sqrt
class Point:
    def __init__(self,x,y):
     self.x=x, self.y=y
     
#where point 1 is p1 and point 2 is p2     
    def Distance(Point2):
        dif= sqrt(((self.x-Point2.x)**2)+((self.y-Point2.y)**2))
        print(dif)


# 12. Implement a line class that takes two point objects and makes a line between them. Note that I am not asking you to plot that line.
class new_line:
    def __init__(self, pt1, pt2):
     self.pt1 = Point(pt1.x, pt1.y1)
     self.pt2 = Point(pt2.x,pt2.y)
     


