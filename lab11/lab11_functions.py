"""
Sally Han
April 27, functions
"""
#  import 'math' module
import math 

username  = "Default user"
#  example 3 :
def greeting():
    print(f"Welcome to function  {username}")

# example 4 :
def printusername(username):
    print(f"Welcome to function {username}")

# example 5 : function with default paramenters
def user_country(username="(no name)", country="USA"):
    print("f{username} is living in {country}")
    return # void function

# example 6 : function that returns a value
# function  that takes two numbers and return the product of them
def product(n1=0, n2=1):
    return n1*n2

# example 7: Boolean function
# function to check if a number a multiple of 3
def miltiple3(n):
    if n %3 == 0 and n!=0:
        return True
    else:
        return False     

# example 8: composition function
# define function to collect, validate, and return a number between 1 and 9
def collectnum():
    n = float(input("Enter a number between 1 and 0(inclusive)"))  #collect
    while(not( 1 <= n <= 9)):
        n = float(input("Re-enter  a number again: ")) # Validate
    return n # Return

# function that adds 'totalnumbers' amount of numbers returns the sum of the numbers.
def sumnumbers(totalnumbers):
    sum = 0
    for n in range(totalnumbers):
        sum += collectnum() # composition function
    return sum

# function to print result
def printresult(totalsum):
    print(f"Sum of all numbers is = {totalsum}")
        
# example 9 built-in function
# define a function to calculate and return the area of a circle
# formular = radius^2 * pi
def areacircle(radius):
    a = math.pow(radius,2) * math.pi
    return round(a,2)

#  function to print result
def areaprint(area, radius=0):
    print(f"The area of a circle with {radius} radius is {area}")



