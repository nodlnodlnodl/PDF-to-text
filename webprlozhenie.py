import eel
import shutil
eel.init("web")


@eel.expose
def add():
    print("1")

#подача значения в JS и проверка условия
@eel.expose
def add1():
    print("1")
    kekv = 1+1
   # shutil.move("test.pdf", "/temp")
    return kekv



ban = add1()

@eel.expose
def add2():
    print("1")


fileInTemp = eel.download()

print(fileInTemp)



#html файл
eel.start("main.html", mode="chrome", size=(700, 650))

