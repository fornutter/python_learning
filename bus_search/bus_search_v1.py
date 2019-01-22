###查询回家或者去学校的站点的车辆时间表，并实现了chrome 的无头查询
## 以列表形式输出，其内为元祖，元祖的第一个元素为多少路车，元祖第二个为还有多长时间到
## 程序可以选择回家还是去学校


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree
from selenium.webdriver.chrome.options import Options


class bus_search():

    def __init__(self):

        self.chrome_options = Options()

        self.chrome_options.add_argument('--headless')  ## 实现了chrome 的无头化操作

        self.url = ''

        self.driver_path = r"D:\chromedriver_win32\chromedriver.exe"

        self.url_home = "https://www.delijn.be/en/haltes/halte/201659/Zwijnaarde_Technologiepark"

        self.url_work = "https://www.delijn.be/en/haltes/halte/200223/Gent_Veemarkt"

        self.driver = webdriver.Chrome(executable_path=self.driver_path, options= self.chrome_options)

    def run(self):

        self.ask()

        self.driver.get(self.url)

        self.get_information()

        self.driver.close()


    def ask(self):

        a = input("please in put your destination(home or work):")

        if a == "home":

            self.url = self.url_home
        elif a == "work":

            self.url = self.url_work

    def get_information(self):

        result = []

        WebDriverWait(self.driver,1000,0.5).until(

            EC.presence_of_element_located((By.ID,"passagesContentList"))
        )

        source = self.driver.page_source

        html = etree.HTML(source)

        line = html.xpath("//ul[@id='passagesContentList']/li//span[@class='line-number']/text()")

        time = html.xpath("//ul[@id='passagesContentList']/li/span[@class='list-time list-time-hour']/text()")

        line = line[1::2]

        for i in range(len(line)):

            line[i] = line[i].strip()


        for j in range(len(line)):

            result.append((line[j],time[j]))


        print(result)


if __name__ == '__main__':

    a = bus_search()

    a.run()