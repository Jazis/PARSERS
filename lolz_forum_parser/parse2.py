import os
import requests

cookies = {
    'xf_id':'b41b6b8b9ae7c5daf125515bbb140bab',
    'xf_last_read_article_date':'1573853580',
    'xf_logged_in':'1',
    'xf_session':'70adc7c7f464c0d1dbfb654e71b5f697',
    'xf_user':'24678%2Cc31149bd53542a6253b9b22c0c0b677b8a19739c',
}

emails = open('emails.txt', 'w')
i = 0

req0 = requests.get('https://lolzteam.org/', cookies=cookies).text.encode('utf-8')
if 'Grint' in req0:
    print "Auth - Success"
else:
    print "Auth - error"
    print req0
    raw_input()
    exit()

with open('links.txt', 'r') as file:
    for line in file:
        print line
        req0 = requests.get(line, cookies=cookies).text.encode('utf-8')
        line1 = line
        open('temp', 'a+').write(req0)
        # with open('temp', 'r') as file:
        #     for line in file:
        #         if '@' in line and ':' in line and '.' in line:
                    # print str(line.split('>')[1].split('</a>')[0]) + str(line.split('</a>')[1].split('<br />')[0])
                    # emails.write(str(line.split('>')[1].split('</a>')[0]) + str(line.split('</a>')[1].split('<br />')[0]) + '\n')
        i += 1
        print str(i) + '\t | \t' + str(line1)
