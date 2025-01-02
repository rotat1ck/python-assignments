# employees = [
#     {"name": "Иван Иванов", "salary": 50000},
#     {"name": "Мария Петрова", "salary": 60000},
#     {"name": "Алексей Сидоров", "salary": 45000},
#     {"name": "Наталья Смирнова", "salary": 70000},
#     {"name": "Дмитрий Кузнецов", "salary": 55000},
#     {"name": "Ольга Попова", "salary": 65000},
#     {"name": "Владимир Ефимов", "salary": 52000}
# ]

# print(list(map(lambda x: f"{x['name']} {x['salary']}", employees)))

from functools import reduce 

#map

#1
numbers = [2, 4, 6, 8, 10]

print(list(map(lambda x: x**2, numbers)))

#2
strings = ["apple", "banana", "kiwi", "mango"]

print(list(map(lambda x: len(x), strings)))

#3
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 150}
]

print(list(map(lambda x: x['name'], products)))

#4
numbers = [5, 15, 25, 35, 45]

print(list(map(lambda x: x+10, numbers)))

#5
students = [
    {"name": "Alex", "grade": 5},
    {"name": "John", "grade": 4},
    {"name": "Emma", "grade": 3},
    {"name": "Sophia", "grade": 5}
]

print(list(map(lambda x: f"Имя: {x['name']}, Оценка: {x['grade']}", students)))

#reduce

#1
numbers = [2, 3, 4, 5]

print('\n')
print(reduce(lambda a, b: a + b, numbers))

#2
transactions = [
    {"amount": 100, "type": "приход"},
    {"amount": 200, "type": "расход"},
    {"amount": 150, "type": "приход"},
    {"amount": 300, "type": "расход"},
    {"amount": 250, "type": "приход"}
]

l1 = list(filter(lambda x: x['type'] == 'приход', transactions))

l2 = list(map(lambda x: x['amount'] , l1))

print(reduce(lambda a, b: a + b, l2))

#3
employees = [
    {"name": "John", "salary": 5000},
    {"name": "Emma", "salary": 4500},
    {"name": "Sophia", "salary": 6000},
    {"name": "Michael", "salary": 5500}
]

l1 = list(map(lambda x: x['salary'] , employees))

print(reduce(lambda a, b: a + b, l1))
