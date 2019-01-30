### 公交查询GUI 的第3版，实现的功能为查找班车，并能选定要做的班车，然后提前八分钟闹钟提示
###涉及到了，多线程解决卡死问题，arrow 时间模块，winsound采用的是闹钟模块，apscheduler的延时设置问题，
from bus_search_v4_coding import bus_search
import tkinter,arrow
import winsound
from apscheduler.schedulers.blocking import BlockingScheduler
import threading



def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()






def clear():
    #点击清楚按钮直接将所有fram的元素清除

    for widget in frm.winfo_children():
        widget.destroy()

def go(a):
    #运行爬虫函数，并显示所有可能

    global direct_number
    clear()
    check = bus_search()
    check.ask(a)
    number = check.get()
    direct_number = direct_bus(number)
    creat_radionbutton(direct_number)


def cal_time(a):
    #将数值格式的时间转化为定时任务所需的字符型时间格式
    arw = arrow.now()
    if len(a) <= 3:
        a = int(a)
        if a <= 8:
            pass
        else:
            t = arw.shift(minutes=(a - 10))
            time_str = t.format('YYYY-MM-DD HH:mm:ss')
            print((time_str,"cal_time"))
            return time_str
    else:
        hour = int(a[:2])
        min = int(a[-2:])
        t = arw.replace(hour=hour, minute=min).shift(minutes=-10)
        time_str = t.format('YYYY-MM-DD HH:mm:ss')
        print((time_str, "cal_time"))
        return time_str



def get_time():
    #在爬虫返回值中得到到站具体时间
    global a,direct_number
    suoyin = a
    int_suoyin = int(suoyin)
    time = direct_number[int_suoyin][1]
    if time[-1]=="'":
        time = time[0:-1]
    time_str = cal_time(time)

    return time_str






def set_clock():

    l.destroy()

    l1 = tkinter.Label(width=25, height=1, text='The alarm clock has been set', font=('Arial', 20), bg='#F0FFFF')
    l1.place(x=60, y=30)

    def clock():

        winsound.Beep(400, 1100)

    sched = BlockingScheduler()

    time_str = get_time()

    sched.add_job(clock, 'date', run_date=time_str)

    sched.start()




def direct_bus(number):

    direct_bus_number = []

    for i in number:
        if i[0] == "70" or i[0] == "71" or i[0] == "72":
            direct_bus_number.append(i)
    return  direct_bus_number




def creat_radionbutton(direct_number):

    global frm,a  #采用global 的方式解决 回调函数不能有返回值的问题

    var = tkinter.StringVar()

    def chose_bus():

        global a  #这样就变相把a的 return了

        a = var.get()


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

    b1 = tkinter.Button(window, text="home", width=15, height=2, command=lambda:thread_it(go,"home"))  #使用lambda 向回调函数中传入参数
    b1.place(x=60, y=130)

    b3 = tkinter.Button(window, text="clear", width=12, height=2, command=clear)
    b3.place(x=380, y=400)

    b4 = tkinter.Button(window, text="choose", width=12, height=2, command=lambda:thread_it(set_clock))
    b4.place(x=380, y=300)

    b2 = tkinter.Button(window, text="work", width=15, height=2, command=lambda:thread_it(go,"work"))
    b2.place(x=245, y=130)




    window.mainloop()