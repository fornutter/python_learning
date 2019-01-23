import pytesseract

from PIL import Image

import re, os, shutil

class p2c():

    def __init__(self):

        self.path = ""

        self.full_name = ""

        self.name = ""

        self.code = ""


    def to_code(self):


        image = Image.open(self.path)

        self.code = pytesseract.image_to_string(image)




    def creat_save(self):

        path = re.split(r"\.",self.path)[0]

        self.full_name = os.path.split(self.path)[1]

        self.name = re.split('\.',self.full_name)[0]

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

    exmaple.to_code()
    exmaple.creat_save()









