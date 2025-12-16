import requests
import urllib.parse


class temp():
    _counter = 0

def getLinks(link):
    cookies = {
        'iac_o': '0',
        'rtb': '20000',
        'OptanonConsent': 'isGpcEnabled=1&datestamp=Sat+Nov+23+2024+23%3A33%3A33+GMT%2B0300+(Moscow+Standard+Time)&version=202404.1.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=8a3debe9-1248-42e9-a542-9dfeed3c0dc1&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.ask.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'iac_o=0; rtb=20000; OptanonConsent=isGpcEnabled=1&datestamp=Sat+Nov+23+2024+23%3A33%3A33+GMT%2B0300+(Moscow+Standard+Time)&version=202404.1.0&browserGpcFlag=1&isIABGlobal=false&hosts=&consentId=8a3debe9-1248-42e9-a542-9dfeed3c0dc1&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.ask.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A0',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    j = 0
    _urls = []
    while j < 3:
        j += 1
        _string = str(urllib.parse.quote_plus(link)).replace(":", "%3a").replace(".", "%2e").replace(".", "%3d").replace("\"", "%22")
        print(_string)
        params = {
            'ueid': 'a4816567-7917-4e21-ba41-cd096afc2e23',
            'o': '0',
            'an': 'organic',
            'ad': 'Other SEO',
            'qo': 'pagination',
            'page': f'{j}',
            'q': f'{_string}',
        }
        response = requests.get('https://www.ask.com/web', params=params, cookies=cookies, headers=headers)
        # print(response.text.split("window.MESON.initialState =")[1].split("};")[0])
        try:
            nedeed_json = response.text.split("window.MESON.initialState =")[1].split("};")[0]
            for i in range(len(nedeed_json.split("\""))):
                if "url" in nedeed_json.split("\"")[i] and "http" in nedeed_json.split("\"")[i+2] and "ask.com" not in nedeed_json.split("\"")[i+2]:
                    if nedeed_json.split("\"")[i+2] not in _urls:
                        _urls.append(nedeed_json.split("\"")[i+2])
                        temp._counter += 1
                        print(f"[{str(temp._counter)}]" + nedeed_json.split("\"")[i+2])
                        save.write(nedeed_json.split("\"")[i+2] + "\n")
        except:
            print(response.text)
            exit()

fil = "E:\\#projects_py\\bing_parser\\in.txt"
save = open('output.txt', 'w')
with open(fil, 'r') as file:
    for line in file:
        link = line.replace("\n", "")
        print(f"[{str(temp._counter)}][+] Get links from -> {link}")
        getLinks(link)

# link = "qwe"
# getLinks(link)