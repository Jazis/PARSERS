import requests, time, threading

class temp():
    _counter = 0

def getLinks(link):
    cookies = {
        'MUID': '2B08C7CC7DB062423E5CD28C7CB96322',
        'MUIDB': '2B08C7CC7DB062423E5CD28C7CB96322',
        '_EDGE_V': '1',
        'SRCHD': 'AF=NOFORM',
        'SRCHUID': 'V=2&GUID=0FB347D9E0284363BA6253EA4CD8B0E5&dmnchg=1',
        '_SS': 'SID=20B403CDEF6D60C72BEC168DEE64612D',
        '_HPVN': 'CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0xMS0yM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxLCJUb2JuIjowfQ==',
        'ak_bmsc': 'DFD60419DBE6997B6D0A19F0A650DAE4~000000000000000000000000000000~YAAQJJhUaLBKWVeTAQAAVdjmWhmQCpdEmVkjVLszOaQlO45m/xbkY7iWiRxg2askc50NaxqRSrDc+72XMUSG7eLGvUJSIjQMSUQck+g+X2EBfo/Sb90ygOhlaIVIQNErYHyPIJt8ZvhFKOSnTn6oG1Up4ZlFj3S/HrVRViANVVjn6xFOl0Ig7oALeQ5rfGYYuX4M60xi5Equ8Fq4TcnI7I94dWWrqTqCwQCf/xt0taswplvwqEnUus7dnl4OK8Wze3ACypDVgNv+zKDMZUE50WjKooshbMI3G2TgJ7CO/Vw2SB0hczsW0GaOghBN/fpDBNcJ4HsfiK5u2XJGrluaLhu/CJbECHjaMUtCXPqySgyg/G95gkIH0PoFW8OsJakkBReGkR4nF2A=',
        'SRCHUSR': 'DOB=20241123&T=1732396898000',
        '_EDGE_S': 'F=1&SID=20B403CDEF6D60C72BEC168DEE64612D&mkt=ru-ru',
        'ipv6': 'hit=1732400501351&t=4',
        'SRCHHPGUSR': 'SRCHLANG=en&IG=F95995155B094D68AF57381F600B126D&DM=1&BRW=XW&BRH=T&CW=1718&CH=1304&SCW=1718&SCH=1304&DPR=1.0&UTC=180&WTS=63867993698&HV=1732396901&PV=15.0.0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'MUID=2B08C7CC7DB062423E5CD28C7CB96322; MUIDB=2B08C7CC7DB062423E5CD28C7CB96322; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=0FB347D9E0284363BA6253EA4CD8B0E5&dmnchg=1; _SS=SID=20B403CDEF6D60C72BEC168DEE64612D; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0xMS0yM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxLCJUb2JuIjowfQ==; ak_bmsc=DFD60419DBE6997B6D0A19F0A650DAE4~000000000000000000000000000000~YAAQJJhUaLBKWVeTAQAAVdjmWhmQCpdEmVkjVLszOaQlO45m/xbkY7iWiRxg2askc50NaxqRSrDc+72XMUSG7eLGvUJSIjQMSUQck+g+X2EBfo/Sb90ygOhlaIVIQNErYHyPIJt8ZvhFKOSnTn6oG1Up4ZlFj3S/HrVRViANVVjn6xFOl0Ig7oALeQ5rfGYYuX4M60xi5Equ8Fq4TcnI7I94dWWrqTqCwQCf/xt0taswplvwqEnUus7dnl4OK8Wze3ACypDVgNv+zKDMZUE50WjKooshbMI3G2TgJ7CO/Vw2SB0hczsW0GaOghBN/fpDBNcJ4HsfiK5u2XJGrluaLhu/CJbECHjaMUtCXPqySgyg/G95gkIH0PoFW8OsJakkBReGkR4nF2A=; SRCHUSR=DOB=20241123&T=1732396898000; _EDGE_S=F=1&SID=20B403CDEF6D60C72BEC168DEE64612D&mkt=ru-ru; ipv6=hit=1732400501351&t=4; SRCHHPGUSR=SRCHLANG=en&IG=F95995155B094D68AF57381F600B126D&DM=1&BRW=XW&BRH=T&CW=1718&CH=1304&SCW=1718&SCH=1304&DPR=1.0&UTC=180&WTS=63867993698&HV=1732396901&PV=15.0.0',
        'dnt': '1',
        'ect': '4g',
        'priority': 'u=0, i',
        'referer': 'https://www.bing.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"131.0.6778.86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.86", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
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
    while j < 1:
        time.sleep(3)
        j += 1
        params = {
            'q': f'{link}',
            'form': 'QBLH',
            'sp': '-1',
            'lq': '0',
            'pq': 'qwe',
            'sc': '0-3',
            'qs': 'n',
            'sk': '',
            'cvid': 'F95995155B094D68AF57381F600B126D',
            'ghsh': '0',
            'ghacc': '0',
            'ghpl': '',
        }
        response = requests.get('https://www.bing.com/search', params=params, cookies=cookies, headers=headers)
        # print(response.text.split("window.MESON.initialState =")[1].split("};")[0])
        try:
            nedeed_json = response.text
            for i in range(len(nedeed_json.split("\""))):
                # print(response.text)
                if "http" in nedeed_json.split("\"")[i] and "bing" not in nedeed_json.split("\"")[i] and "{" not in nedeed_json.split("\"")[i]:
                    if nedeed_json.split("\"")[i] not in _urls:
                        if " " in nedeed_json.split("\"")[i]:
                            for j in range(len(nedeed_json.split("\"")[i].split(" "))):
                                if "http" in nedeed_json.split("\"")[i].split(" ")[j]:
                                    _urls.append(nedeed_json.split("\"")[i].split(" ")[j])
                                    temp._counter += 1
                                    print(f"[{str(temp._counter)}]" + nedeed_json.split("\"")[i].split(" ")[j])
                                    save.write(nedeed_json.split("\"")[i].split(" ")[j] + "\n")
                                    continue
                        _urls.append(nedeed_json.split("\"")[i])
                        temp._counter += 1
                        print(f"[{str(temp._counter)}]" + nedeed_json.split("\"")[i])
                        save.write(nedeed_json.split("\"")[i] + "\n")
        except:
            continue

fil = "E:\\#projects_py\\bing_parser\\_dorks.txt"
save = open('output.txt', 'w')
with open(fil, 'r', encoding="utf-8") as file:
    for line in file:
        link = line.replace("\n", "")
        print(f"[{str(temp._counter)}][+] Get links from -> {link}")
        threading.Thread(target=getLinks, args=(link, )).start()
        time.sleep(10)
        # getLinks(link)

# link = "qwe"
# getLinks(link)