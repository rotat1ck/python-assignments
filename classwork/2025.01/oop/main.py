# 3 принципа ООП (Объектно-ориенторованное-програмирование)

# 1. Инкапсуляция - процесс создания функций внутри класса,
# которые могут быть вызваны только через экземляр класса

# 2. Полиформизм - изменения поведения метода класса 
# при его наследовании

# 3. Наследование - процесс передачи всех свойств и методов от 
# родительского класса к дочернему

# Основной единицей в ООП является класс

# Класс - объект, который описывает определенную сущность 
# через свойства и методы

# Метод - функция, созданная внутри класса

class Car:
    # self - это обращение к классу 
    # он нужен чтобы связать функцию с классом
    
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        
    def startEngine(self):
        self.started = True
        return "Машина заведена"
        
    def shutEngine(self):
        self.started = False
        return "Машина заглушена"

# car = Car(model = "Tesla Model S", year=2024, color = "White")
# print(car.model)
# print(car.year)
# print(car.color)

# print(car.startEngine())
# print(car.shutEngine())


class Animal:
    def __init__(self, animalType, isWild):
        self.animalType = animalType
        self.isWild = isWild
        
    def introduce(self):
        return f"Это животное типа: {self.animalType}"
    
class Lion(Animal):
    def __init__(self, animalType, isWild, place, age):
        super().__init__(animalType, isWild)
        self.place = place
        self.age = age

lion = Lion(animalType = "Лев", isWild = True)
print(lion.introduce())