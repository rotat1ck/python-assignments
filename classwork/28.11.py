import re

# text = 'Hello world!'

# print(re.match('hello', text))
# print(re.match('hi', text))

# text2 = 'hello world hello qwerty hello ipsum'
# print(re.search("hello", text2))

# print(re.findall("hello", text2))

data = 'В компании работают 5 бекендеров, 10 фрондендеров и 3 дизайнера'

print(re.findall(r"\w", data))
print(re.findall(r"\d\d", data))

fruits = 'apple pineapple apricot avocado banana'

print(re.findall(r"a\w+", fruits))
print(re.findall(r"\ba\w+\b", fruits))