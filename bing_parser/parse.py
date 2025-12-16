#-*- coding: UTF-8 -*-
import json
import requests
import urllib.request as ur
from bs4 import BeautifulSoup

cookies = {
    'iac_o': '0',
    'rtb': '20000',
    'OptanonConsent': 'isGpcEnabled=1&datestamp=Tue+May+28+2024+18%3A44%3A50+GMT%2B0300+(Moscow+Standard+Time)&version=202404.1.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=5fd466e4-2897-4359-a4ba-e41e96c4e985&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.ask.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'iac_o=0; rtb=20000; OptanonConsent=isGpcEnabled=1&datestamp=Tue+May+28+2024+18%3A44%3A50+GMT%2B0300+(Moscow+Standard+Time)&version=202404.1.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=5fd466e4-2897-4359-a4ba-e41e96c4e985&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.ask.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.ask.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}


#print "Zapros"
#zapros = raw_input()
 #inurl:"cart.php" intext:"Warning"
def start(zapros):
    # temp = open('temp', 'w')
    save = open('output.txt', 'a')
    for i in range (5):
        print('https://www.ask.com/web?q=qwe' + str(zapros.replace(" ", "+")) + '&page=' + str(i))
        qw = zapros.replace(".", "+.+").replace("?", "+%3F+").replace("=", "+%3D+")
        # https://www.ask.com/web?q=Login+Aspx+Page&qo=relatedSearchNarrow&o=1473171&l=dir&ad=semA&ueid=ef7e2ea1-fd28-4c31-91ad-e28e23ab7329
        # req0 = requests.get('https://www.ask.com/web?q=' + str(zapros.replace(" ", "+")) + '&page=' + str(i)).text.encode('utf-8')
        # req0 = requests.get('https://www.ask.com/web?q=' + str(zapros) + '&page=' + str(i)).text.encode('utf-8')
        params = {
            'q': str(qw),
            'o': str(i),
        }
        response = requests.get('https://www.ask.com/web', params=params, cookies=cookies, headers=headers).text.split("window.MESON.initialState = ")[1].split("window.MESON.loadedLang")[0].replace("\n", "").replace("}};", "}}")
        # print(response)
        jsn = json.loads(response)
        print(jsn["siteConfig"])
        exit()
        for link in soup.findAll('a'):
            print(link.get('href'))
            save.write(link.get('href'))
            
        # for i in range(len(str(req0).split('<a href="'))):
        #     if "http" in str(req0).split('<a href="')[i].split("\"")[0]:
        #         print(str(req0).split('<a href="')[i].split("\"")[0])
        #         save.write(str(req0).split('<a href="')[i].split("\"")[0] + "\n")
    

save = open('output.txt', 'w')
# fil = input("Input file with dorks ->")
# fil = "C:\\Users\\Jazis\\Desktop\\bing_parser\\Dorks-11.03.23-16.56.15.txt"
fil = "D:\\#projects_py\\bing_parser\\in.txt"

with open(fil, 'r') as file:
    for line in file:
        zapros = line.replace("\n", "")
        start(zapros)

save.close()


# https://www.ask.com/web?q=Login%20Aspx%20Page&qo=pagination&o=1473171&l=dir&ad=semA&ueid=ef7e2ea1-fd28-4c31-91ad-e28e23ab7329&qsrc=998&page=2