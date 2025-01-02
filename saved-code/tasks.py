import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  


def choose():
    tasknum = int(input('Выберите номер задачи от 1 до 5: '))
    if tasknum == 1: one()
    elif tasknum == 2: two()
    elif tasknum == 3: three()
    elif tasknum == 4: four()
    elif tasknum == 5: five()
    else:
        print('Такой задачи нет)')
        choose()


def one():
    clear()
    
    string = 'hello pythonist, hello notpythonist'
    
    string = string.split()
    print({word: string.count(word) for word in string})
    
    choose()


def two():
    clear()
    
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    
    result = {}
    for i in range(len(l1)):
        result[l1[i]] = l2[i]

    print(result)
    
    choose()


def three():
    clear()
    
    worddict = {'value': 'key', 'abc': 123}
    result = {}
    
    for key, value in worddict.items():
        result[value] = key

    print(result)

    choose()


def four():
    clear()
    
    dict1 = {'a': 2, 'b': 3, 'c': 9}
    dict2 = {'b': 4, 'c': 5}
    
    result = dict1.copy()
    result.update(dict2)
    
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if (key1 == key2):
                result[key1] = value1 + value2
                
    print(result)
    
    choose()


def five():
    clear()
    
    keylist = ['abc', 123, 'text', 'pythonist', 'nottext', 1234]
    
    result = {}
    for i in range (0, len(keylist), 2):
        result[keylist[i]] = keylist[i+1]


    print(result)
    
    choose()

if __name__ == "__main__":
    clear()
    choose()