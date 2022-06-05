import sqlite3

user = ("1", "2", "3", "4")
con = sqlite3.connect('D:\\testdb2.db')
cur = con.cursor()
cur.execute("""INSERT INTO final_version (Номер_в_госреестре, Наименование_СИ, Производитель_СИ, Наименование_файла_с_описанием) 
   VALUES(?, ?, ?, ?);""", user)

con.commit()
con.close()
print("Загрузка завершена")

print(whatiscountry(saving_folder + f"//1.txt"))
print(foundnumber(saving_folder + f"//1.txt"))
print(foundname(saving_folder + f"//1.txt"))