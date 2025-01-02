users = [
    {id: 1, 'name': 'Ivan', 'last_name': 'Ivanov', 'isActive': True, 'age': 22},
    {id: 2, 'name': 'Petya', 'last_name': 'Petrov', 'isActive': False, 'age': 30},
    {id: 3, 'name': 'Vasya', 'last_name': 'Vasilyev', 'isActive': True, 'age': 40},
    {id: 3, 'name': 'Vladimir', 'last_name': 'Viktorov', 'isActive': False, 'age': 50},
    {id: 5, 'name': 'Ivan', 'last_name': 'Alexseyev', 'isActive': True, 'age': 18},
    {id: 2, 'name': 'Alexandr', 'last_name': 'Familiya', 'isActive': False, 'age': 35},
]

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  


def choose():
    print("\nИмена пользователей (1)\nИнформация о пользователях (2)\nСредний возвраст (3)")
    print("Количество активных пользователей (4)\nПроверка идентификаторов (5/6)\nПроверка имен (7)\nАктивность пользователей (8)")
    tasknum = int(input('\nВведите номер проверки: '))
    if tasknum == 1: getNames(users)
    elif tasknum == 2: getInfo(users)
    elif tasknum == 3: averageAge(users)
    elif tasknum == 4: activeUsers(users)
    elif tasknum == 5: idChecker(users)
    elif tasknum == 6: uniqueIds(users)
    elif tasknum == 7: uniqueNames(users)
    elif tasknum == 8: isActive(users)
    else: 
        print('Некорректный ввод')
        choose()

def getNames(users):
    clear()
    
    for line in users:
        print(line.get('name'))
    
    choose()


# Второе и третье задание в одном
def getInfo(users):
    clear()
    
    for line in users:
        name = line.get('name')
        lastName = line.get('last_name')
        age = line.get('age')
        status = 'Активен' if line.get('isActive') else 'Неактивен'
        
        print(f"Имя пользователя - {name} | Фамилия - {lastName} | Возраст - {age} | Cтатус - {status}")
        
    choose()


def averageAge(users):
    clear()
    
    ageSum = 0
    
    for line in users:
        ageSum += line.get('age')
        
    print(f"Средний возвраст пользователей - {ageSum / (users.index(line)+1)}")
    
    choose()


def activeUsers(users):
    clear()
    
    activeCount = 0
    
    for line in users:
        if line.get('isActive'):
            activeCount += 1 
            
    print(f"Количество активных пользователей - {activeCount}")
    
    choose()


def idChecker(users):
    clear()
    
    idlist = []
    checkFlag = True
    
    for line in users:
        userid = line.get(id)
        
        if userid not in idlist:
            idlist.append(userid)
        else:
            checkFlag = False
            print(f"Повторяющийся идентификатор | Строка - {users.index(line)+1}, Имя - {line.get('name')} {line.get('last_name')}")
    
    if checkFlag:
        print('Нет повторяющихся идентификаторов')
        
    choose()


def uniqueIds(users):
    clear()
    
    idlist = []

    for line in users:
        userid = line.get(id)
        idlist.append(userid)
    
    for ids in idlist:
        if idlist.count(ids) == 1:
            
            for line in users:
                if line.get(id) == ids:
                    print(f"Уникальный идентификатор | Строка - {users.index(line)+1}, Имя - {line.get('name')} {line.get('last_name')}")
    
    choose()


def uniqueNames(users):
    clear()
    
    namelist = []

    for line in users:
        username = line.get('name')
        namelist.append(username)
    
    for name in namelist:
        if namelist.count(name) == 1:
            
            for line in users:
                if line.get('name') == name:
                    print(f"Уникальное имя | Строка - {users.index(line)+1}, Имя - {line.get('name')} {line.get('last_name')}")
    
    choose()


# Последние два задания в одном
def isActive(users):
    clear()
    
    inactiveCount = 0
    for line in users:
        if line.get('isActive'):
            print(f"Пользователь {line.get('name')} {line.get('last_name')} - Активен")
        else:
            inactiveCount += 1
    
    if inactiveCount == 0:
        print('\nВсе пользователи активны')
    else:
        print(f"\nНеактивных пользователей - {inactiveCount}")
        
    choose()



if __name__ == "__main__":
    clear()
    choose()