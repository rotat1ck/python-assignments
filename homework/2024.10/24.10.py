def table():
    n = int(input("Введите размер таблицы: "))
    result = []
    
    for i in range(1, n+1):
        result.append([i*j for j in range(1, n+1)])
        
    return result

def squares():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = []
    
    for i in range(a, b+1):
        result.append(i**2)
        
    return result


print(table())
print(squares())