''' 
anything that begins with a #is a comment
comments are code that doesn't get executed
'''

'''
print('hello world')
var1 = 'hello'
var2 = 'world'
var3 = var1 + ' ' + var2
print(var3)


# for integers, python is always going to give yo exact results
# there are no size limits
# the type of a number with no period is called an int
x = 1
y = 5
z = 5**999 # 5 raised to he power of 999
#print(z)

# non-integer numbers are approximations
# type of number witch a period is called a float
x = 0.1
y = 0.1
z = 0.1
q = x + y + z
print(q)

# the last type is the str = "string" type, for strings
# python is an "untyped language" becasue we can change type whenever you want
'''
#import = keyword; math = package or library we are importitng
import math
'''
#psuedocode for the quadratic formula
# (-b +- sqrt(b**2 - 4ac))/2a

a = 5
b = 100
c = 2
quadratic = (-b + math.sqrt(b**2-4*a*c))/2*a

print (quadratic)

a = 3
print(quadratic)
quadratic = (-b + math.sqrt(b**2-4*a*c))/2*a
print (quadratic)

#functions + variables are he key difference between Python and HTML/CSS
'''
'''
quadratic = 0 
def quadratic(a,b,c):
    quadratic = (-b + math.sqrt(b**2-4*a*c))/2*a
    # don't print in the function
quadratic(2,500,5)
print(quadratic)
'''

quadratic = 0 
def quadratic2(a,b,c):
    quadratic = (-b + math.sqrt(b**2-4*a*c))/2*a
    # don't print in the function
quadratic2(2,500,5)
print(quadratic)



'''def quadratic(a,b,c):
    return (-b + math.sqrt(b**2-4*a*c))/2*a
    # don't print in he function

print(quadratic(2,500,5))
'''
'''
quadratic_formula # this is called snake case
quadraticFormula > this is called camel case
python is snake case
'''