import os, random

# систему подсказок горячо, тепло, холодно я считаю что реализовал плохо
# я уверен что её можно написать гораздо понятнее 
# не хотелось искать готовое решение, а сделать самому
# вышло не читаемо, наверняка если я открою этот код через месяц другой то буду сидеть и не понимать что я тут написал
# хоть код и работает, но я считаю что вышло так себе :(
# я пометил все то про что я тут написал




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  


def main():
    clear()
    print("Игра - удагай число.\nЗадача - угадать моё число. \nКоличество попыток ограничено.\n")
    lvlOne(totaltries=0)


def hint(randnum, num):
    if randnum > num:
        print('Дополнительная подсказка: Мое число больше вашего\n')
    else:
        print('Дополнительная подсказка: Мое число меньше вашего\n')


def lvlOne(totaltries):
    tries = 3
    randnum = random.randint(1, 5)
    print('Первый уровень: Число от 1 до 5')
    while tries != 0:
        print(f'Оставшееся кол-во попыток: {tries}\n')
        num = int(input('Введите число: '))
        if num < 1 or num > 5:
            clear()
            print('Неккоректный выбор\n')
        elif num != randnum:
            if randnum - num == 1 or randnum - num == -1: 
                clear()
                print('Тепло\n')
                tries -= 1
                totaltries += 1
            else:
                clear()
                print('Холодно\n')
                tries -= 1
                totaltries += 1
        elif num == randnum:
            totaltries += 1
            clear()
            break

    
    if tries == 0:
        clear()
        print('Вы проиграли.\n')
        lvlOne(totaltries)
    else:
        print('Верно!\n')
        lvlTwo(totaltries)


def lvlTwo(totaltries):
    tries = 6
    randnum = random.randint(1, 15)
    print('Второй уровень: Число от 1 до 15')
    while tries != 0:
        print(f'Оставшееся кол-во попыток: {tries}\n')
        num = int(input('Введите число: '))
        if num < 1 or num > 15:
            clear()
            print('Неккоректный выбор\n')
        elif num != randnum:

            if randnum - num == 1 or randnum - num == -1:
                clear()
                print('Горячо\n')
                tries -= 1
                totaltries += 1

            elif randnum > num and randnum - num <= 4: # :(
                clear()
                print('Тепло\n')
                tries -= 1
                totaltries += 1

            elif randnum < num and randnum - num >= -4: # :(
                clear()
                print('Тепло\n')
                tries -= 1
                totaltries += 1

            else:
                clear()
                print('Холодно\n')
                tries -= 1
                totaltries += 1

        elif num == randnum:
            totaltries += 1
            clear()
            break

    
    if tries == 0:
        clear()
        print('Вы проиграли.\n')
        lvlOne(totaltries)
    else:
        print('Верно!\n')
        lvlThree(totaltries)


def lvlThree(totaltries):
    tries = 8
    randnum = random.randint(1, 30)
    print('Третий уровень: Число от 1 до 30')
    while tries != 0:
        print(f'Оставшееся кол-во попыток: {tries}\n')
        num = int(input('Введите число: '))
        if num < 1 or num > 30:
            clear()
            print('Неккоректный выбор\n')
        elif num != randnum:

            if randnum > num and randnum - num <= 2: # :(
                clear()
                print('Горячо\n')
                tries -= 1
                totaltries += 1
                if tries <= 2:
                    hint(randnum, num)

            elif randnum < num and randnum - num >= -2: # :(
                clear()
                print('Горячо\n')
                tries -= 1
                totaltries += 1
                if tries <= 2:
                    hint(randnum, num)

            elif randnum > num and randnum - num <= 6: # :(
                clear()
                print('Тепло\n')
                tries -= 1
                totaltries += 1
                if tries <= 4:
                    hint(randnum, num)

            elif randnum < num and randnum - num >= -6: # :(
                clear()
                print('Тепло\n')
                tries -= 1
                totaltries += 1
                if tries <= 4:
                    hint(randnum, num)

            else:
                clear()
                print('Холодно\n')
                tries -= 1
                totaltries += 1
        elif num == randnum:
            totaltries += 1
            clear()
            break

    
    if tries == 0:
        clear()
        print('Вы проиграли.\n')
        lvlOne(totaltries)
    else:
        print(f'Поздравляю!\nДля прохождения игры вам потребовалось {totaltries} попыток')
    

if __name__ == "__main__":
    main()