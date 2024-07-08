#to define class
class MyCollege:
  x='Ram'

obj = MyCollege()
print(obj.x)

#this is how we create class with constructor

class ClassWithCons:
  def __init__(self):
    print('This is being called when initializing object')

obj1=ClassWithCons()

#this is how we pass paramete(data) to class
class ClassWithData:
  def __init__(self,name,address):
    self.name=name
    self.address=address
    
    print(self.name)
    print(self.address)

obj2=ClassWithData('Ram',"dang")

#this is how we add multiple function in a class
class multipleFunctionClass:
    def __init__(self,name,age,address):
      self.name =name
      self.age=age
      self.address=address

    def printName(self):
      print(self.name)

    def printAge(self):
      print(self.age)

    def printAddess(self):
      print(self.address)

obj3=multipleFunctionClass('Kunjan',18,'Bhaktapur')
obj3.printName()
obj3.printAge()
obj3.printAddess()

#calculator using class
class Calculator:
    def __init__(self, num):
        self.number = num
        self.amt = 0
        self.splited_data = None

    def sumFunction(self):
        self.amt = int(self.splited_data[0]) + int(self.splited_data[1])
        print(self.amt)

    def subFunction(self):
        self.amt = int(self.splited_data[0]) - int(self.splited_data[1])
        print(self.amt)

    def mulFunction(self):
        self.amt = int(self.splited_data[0]) * int(self.splited_data[1])
        print(self.amt)

    def divFunction(self):
        self.amt = int(self.splited_data[0]) / int(self.splited_data[1])
        print(self.amt)

    def splitFunction(self):
        if '+' in self.number:
            self.splited_data = self.number.split('+')
            self.sumFunction()
        elif '-' in self.number:
            self.splited_data = self.number.split('-')
            self.subFunction()
        elif '*' in self.number:
            self.splited_data = self.number.split('*')
            self.mulFunction()
        elif '/' in self.number:
            self.splited_data = self.number.split('/')
            self.divFunction()

# Calculator usage loop
while True:
    input_number = input("Enter the number (or type 'exit' to quit): ")
    if input_number == 'exit':
        break
    else:
        calc = Calculator(input_number)
        calc.splitFunction()

#inheritance in class
class ParentClass:
   def __init__(self, name):
      self.name=name
      self.class_type='BIT'
      print('This is parent class')

   def printName(self):
      print(self.name)

      #here we inherit the parent class
class ChildClass(ParentClass):
   pass
obj1=ChildClass('Ashim')
print(obj1.class_type)
obj1.printName()

#class parent2
class Parent2:
   def __init__(self,name,age):
      self.name=name
      self.age=age

      print('This is being called parent class')
      print(f"{self.name}{self.age}")

class Child2(Parent2):
   def printNumber(self):
      print('This is number')

obj3=Child2('bibek ','bouddha')
obj4=Child2('ram ','sindhuli')
obj5=Child2('sam ','chabahil')

import math

print(math.sqrt(300))