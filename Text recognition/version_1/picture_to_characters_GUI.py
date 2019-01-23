from picture_to_characters import p2c

import tkinter

import tkinter.filedialog



def run():

    file_name = en.get()
    a = p2c()
    a.full_name = file_name
    a.open_file()
    a.to_code()
    a.creat_save()
    




window = tkinter.Tk()

window.title("图片转文字1.0版本")

window.geometry('500x500')

l = tkinter.Label(window, bg="#ADD8E6", text="请将图片放入D:/picture_to_characters_datebase 目录下", width=110, height=3,
                  font=('宋体', 12))
l.pack()

l2 = tkinter.Label(window, text="请输入包含扩展名的文件名", width=60, height=2,
                  font=('宋体', 12))
l2.place(x=27,y=80)

en = tkinter.Entry(window,width=30,font=('宋体', 20))

en.place(x=37,y=130)

b = tkinter.Button(window,  width = 5,text = "提交",command = run).place(x=225,y=180)






window.mainloop()
