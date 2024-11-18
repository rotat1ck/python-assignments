import os

nums = set()
c = 0
os.system("cls")
while len(nums) < 10:
    data = input(f"Введите {10 - len(nums)} чисел: ")
    new_nums = ([int(i) for i in data.strip().split(' ')])
    if len(new_nums) + len(nums) <= 10:
        nums.update(set(new_nums))
    else:
        for num in new_nums:
            if len(nums) < 10:
                nums.add(num)
            else:
                print(nums)
                break



def isAnagram(s1, s2):
    return set(s1) == set(s2)

print(isAnagram('кластер', 'стрелка'))

def findSimilaryty(s1, s2):
    similarity = set(s1).intersection(set(s2))
    return len(similarity)

s1 = input("Введите 1 набор книг: ").strip().split(', ')
s2 = input("Введите 2 набор книг: ").strip().split(', ')

print(findSimilaryty(set(s1), set(s2)))

