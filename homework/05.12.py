import re

def one(string):
    result = re.findall(r'\bкот\b', string)
    return result

def two(string):
    result = re.findall(r'\S*кот\S*', string)
    return result

def three(string):
    result = re.findall(r'\d+', string)
    return result

def four(string):
    result = re.findall(r'\b\w*\d\w*\b', string)
    return result


print(one("кот котопес кот котик котэ кот"))

print(two("кот котопес кот котик котэ кот"))

print(three("2023 hello world 2024 top academy"))

print(four("lorem 2023year hello1 world hello2 top2024 academy"))