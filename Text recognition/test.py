import tkinter

import tkinter.filedialog


def run():

    filename = tkinter.filedialog.askopenfilename()

    print(filename)

window = tkinter.Tk()

window.title("图片转文字1.0版本")

window.geometry('500x500')

b = tkinter.Button(window,  width = 5,text = "提交",command = run).pack()


window.mainloop()