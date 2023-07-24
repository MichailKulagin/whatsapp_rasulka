
import openpyxl
import pywhatkit
import time
import pyautogui

wb = openpyxl.reader.excel.load_workbook(filename="2023_02 СВОДНЫЙ.xlsx")


wb.active = 1

sheet = wb.active

num=1
nomera = []
while True:
    num+=1
    if sheet['G'+str(num)].value == None:
        break

    else:
        #print(num,"  ",sheet['G'+str(num)].value)
        nomera.append(sheet['G'+str(num)].value)

nomera_sort = []
nomera_sort.append(nomera[0])
q = 0
while q<len(nomera):
    q+=1
    try:
        if nomera_sort.count(nomera[q]):
            pass
        else:
            nomera_sort.append(nomera[q])
    except:
        print(q)
print(len(nomera_sort))

with open("namber.txt", "r", encoding="utf-8") as file:
    q = file.readline()

print(q)
try:
    for i in nomera_sort:
        q+=1
        if q<=50:
            print(q)
            mobile = [i]
            print(type(mobile))
            phone = str(mobile) 
            print(type(mobile))
            message = ("Привет")
            pywhatkit.sendwhatmsg_instantly(phone_no=phone, message=message)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1.5)
        else:
            with open("namber.txt", "w", encoding="utf-8") as file:
                file.write(q)

except:
    print("Последний номер", q)
    print("Ошибка человека нет в whatsapp")