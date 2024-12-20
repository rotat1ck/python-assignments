import re

def one(input: str) -> str:
    if re.findall(r"\w+", input):
        return 'Спасибо'
    else:
        return 'Вы ничего не ввели'
    
    
userInput = input()
print(one(userInput))


def two(input: str) -> None:
    input = re.split("%", input)
    for item in input:
        print(f"{input.index(item)}. {item}")
        
        
userInput = input()
two(userInput)


def three(input: str) -> str:
    return re.sub('%', ' ', input)

userInput = input()
print(three(userInput))


def four(input: str) -> str:
    if re.findall(r"\d+", input):
        return 'Есть цифра'
    else:
        return 'Нет цифры'
    
userInput = input()
print(four(userInput))


def five(input: str) -> str:
    if re.findall(r"^\w+$", input):
        return 'Пароль корректный'
    else:
        return 'Некорректный'
    
userInput = input()
print(five(userInput))


def six(input: str) -> str:
    if re.findall(r"^[a-zA-Zа-яА-ЯёЁ\s]+$", input):
        return 'Принято'
    else:
        return 'Некорректный ввод'
    
userInput = input()
print(six(userInput))


