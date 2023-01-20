
"""
   # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""
import re

# Список
list_of_words = ["а", "б", "в"]

# Строка
string_to_process = "Сервис  б по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."

# lambda-функция, фильтрующая
# string_to_process = re.sub("[а|б|в]", "+", string_to_process)
# split_str = string_to_process.split('+')
filtered_str = ''.join((filter(lambda s: s not in list_of_words, string_to_process)))

print("Отфильтрованная строка:", filtered_str)