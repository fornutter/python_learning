import pytesseract

from PIL import Image

import re, os, shutil

class p2c():

    def __init__(self):

        self.path = "D:/picture_to_characters_datebase/"

        self.name=""

        self.full_name = ""

        self.code = ""


    def to_code(self):


        image = Image.open(self.path)

        self.code = pytesseract.image_to_string(image)


    def open_file(self):

        self.path = self.path + self.full_name


    def creat_save(self):

        self.name = re.split(r"\.",self.full_name)[0]

        path = re.split(r"\.",self.path)[0]

        os.mkdir(path)

        list = self.code.split(' \n')

        while "\n" in list:
            list.remove("\n")

        with open(path+"/"+self.name+".txt", "w",encoding="utf-8") as f:
            for i in list:
                f.write(i)

        shutil.move(self.path, path+"/"+self.full_name)

if __name__ == '__main__':

    exmaple = p2c()
    exmaple.open_file()
    exmaple.to_code()
    exmaple.creat_save()









