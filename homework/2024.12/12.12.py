import re

s1 = """
    Betty bought a bit of butter, But the butter was so bitter,
    So she bought some better butter, To make the bitter butter better.
"""

temp = re.findall(r"\b[bB]\w+", s1)
print(temp)


s2 = "A, very very; irregular_sentence"

temp = re.sub(r"[,;_]", ' ', s2)
print(re.sub(r'\s+', ' ', temp))


s3 = ["admin@mail.ru", "top@yandex.ru", "email@top-academy.ru"]

print([re.findall(r"@\S+", email) for email in s3])