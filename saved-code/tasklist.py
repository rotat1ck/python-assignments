import os


def create_array():
    array = []
    oneprint = 0 #переменная нужна что-бы просьба ввести число выводилась только один раз (костыль) 
    
    while oneprint == 0:
        num = input('Введите число для добавления в массив (y - завершить ввод): \n')

        if num != 'y':
            num = int(num)
            array.append(num)

            while oneprint == 0:
                num = input()
                if num != 'y':
                    num = int(num)
                    array.append(num)   
                else:
                    oneprint = 1
                    break

        else:
            break

    
    return array


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # очистка консоли (не работает внутри pycharm)


def choose():
    
    tasknum = int(input('Выберите номер задачи от 1 до 6: '))
    if tasknum == 1: one()
    elif tasknum == 2: two()
    elif tasknum == 3: three()
    elif tasknum == 4: four()
    elif tasknum == 5: five()
    elif tasknum == 6: six()
    else:
        print('Такой задачи нет)')
        choose()


# 1
def one():
    clear()
    
    array = []
    oneprint = 0
    
    while oneprint == 0:
        word = input('Введите число для добавления в массив (y - завершить ввод): \n')

        if word != 'y':
            array.append(word)

            while oneprint == 0:
                word = input()
                if word != 'y':
                    array.append(word)   
                else:
                    oneprint = 1
                    break

        else:
            break
    
    result = ''
    for word in array:
        result += word + " "
    result.strip()
    
    print(f'\nРезультат: {result}')

    choose()


# 2
def two():
    clear()

    array = create_array()
    result = 0
    
    for num in array:
        if num > 0:
            result += num
    
    print(f'\nРезультат: {result}')
    
    choose()


# 3
def three():
    clear()

    array = create_array()
    result = []
    
    if len(array) == 0:
        print(f'\nРезультат: {result}')
        choose()
        
    result = [0, 0]
    
    for num in array:
        if num > 0:
            result[0] += 1
        else:
            result[1] += num
            

    print(f'\nРезультат: {result}')
            
    choose()


# 4
def four():
    clear()

    nums = int(input('Введите любое положительное число: '))
    
    if nums <= 0:
        print('Число не положительное')
        choose()
        
    numlist = []
    nums = str(nums)
    
    for num in nums:
        numlist.append(num)
        
    numlist = sorted(numlist, reverse=True)
    result = ''
    
    for num in numlist:
        result += num

    print(f'\nРезультат: {int(result)}')
    
    choose()


# 5 
def five():
    clear()
    
    array = create_array()
    c1 =0
    c2 =0
    
    if len(array) < 3:
        print('Список должен быть больше 3')
    
    for num in array:
        if num % 2 == 0:
            c1 += 1
        else:
            c2 += 1
            
    if c1 > 1 and c2 > 1:
        print('Некорректный ввод')
        
    for num in array:
        if c1 == 1 and num % 2 ==0:
            print(f'\nРезультат: {num}')
            break
        elif c2 == 1 and num % 2 !=0:
            print(f'\nРезультат: {num}')
            break

    choose()


# 6
def six():
    clear()
    
    array = create_array()
    result = 0
    
    if len(array) < 4:
        print('Список должен быть больше 4')
        
    array = sorted(array)
    result = array[0] + array[1]
    
    print(f'\nРезультат: {result}')
    
    choose()


if __name__ == "__main__":
    choose()