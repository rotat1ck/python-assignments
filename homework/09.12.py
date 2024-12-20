import re

emails = "Свяжитесь с нами по адресу support@domain.com или sales@company.org."
print(re.findall(r"\w+@\w+.\w+", emails))

phones = ["+7 (123) 456-78-90", "8-123-456-78-90", "123-456-7890"]
print([re.findall(r'\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}|8-\d{3}-\d{3}-\d{2}-\d{2}', phone) for phone in phones])

dates = "Встречи назначены на 32.05.2023 и 25.12.2024."
print(re.findall(r'\b(?:0[1-9]|[12][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.\d{4}\b', dates))

