def uniqueFileNames(s: set):
    result = set(item for item in s if ".jpg" in item)
    
    return result

s = ("book_cover.jpg cover.png Book_cover.jpg "
    "illustration.jpg ILLUSTRATION.JPG my_cover.png "
    "photo.gif award.jpg Award.jpg award.JPG".lower().strip().split(" "))

print(uniqueFileNames(set(s)))


def getColors(amount):
    namedColors = set(input(f"Введите {i + 1} цвет: ").lower() for i in range(amount))
    return "Принято" if len(namedColors) == amount else "Повтор"
    

print(getColors(int(input("Введите кол-во цветов: "))))