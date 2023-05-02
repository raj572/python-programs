#Hard coding

'''
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
myobj=MyClass("honey",28)
myobj.greet()

'''

#soft coding

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
        
name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = Person(name, age)
person.greet()
'''
class Adder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

adder = Adder(num1, num2)
result = adder.add()

print(f"The sum of {num1} and {num2} is {result}.")

        