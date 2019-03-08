import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import etree

class get_full_url():

    def __init__(self):

        self.url ='https://www.ratebeer.com/ajax/taggedbeer.asp?t=1129&p='

        self.middle_result = []

        self.picture_src = []

        self.driver_path = r"D:\chromedriver_win32\chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def get(self):

        for i in range(1, 4):

            url = self.url + str(i)

            print(url)

            response = requests.get(url)

            text = response.text

            html = etree.HTML(text)

            tr = html.xpath("//table/tr")

            for td in tr:

                info = td.xpath("./td")[1]

                name = info.xpath("./a/text()")[0]

                degree = info.xpath("./span/text()")[0]

                scr = "https://www.ratebeer.com" + info.xpath("./a/@href")[0]

                bears = {

                    "name":name,
                    "degree":degree,
                    "src":scr

                }
                self.middle_result.append(bears)


    def get_picture(self):

        for i in range(len(self.middle_result)):

            url = self.middle_result[i]["src"]

            self.driver.get(url)

            WebDriverWait(self.driver, 1000, 0.5).until(

                EC.presence_of_element_located((By.ID, "toggleImage"))
            )

            picturs_adress = self.driver.find_element_by_xpath("//div[@id = 'toggleImage']/img").get_attribute("src")

            self.middle_result[i]["src"] = picturs_adress

            print(i)

        print(self.middle_result)

        with open("123.txt","w",encoding='UTF-8') as ne:

            for i in self.middle_result:

                ne.write(i["name"])
                ne.write("\n")
                ne.write(i["degree"])
                ne.write("\n")
                ne.write(i["src"])
                ne.write("\n")

        print("success")


if __name__ == '__main__':

    a = get_full_url()

    a.get()

    a.get_picture()

