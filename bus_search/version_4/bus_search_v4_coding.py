## 在第三版的基础上，进一步分析数据，通过直接爬取ajax 接口的方式，直接爬取了json 的数据
## 可以发现在url 中只是车站的编号发生了变化，在编号后边的13 应该是显示多少个公交信息
## 在分析ajax时 在chrome的控制栏里直接 找xhr格式的类型数据，点击preview查看jison 的数据类型情况，通过requests的json方法直接转化为字典类型
## 效率提升很多
import requests

class bus_search():

    def __init__(self):

        self.url_home ='https://www.delijn.be/rise-api-core/haltes/doorkomstenditmoment/201659/13'
        self.url_work ="https://www.delijn.be/rise-api-core/haltes/doorkomstenditmoment/200223/13"
        self.url = ""
        self.result = []

    def ask(self, a):
        if a == "home":
            self.url = self.url_home
        elif a == "work":
            self.url = self.url_work

    def get(self):
        html = requests.get(self.url)
        list = html.json()["lijnen"]
        for i in list:
            number = i["lijnNummerPubliek"]
            time = i["vertrekTijd"]
            self.result.append((number,time))
        return self.result


