def countChar(userInput):
    return f"Количество уникальных символов во всех словах: {len(set(map(lambda x: x, userInput)))}"

n = int(input("Введите кол-во слов: "))
userInput = ''.join(input(f"Введите {i} слово: ") for i in range(1, n + 1))

print(countChar(userInput))