class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return "Гав-гав!"
    
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getP(self):
        return (self.width*2) + (self.height*2)
    
    def getS(self):
        return self.width * self.height
    
class BankAccount():
    def __init__(self):
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Недостаточно средств"
        else:
            self.balance -= amount
            
class Animal():
    def eat(self):
        return "Ем"
    
    def sleep(self):
        return "Сплю"
    
class Cat(Animal):
    def meow(self):
        return "Мяу!"
    
cat = Cat()
print(cat.sleep())

class Shape():
    def area(self):
        return 0
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * math.pow(self.radius, 2)

class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
circle = Circle(10)
print(circle.area())