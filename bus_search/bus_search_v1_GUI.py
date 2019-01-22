### 公交查询GUI 的第一版，初步实现了功能  导入了buss_search 1 这个包中的相应程序



from bus_search_1_GUI import bus_search

import tkinter


def clear():

    l.delete("1.0", tkinter.END)

def go(a):



    check = bus_search()

    check.ask(a)

    check.get()

    number = check.get_information()

    for i in number:

        if i[0] == "70" or i[0] == "71" or i[0] == "72":

            l.insert("end",i)

            l.insert("end",'\n')

    check.close()



window = tkinter.Tk()

window.title("BUE_SEARCH")

window.geometry("500x700")

l =tkinter.Label(width = 20, height = 1, text='chose your destination', font =('Arial',20),bg='#DAA520')

l.place(x=80,y=30)


b1 = tkinter.Button(window,text="home",width=8,height=2,command =lambda:go("home"))  #使用lambda 向回调函数中传入参数

b1.place(x=30,y=120)

b3 = tkinter.Button(window,text="clear",width=8,height=2,command =clear)

b3.place(x=235,y=120)

b2 = tkinter.Button(window,text="work",width=8,height=2,command =lambda:go("work"))

b2.place(x=420,y=120)

var =tkinter.StringVar()

l = tkinter.Text(window,width=20,height=20,bg="#808080", font =('Arial',15))

l.place(x=150,y=200)




window.mainloop()