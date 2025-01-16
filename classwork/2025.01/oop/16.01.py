class Cat():
    def __init__(self, _name, _color):
        self.name = _name
        self.color = _color
    def meow(self):
        return "Мяу"
    
cat = Cat("снежок", "белый")
print(cat.meow())

import math
class Circle():
    def __init__(self, _radius):
        self.radius = _radius
    def area(self):
        return math.pi * math.pow(self.radius, 2)
    def circumference(self):
        return math.pi * (2 * self.radius)
    
circle = Circle(10)
print(circle.circumference())

class Book():
    def __init__(self, _title, _author):
        self.title = _title
        self.author = _author
    def getInfo(self):
        return f"Название: {self.title}, Автор: {self.author}"
    
book = Book("Гарри поттер", "Дж. Роулинг")
print(book.getInfo())