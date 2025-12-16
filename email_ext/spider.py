import os
import requests
import time

print "Input site"
site = raw_input('URL which you want -> ')

site00 = site.split('/')[2].split('.')[-2]
temp0_save = open('temp0', 'w')
temp1_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt', 'w')
temp2_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'emails.txt', 'w')

# print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1],'output')

sites_score = []
app_words = []

req0 = requests.get(site).text.encode('utf-8')
temp0_save.write(req0)

count = 0
count2 = 0
def check( temp1_save, sites_score, site, count, count2, app_words):
    try:
        x = 0
        for x in range(len(sites_score)):
            if 'h' in sites_score[x][0]:
                temp = open('temp0', 'w')
                if site.split('/')[2] in sites_score[x]:
                    try:
                        req1 = requests.get(sites_score[x]).text.encode('utf-8')
                    except requests.exceptions.SSLError:
                        pass
                else:
                    # print sites_score[x]
                    next
                temp.write(req1)
                with open('temp0', 'r') as file:
                    for line in file:
                        if 'href' in line or 'src' in line:
                            if 'mailto:' in line:
                                new_line0 = line.split('"')
                                for i in range(len(line.split('"'))):
                                    if '@' in line.split('"')[i]:
                                        try:
                                            new_line1 = line.split('"')[i].split(':')[1].split('>')[0]
                                            if ' ' in new_line1:
                                                pass
                                            else:
                                                if '@' in new_line1 and '.' in new_line1:
                                                    if new_line1 in app_words:
                                                        pass
                                                    else:
                                                        app_words.append(new_line1)
                                                        temp2_save.write(new_line1 + '\n')
                                        except IndexError:
                                            pass
                                # temp2_save.write(line)
                                # print line
                                count2 += 1
                            new_line0 = line.split('"')
                            for i in range(len(new_line0)):
                                if '/' in new_line0[i] and '<' not in new_line0[i]:
                                    if '/' in new_line0[i][0]:
                                        new_line2 = str(site) + str(new_line0[i]).replace('/>','')
                                        if new_line2 not in sites_score:
                                            if site00 in new_line2:
                                                temp1_save.write(new_line2.strip() + '\n')
                                                sites_score.append(new_line2)
                                                if site.split('/')[2] in new_line2:
                                                    count += 1
                                    elif 'http' in new_line0[i]:
                                        if new_line0[i] not in sites_score:
                                            if '&#58;' in new_line0[i]:
                                                new_line0[i].replace('&#58;', ':')
                                                pass
                                            else:
                                                sites_score.append(new_line0[i])
                                                if site00 in new_line0[i]:
                                                    temp1_save.write(new_line0[i].strip() + '\n')
                                                    if site.split('/')[2] in new_line0[i]:
                                                        count += 1
                print str(len(sites_score)) + str([count]) + str([count2])
            else:
                next

        check(temp1_save, sites_score, site, count, count2, app_words)
    except KeyboardInterrupt:
        print '\nExiting....'
        exit

with open('temp0', 'r') as file:
    for line in file:
        if 'href' in line or 'src' in line:
            new_line0 = line.split('"')
            for i in range(len(new_line0)):
                if '/' in new_line0[i] and '<' not in new_line0[i]:
                    if '/' in new_line0[i][0]:
                        new_line2 = str(site) + str(new_line0[i]).replace('/>','')
                        if new_line2 not in sites_score:
                            temp1_save.write(new_line2.strip() + '\n')
                            sites_score.append(new_line2)
                    elif 'http' in new_line0[i]:
                        if new_line0[i] not in sites_score:
                            if '&#58;' in new_line0[i]:
                                new_line0[i].replace('&#58;', ':')
                                pass
                            else:
                                sites_score.append(new_line0[i])
                                temp1_save.write(new_line0[i].strip() + '\n')
    print len(sites_score)
    check(temp1_save, sites_score, site, count, count2, app_words)


temp0_save.close()
temp1_save.close()
temp2_save.close()
print "Done"
raw_input()
