import os
import requests

cookies = {
    "df_id" : "005ab42fd245c418f90ee444b1381ad8",
    "xf_logged_in" : "1",
    "xf_market_currency" : "usd",
    "xf_session" : "1b3c32a51b5cdd9d7a83c0e70c19d8a4",
    "xf_tfa_trust" : "kV_rA2p8XsvUPBAwqEYojj5Qn9_mYcXz",
    "xf_user" : "24678%2Cc31149bd53542a6253b9b22c0c0b677b8a19739c"
}

count = 0
open('nicks.txt', 'w')

for i in range(114):
    req0 = requests.get('https://lzt.guru/threads/53064/page-' + str(i), cookies=cookies).text.encode('utf-8')
    page = []
    page.append(req0)
    for x in range(len(page[0])):
        if 'name' in page[0][i]:
            open('nicks.txt', 'a+').write(page[0][i+3].split('>')[1].split('<')[0])
            count += 1
    print count