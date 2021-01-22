import openpyxl as opx
import re

digital_find = r'\s[А-Я][а-я]*'
email_find = r'\w+\@\w+.\w+'
f = open('import.csv', 'w')
work_document = opx.load_workbook('1.xlsx') #подгружаем файл
work_sheet = work_document.worksheets[0] #выбираем 1 лист для работы
for row in work_sheet.rows:
    firma = row[0].value
    stroka = row[2].value
    fio = re.findall(digital_find, stroka)[:3]# 1:Фамилия 2: Имя 3: Отчество Список
    contact_email = re.findall(email_find, stroka)
    if contact_email:
#   f.write(firma + ',' + fio[0] + ',,' +fio[1] + fio[2] + ',,,,,,,,,,,' + contact_email[0] + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,firma,' +'\n')
        f.write(firma + ',,,,,,,,,,,,,,' + contact_email[0] + ',,,,,,,,,,,,,,,,,,,,,,,,,,,,,' + '\n')
f.close()




