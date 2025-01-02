def findInterest(s1, s2):
    return f"Общих чисел: {' '.join(sorted(s1.intersection(s2)))}"


# print(findInterest(
#     set("4 12 6 11 0 8 7 5 1 25".strip().split(" ")),
#     set("2 1 4 5 56 6 8 7 14 33".strip().split(" "))
# ))

def findSimilarity(s1, s2):
    return "Yes" if s1 & s2 else "No"

print(findSimilarity(
    set("5 5 5 4 8 1".strip().split(" ")),
    set("6 3 2 0 0 1".strip().split(" "))
))