import csv
import sqlite3
import os

path = "C:\\Users\\Варя\\Desktop\\csv"
path_file = (os.listdir(path))
count_file = len(path_file)
for i in range(count_file):
    path_2 = (path + "\\" + path_file[i])
    print(path_2 + " добавлено в общую базу")
    con = sqlite3.connect('D:\\bdlast\\database1.sql')
    cur = con.cursor()
    with open('C:\\Users\\Варя\Desktop\\data.csv', 'r', encoding="Windows-1251") as f:
        dr = csv.DictReader(f, delimiter=";")
        to_db = [(i['Номер_в_госреестре'], i['Наименование_СИ'], i['Единица_измерения_СИ'], i['Модификация_СИ'],
                  i['Тип_СИ'], i['Погрешность_СИ'], i['Дата_утверждения_типа_СИ'], i['Производитель_СИ'],
                  i['Дата_поверки_СИ'], i['Наименование_файла_с_описанием']) for i in dr]
    cur.executemany("INSERT INTO dblast11  (Номер_в_госреестре, Наименование_СИ, Единица_измерения_СИ, Модификация_СИ,"
                    "Тип_СИ, Погрешность_СИ, Дата_утверждения_типа_СИ, Производитель_СИ, "
                    "Дата_поверки_СИ, Наименование_файла_с_описанием) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    con.commit()
    con.close()
print("Загрузка завершена")