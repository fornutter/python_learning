import random  # 引入random 函数

'''
相较于上一版本，重新编写了计算函数，这次没动一步，仅有一步计算，不会采用递归方式，
引进了矩阵的旋转等操作，减小了代码量。

'''


class Game:  # 定义了game的类

    def __init__(self):  # 定义了初始情况
        self.board_list = [
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""],
            ["", "", "", ""]
        ]
        self.score = 0
        self.board_empty = []
        self.tem = []

    def start(self):  # 主程序
        self.restart()  # 开始时产生两个数字，2或者2
        while True:
            judge = []
            self.print_board()
            code = input("请输入指令")
            if code == "w":
                self.move_up()
            elif code == "s":
                self.move_down()
            elif code == "a":
                self.move_left()
            elif code == "d":
                self.move_right()
            elif code == "r":
                self.restart()
                continue
            elif code == "q":
                exit("退出")
            else:
                print("wrong input")
                continue
            if self.is_win():  # 判断是否出现2048的值
                print("You Win")
                break
            if self.gameover():  # 判断是否是所有个字都已经满了，满了就是完事了
                print("game over")
                break
            self.add_pice()  # 每次循环完都增加一个棋子

    def restart(self):  # 刚开始时候产生随机产生两个位置的棋子

        while True:
            x1 = (random.randrange(0, len(self.board_list)), random.randrange(0, len(self.board_list[0])))
            x2 = (random.randrange(0, len(self.board_list)), random.randrange(0, len(self.board_list[0])))
            if x1 != x2:  # 防止产生的坐标相同
                break
        self.board_list[x1[0]][x1[1]] = random.choice([2, 4])
        self.board_list[x2[0]][x2[1]] = random.choice([2, 4])

    def is_win(self):
        self.board_empty = []
        for i in range(len(self.board_list)):
            for j in self.board_list[i]:
                if j == 2048:
                    return True
                elif j == "":
                    self.board_empty.append((i, self.board_list[i].index(j)))
        return False

    def gameover(self):
        if len(self.board_empty):
            return False
        else:
            return True

    def move_left(self):
        self.tem = []
        for i in range(len(self.board_list)):
            self.tem = []
            for j in range(len(self.board_list)):
                if self.board_list[i][j] != "":
                    self.tem.append(self.board_list[i][j])

            self.board_list[i] = self.calculate(self.tem)

    def move_up(self):
        self.board_list = self.transpose1(self.board_list)  # 向左旋转
        self.move_left()
        self.board_list = self.transpose2(self.board_list)  # 向右旋转

    def move_right(self):
        for i in range(len(self.board_list)):
            self.board_list[i] = self.board_list[i][::-1]
        self.move_left()
        for j in range(len(self.board_list)):
            self.board_list[j] = self.board_list[j][::-1]

    def move_down(self):
        self.board_list = self.transpose2(self.board_list)
        self.move_left()
        self.board_list = self.transpose1(self.board_list)

    def add_pice(self):
        """
        每次增加一个棋子
        """
        if self.board_empty:
            p = self.board_empty.pop(random.randint(0, len(self.board_empty) - 1))
            num = random.choice([2, 4])
            self.board_list[p[0]][p[1]] = num

    def calculate(self, cal):
        flag = True
        narrow = []
        if len(self.tem) > 1:
            for i in range(len(self.tem)):
                if flag:
                    if i + 1 < len(self.tem) and self.tem[i] == self.tem[i + 1]:
                        self.tem[i] = self.tem[i] * 2
                        narrow.append(self.tem[i])
                        flag = False
                    else:
                        narrow.append(self.tem[i])
                        flag = True
        else:
            narrow = self.tem
        for i in range(len(self.board_list) - len(narrow)):
            narrow.append("")
        return narrow

    def transpose1(self, M):  # 矩阵向左旋转函数
        return [list(row) for row in zip(*M)][::-1]

    def transpose2(self, M):  # 矩阵向右旋转函数
        return [list(row) for row in zip(*M[::-1])]

    def print_board(self):
        print("""
Score:{}
+=====+=====+=====+=====+
|{:^5}|{:^5}|{:^5}|{:^5}|
+=====+=====+=====+=====+
|{:^5}|{:^5}|{:^5}|{:^5}|
+=====+=====+=====+=====+
|{:^5}|{:^5}|{:^5}|{:^5}|
+=====+=====+=====+=====+
|{:^5}|{:^5}|{:^5}|{:^5}|
+=====+=====+=====+=====+
w(up),s(down),a(left),d(right)
r(restart),q(exit)""" .format(self.score, *self.board_list[0], *self.board_list[1], *self.board_list[2], *self.board_list[3],))


if __name__ == '__main__':
    a = Game()
    a.start()
