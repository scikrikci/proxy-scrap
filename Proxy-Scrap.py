import requests
from bs4 import BeautifulSoup as bs4
from time import sleep
import json

class Proxy():

    def login(self):
        proxy_sites_url = "https://socks-proxy.net/"
        banned_site_url = "https://www.gsmarena.com/"
        
        r= requests.get(proxy_sites_url)
        soup = bs4(r.content,"html.parser")

        data = soup.find_all("table",{"class":"table table-striped table-bordered"})
        # print(data)

        tablo = (data[0].contents)[len(data[0].contents)-1]
        # print(tablo)

        tablo = tablo.find_all("tr")
        # print(tablo)

        Dict = []
        for tr in tablo:

            port = tr.find_all("td")[0].text
            ip = tr.find_all("td")[1].text
            httpss = tr.find_all("td")[6].text

            proxy = f"{port}:{ip}"
            print(proxy)

            Dict.append(proxy)

        print(json.dumps(Dict,indent=4))
        json_string = json.dumps(Dict,indent=4)

        with open('proxy_json_data.json', 'w') as outfile:
            json.dump(json_string, outfile)

if __name__ == "__main__":

    scrap = Proxy()
    scrap.login()
    quit()



