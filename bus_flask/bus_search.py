
import requests
import arrow
import re


class bus_search():

    def __init__(self):

        self.url_home ='https://www.delijn.be/rise-api-core/haltes/doorkomstenditmoment/201659/13'
        self.url_work ="https://www.delijn.be/rise-api-core/haltes/doorkomstenditmoment/200223/13"
        self.url = "https://www.delijn.be/rise-api-core/haltes/doorkomstenditmoment/{}/13"
        self.result = []
        self.now = arrow.utcnow().shift(hours=1)

    def ask(self, a):
        if a == "home":
            self.url = self.url_home
        elif a == "work":
            self.url = self.url_work
        else:
            self.url = self.url.format(a)

    def get(self):
        html = requests.get(self.url)
        list = html.json()["lijnen"]
        for i in list:
            number = i["lijnNummerPubliek"]
            time = i["vertrekTijd"]
            judge = re.findall("(\d+)\'", time)

            if judge:
                minutes = int(judge[0])
                b = self.now.shift(minutes=minutes)
                if b.minute < 10:
                    minutes = "0" + str(b.minute)
                else:
                    minutes = str(b.minute)
                time = str(b.hour) + ":" + minutes
            self.result.append((number, time))

    def direct_bus(self, direction="home"):
        self.ask(direction)
        self.get()
        if direction =="home" or direction == "work":
            direct_bus_number = []
            for i in self.result:
                if i[0] == "70" or i[0] == "71" or i[0] == "72":
                    direct_bus_number.append(i)
            return direct_bus_number
        else:
            return self.result



