"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""
from email.header import UTF8

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

num_of_students = 0
total_math = 0
total_python = 0
total_english = 0

best_student = (None, 0)

with open(INPUT_FILE, "r", encoding="UTF8") as f:
    next(f)
    for line in f:
        num_of_students += 1

        line = line.strip("\n").split(",")

        name = line[0]

        math = int(line[1])
        total_math += math

        python = int(line[2])
        total_python += python

        english = int(line[3])
        total_english += english

        av = round((math + python + english)/3,1)

        if av > best_student[1]:
            best_student = (name,av)

    try:
        av_math = round(total_math/num_of_students,1)
        av_python = round(total_python/num_of_students,1)
        av_english = round(total_english/num_of_students,1)
    except ZeroDivisionError:
        print("У списку 0 студентів :(")

with open(OUTPUT_FILE, "w", encoding="UTF8") as f:
    f.write(f"Середній бал по класу:\n math: {av_math}\n python: {av_python}\n english: {av_english}\n")
    f.write(f"Найкращий студент: {best_student[0]} ({best_student[1]})")

print(f"Середній бал по класу:\n math: {av_math}\n python: {av_python}\n english: {av_english}\n")
print(f"Найкращий студент: {best_student[0]} ({best_student[1]})")


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
