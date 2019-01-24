### 公交查询GUI 的第一版，初步实现了功能  导入了buss_search 1 这个包中的相应程序
from bus_search_3_GUI import bus_search
import tkinter
import winsound





def clear():

    pass

def go(a):

    global direct_number

    check = bus_search()
    check.ask(a)
    check.get()
    number = check.get_information()
    direct_number = direct_bus(number)
    creat_radionbutton(direct_number)




def get_time():

    global a,direct_number
    suoyin = a
    int_suoyin = int(suoyin)
    time = direct_number[int_suoyin][1]
    if time[-1]=="'":
        time = time[0:-1]
    print(time)






def set_clock():

    get_time()
    file = "bird.wav"
    winsound.PlaySound(file, winsound.SND_FILENAME|winsound.SND_NOWAIT)


def direct_bus(number):

    for i in number:
        if not(i[0] == "70" or i[0] == "71" or i[0] == "72"):
            number.remove(i)
    return  number




def creat_radionbutton(direct_number):

    global frm,a  #采用global 的方式解决 回调函数不能有返回值的问题

    var = tkinter.StringVar()

    def chose_bus():

        global a  #这样就变相把a的 return了

        a = var.get()

        print(a)

    for i in range(len(direct_number)):

        bus_str = direct_number[i][0]+" "*(20-len(direct_number[i][1]))+direct_number[i][1]

        i = str(i)

        tkinter.Radiobutton(frm, text=bus_str,variable=var,value=i,justify="center",indicatoron=0,
                            font=('Arial',16),width=20,command=chose_bus).place(x=25,y=(46*int(i)+20))










if __name__ == '__main__':


    a="1"

    direct_number=[]

    window = tkinter.Tk()

    window.title("BUE_SEARCH")

    window.geometry("500x700")

    frm = tkinter.Frame(width=300,height=450,bg="#FDF5E6")

    frm.place(x=60,y=200)

    l =tkinter.Label(width=25, height=1, text='chose your destination', font=('Arial',20),bg='#F0FFFF')
    l.place(x=60, y=30)

    b1 = tkinter.Button(window, text="home", width=15, height=2, command=lambda:go("home"))  #使用lambda 向回调函数中传入参数
    b1.place(x=60, y=130)

    b3 = tkinter.Button(window, text="clear", width=12, height=2, command=clear)
    b3.place(x=380, y=400)

    b4 = tkinter.Button(window, text="choose", width=12, height=2, command=set_clock)
    b4.place(x=380, y=300)

    b2 = tkinter.Button(window, text="work", width=15, height=2, command=lambda:go("work"))
    b2.place(x=245, y=130)




    window.mainloop()