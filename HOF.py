#Higher order functions, composing functions, and brain fuckery

#---------------------------------------------#
def compose(f, g):
    return lambda x: f(g(x))

thrice = lambda f: compose(compose(f, f), f)
#print(thrice(lambda x: x+1)(6))

#---------------------------------------------#
def times3(x):
    return x * 3

def add1(x):
    return x + 1

def compose(f, g):
    return lambda x: f(g(x))

three_x_plus_1 = compose(add1, times3)
#print(three_x_plus_1(3)) #10 = 3(3) + 1
#---------------------------------------------#

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add1 = make_adder(1)
#print(add1(5)) #6
#---------------------------------------------#
def is_same(x, y):
    return x == y #check if two things equal, return T/F

def make_verifier(key):
    def verify(input):
        return is_same(input, key) #returns T/F
    return verify

check_password = make_verifier(262010771)

#print(check_password(111111))
#Result: False
#print(check_password(262010771))
#Result: True
"""
What actually happens here is that make_verifier returns the inner verify function 
(with the key set to 262010771), and that function is stored in the variable check_password. 
When you later call check_password, you're actually calling that returned inner function 
with access to the key due to the closure.
"""
#---------------------------------------------#
def product(f, n):
    result = 1
    for i in range(n+1):
        result *= f(i)
    return result

def factorial(n):
    return product(lambda x: x+1, n-1)

def exponent(x, n):
    return product(lambda _: x, n)

#print(factorial(5))
print(exponent(3, 5))
#---------------------------------------------#
import random

#generate random 4 digit number
def generate_random_4d_number():
     return int(random.random() * 10000)

#print(generate_random_4d_number())