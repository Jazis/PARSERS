import os
import requests
temp = 'temp'
save = open('save.txt', 'w+')
save = open('save.txt', 'a+')
base = raw_input('Base please: ')
base = base.replace('"', '').replace(' ', '').replace('"', '')
with open(base, 'r') as file:
    for line in file:
        print line
        # save.write(line[0:5])
        save.write(line)
        line = line[0:6]
        req0 = requests.get('https://ccbins.pro/?bins=' + line, data={'bins':line}).text.encode('utf-8')
        # print req0
        open(temp,'w').write(req0)
        with open('temp', 'r') as file:
            for line in file:
                if '<tr><th>BIN' in line:
                    bin_ = line.replace('</head><br><br><hr><br><table style="">', '').replace('&nbsp;&nbsp;</th><td>', '').replace('</td></tr>', '').replace('<tr><th>', '')
                    save.write('\t'+bin_)
                if '<tr><th>Country' in line:
                    country_ = line.replace('<tr><th>', '').replace('&nbsp;&nbsp;</th><td>', '').replace('</td></tr>', '')
                    save.write(country_)
                if '<tr><th>Vendor' in line:
                    vendor_ = line.replace('<tr><th>', '').replace('&nbsp;&nbsp;</th><td>', '').replace('</td></tr>', '')
                    save.write(vendor_)
                if '<tr><th>Type' in line:
                    type_ = line.replace('<tr><th>', '').replace('&nbsp;&nbsp;</th><td>', '').replace('</td></tr>', '')
                    save.write(type_)
                if '<tr><th>Level' in line:
                    level_ = line.replace('<tr><th>', '').replace('&nbsp;&nbsp;</th><td>', '').replace('</td></tr>', '')
                    save.write(level_)
                if '<tr><th>Bank' in line:
                    bank_ = line.replace('<tr><th>', '').replace('&nbsp;&nbsp;</th><td>', '').replace('</td></tr>', '')
                    save.write(bank_)
        save.write('___________________________________\n')
                    