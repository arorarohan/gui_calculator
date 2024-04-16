#this will house our calculator functions

#let's start with the basic ones
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "cannot divide by zero! dummy"
    
    return result

def exponent(num1,num2):
    return num1 ** num2

def nth_root(num1,num2):
    return num2 ** (1 / num1)

