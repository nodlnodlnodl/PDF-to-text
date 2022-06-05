import sqlite3


con = sqlite3.connect('D:\\test.sql')
cur = con.cursor()
cur.execute("""CREATE TABLE test1 (
            Номер_в_госреестре TEXT,
            Наименование_СИ TEXT,
            Единица_измерения_СИ TEXT,
            Модификация_СИ TEXT,
            Тип_СИ TEXT,
            Погрешность_СИ TEXT,
            Дата_утверждения_типа_СИ TEXT,
            Производитель_СИ TEXT,
            Дата_поверки_СИ TEXT,
            Наименование_файла_с_описанием TEXT)""")

con.commit()
con.close()
