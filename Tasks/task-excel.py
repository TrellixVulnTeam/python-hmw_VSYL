import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['фамилия', 'имя', 'оценка'])

with open('students.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.split(' ')
        ws.append([parts[0], parts[1], parts[-1]])

wb.save("students.csv")
wb.close()