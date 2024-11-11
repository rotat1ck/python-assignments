#1
sentence = 'Мама мыла рамhу 123'

print(list(map(lambda x: len(x), sentence.split())))

#2
sentence = 'Мама мыла раму'
sentence = sentence.lower()

print(dict(set(map(lambda x: (x, sentence.count(x)), sentence))))

#3
numbers = [1,2,3,4,5]
dict = {}

for i in numbers:
    dict[i] = [j for j in range(1, i + 1) if i % j == 0]

print(dict)

#4
string = 'Российская Федерация'
string = string.upper()
string = string.split()

print(''.join(list(map(lambda x: x[0], string))))

#5
rle = [('a', 2), ('b', 3), ('c', 1)]

print(''.join(list(map(lambda x : x[0]*x[1], rle))))



