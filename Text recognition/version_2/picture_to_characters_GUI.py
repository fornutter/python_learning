
from picture_to_characters import p2c

import tkinter

import tkinter.filedialog

import tkinter.messagebox



def show_path():

    filename = tkinter.filedialog.askopenfilename()
    value_e.set(filename)


def run():

    file = p2c()
    file.path = en.get()
    file.to_code()
    file.creat_save()
    tkinter.messagebox.showinfo(title="消息提醒",message="识别已经完成，存放在当前目录下\" "+file.name+"\" 文件夹中")





window = tkinter.Tk()

window.title("图片转文字1.0版本")

window.geometry('500x500')

l = tkinter.Label(window, bg="#ADD8E6", text="请选择要识别的图片文件", width=110, height=3,
                  font=('宋体', 12))
l.pack()

value_e =tkinter.StringVar()

en = tkinter.Entry(window,width=35,font=('宋体', 16),textvariable = value_e)

en.place(x=23,y=130)



b = tkinter.Button(window, height=1, width = 6,text = "浏览",command =show_path, font=('宋体', 12))

b.place(x=418,y=128)

b2 = tkinter.Button(window, height=2, width = 8,text = "开始识别",command = run ).place(x=225,y=180)



window.mainloop()
