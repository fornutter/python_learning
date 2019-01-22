from selenium import webdriver

import time





class search():

    def __init__(self):

        self.driver_path = r"D:\chromedriver_win32\chromedriver.exe"

        self.route = []

        self.route_one = ["Halte Zwijnaarde Technologiepark (201659)", "Station Gent-Dampoort"]

        self.route_two = ["Station Gent-Dampoort", "Halte Zwijnaarde Technologiepark (200659)"]

        self.url = "https://www.delijn.be/en/"

        self.driver = webdriver.Chrome(executable_path=self.driver_path)


    def chose_route(self,way):

        if way == "home":

            self.route = self.route_one
        elif way == "work":

            self.route = self.route_two
        else:

            print("wrong route")

    def run(self):

        self.driver.get(self.url)

        start = self.driver.find_element_by_id("search-start")

        finish = self.driver.find_element_by_id("search-finish")



        start.send_keys(self.route_one[0])

        finish.send_keys(self.route_one[1])

        time.sleep(3)

        button = self.driver.find_element_by_xpath(
            '//div[@class="search-input-group search-bottom"]/div[@class="search-input-button real-input search-input"]/button')

        button.click()



if __name__ == '__main__':

    a = search()

    a.chose_route("home")
    a.run()







