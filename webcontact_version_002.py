import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from pdf2image import convert_from_path
import os
import sqlite3
from imortorexport import whatiscountry
from imortorexport import foundnumber
from imortorexport import foundname

#Код для прогона всех пдф файлов и перевода их пострачнично в текстовые документ с помошью нейроночки

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # путь к тессеракту
poppler_path = r"C:\Program Files\poppler-0.68.0\bin" # путь к попплеру

path = r"temp"
path_file = (os.listdir(path))
count_file = len(path_file)

for i in range(count_file):
    filePdfname = os.path.splitext(path_file[i])[0]
    pdf_path = os.path.splitext(path + "/" + path_file[i])[0] + ".pdf"
    pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
    saving_dir = r"temp"
    saving_folder = saving_dir + f"/texted_" + filePdfname
    os.mkdir(saving_folder)
    c = 1
    for page in pages:
        img_name = f'img-{c}.jpeg'
        page.save(os.path.join(saving_folder, img_name), "JPEG")
        im = Image.open(saving_folder + f"/{img_name}") # the second one
        im = im.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(2)
        im = im.convert('1')
        blured_file = saving_folder + f"/hsv_{img_name}"
        im.save(blured_file)
        text = (pytesseract.image_to_string(Image.open(blured_file), lang='rus+eng'))
        traectoriya = saving_folder + f"//{c}.txt"
        f = open(traectoriya, 'w+', encoding='utf-8')
        f.write(f"Старница {c}\n" + text)
        textnames = f.read()
        if c == 1:
            print(foundnumber(saving_folder + f"//1.txt"))
            print(foundname(saving_folder + f"//1.txt"))
        f.close()
        c = c + 1
    print(whatiscountry(saving_folder + f"//{c-1}.txt"))
    user = (foundnumber(saving_folder + f"//1.txt"), foundname(saving_folder + f"//1.txt"),
            whatiscountry(saving_folder + f"//{c-1}.txt"), path_file[i][0] + ".pdf")
    con = sqlite3.connect('C:\\Users\\admin\\PycharmProjects\\pythonProject2\\webprilozhenie\\database.db')
    cur = con.cursor()
    cur.execute("""INSERT INTO final_table1 (Номер_в_госреестре, Наименование_СИ, Производитель_СИ, Наименование_файла_с_описанием)
               VALUES(?, ?, ?, ?);""", user)

    con.commit()
    con.close()
    print("Загрузка завершена")
    # os.rmdir(saving_folder)
