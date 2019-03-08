from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class weibo():

    def __init__(self):
        self.log_success = "https://www.weibo.com/u/6278530071/home?wvr=5&lf=reg"
        self.log_url = "https://www.weibo.com/overseas"
        self.path = r"D:\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path =self.path)

    def log_in(self):

        self.driver.get(self.log_url)
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be(self.log_success)
        )

        print("successful")

    def search_choujiangjun(self):

        self.driver.get("https://www.weibo.com/u/6196818433?profile_ftype=1&is_all=1#_0")
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@class="pos"]/a[@title="搜索"]')))
        input_search = self.driver.find_element_by_xpath("//input[@value='搜索他的微博']")
        input_search.send_keys("开奖集合")
        input_button = self.driver.find_element_by_xpath("//span[@class='pos']/a[@title='搜索']")
        input_button.click()


    def search_1(self):

        self.driver.get("https://www.weibo.com/u/3805466479?profile_ftype=1&is_all=1#_0")
        WebDriverWait(self.driver,1000).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="pos"]/a[@title="搜索"]')))
        input_search = self.driver.find_element_by_xpath("//input[@value='搜索她的微博']")
        input_search.send_keys("看到扣1，见者好运！转过88揪一位粉丝发红包哦… 真的很容易中")
        input_button = self.driver.find_element_by_xpath("//span[@class='pos']/a[@title='搜索']")
        input_button.click()

    def get_content(self):

        pass


if __name__ == '__main__':

    a = weibo()

    a.log_in()

    a.search_choujiangjun()