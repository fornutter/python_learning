from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import  time



class bus_search_powful():

    def __init__(self):

        self.driver_path = r"D:\chromedriver_win32\chromedriver.exe"
        self.path = 'https://www.delijn.be/en/'
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def run(self,a):

        self.driver.get(self.path)

        WebDriverWait(self.driver,1000,0.5).until(
            EC.presence_of_element_located((By.ID,"autocomplete-placeholder-start"))
        )

        start = self.driver.find_element_by_id("search-start")

        start.send_keys(a["from"])

        finish = self.driver.find_element_by_id("search-finish")

        finish.send_keys(a["to"])

        time.sleep(5)

        # WebDriverWait(self.driver,1000,0.5).until(
        #     EC.presence_of_element_located((By.CLASS_NAME,"search-button alpha button"))
        # )

        button = self.driver.find_element_by_xpath('//div[@class= "search-input-button real-input search-input"]/button')

        button.click()

    def get_detail_page(self):

        WebDriverWait(self.driver,1000,0.5).until(
            EC.presence_of_element_located((By.ID,"routeSelectionList"))
        )



if __name__ == '__main__':

    a= bus_search_powful()

    a.run({"from":"Halte Zwijnaarde Technologiepark (200659)","to":"Halte Gent Zuid Perron 3 (201269)"})

    a.get_detail_page()