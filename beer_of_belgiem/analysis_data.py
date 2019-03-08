from urllib import request

class analysis():

    def  __init__(self):
        with open("123.txt",'r',encoding="utf-8") as f:

            self.data = f.read().splitlines()
            self.name = self.data[::3]
            self.degree = self.data[1::3]
            self.src = self.data[2::3]

    def creat_markdown_file(self):

        with open("result.md",'w',encoding="utf-8") as nu:
            for i in range(len(self.name)):
                name ="## "+str(i)+" "+self.name[i]+' '+self.degree[i]
                pic = "![{}]".format(self.name[i])+"({})".format(self.src[i])
                nu.write("\n")
                nu.write(name)
                nu.write("\n")
                nu.write(pic)
        print("success")

    def down_pics(self):

        for i in range(len(self.name)):

            request.urlretrieve(self.src[i], "D:/python_learning/beer_of_belgiem/pic/"+str(i)+".png")


if __name__ == '__main__':

    a = analysis()

    a.creat_markdown_file()

    a.down_pics()