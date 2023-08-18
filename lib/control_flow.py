#!/usr/bin/env python3

def admin_login(username, password):
    # your code here"
    if (username == "ADMIN" or username == "admin") and password == 12345: 
        return "Access granted"
    else:
        return "Access denied"
    

def hows_the_weather(temperature):
    # your code here
    if temperature>85:
        return "It's too dang hot out there!"
    elif temperature>40 and temperature<65:
        return "It's a little chilly out there!"
    elif temperature<40:
        return "it;s brisk out there!"
    else: 
        return "It's perfect out there"

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

def calculator(operation, num1, num2):
    # your code here
    if operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    elif operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1-num2
    else:
        return "Invalid operation!"
    
print(admin_login("ADMIN", 12345))
print(hows_the_weather(63))
print(fizzbuzz(15))
print(calculator("*",3,5))
