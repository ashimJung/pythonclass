#type of function are 2
#1. built in function
#2. user defined function
#example of in built function
print("hello world")

#example of user defined function
def my_function():
    print("hello world")
    my_function()
    
 # how to perform calculation within function   

def calculation():
    a=10
    b=20
    c=a+b
    print(c)
calculation()

#how to return any operation frim function
def returningFunction():
    num1 = 80 
    num2 = 200
    return num1+num2
return_data = returningFunction()
print(return_data)

#how to send parameter as an argument of function and perform operation

def parameterFunction(num1,num2,num3,name):
    print(num1)
    print(num2)
    print(num3)
    print(name)

num1=input("enter Num 1:")
parameterFunction(num1,40,100,'Ram')

#how to perform operation inside function using parameters
def paraFunction(name,year):
    print('The user name is',name)
    current_year=2024
    real_age=current_year-int(year)
    return real_age

   
name=input("enter your name:")
age=input("enter your age:")

real_birth_year=paraFunction(name,age)
print("Your birth year is",real_birth_year)

#how to handle arbitary arguments
def arbiFunction(*args):
    selected_user=['ram','shyam']
    print(args)
    for i in args:
        if i in selected_user:
            print('Selected user argument found',i)

arbiFunction('ram','shyam','hari','sita',10,20,30)

#how to handle keyword argument
def keFunction(**kwargs):
    print(kwargs)

keFunction(name1='Ashim',name2='Hari')

#default value function
def defaultValueFunction(country="Nepal",city="kathmandu"):
    print('Your country is', country)
    print('Your city is', city)

defaultValueFunction(country="japan")

#how to define and access global variable
street='Jorpati'

def globalchangeFunction():
    global street
    street='chabahil'
    print(street)

globalchangeFunction()

print(street)



    