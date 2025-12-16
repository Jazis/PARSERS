import os
import requests
import time

print "Input site"
site = 'http://www.fa.ru/Pages/Home.aspx'#raw_input()

site00 = site.split('/')[2].split('.')[-2]
temp0_save = open('temp0', 'w')
temp1_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'urls.txt', 'w')
temp2_save = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'emails.txt', 'w')

print os.path.abspath(__file__).replace(os.path.abspath(__file__).split('\\')[-1],'output')

sites_score = []
dork_score = []

req0 = requests.get(site).text.encode('utf-8')
temp0_save.write(req0)

count = 0
count2 = 0
def check( temp1_save, sites_score, site, count, count2, dork_score):
    try:
        x = 0
        for x in range(len(sites_score)):
            if 'h' in sites_score[x][0]:
                temp = open('temp0', 'w')
                if site.split('/')[2] in sites_score[x]:
                    req1 = requests.get(sites_score[x]).text.encode('utf-8')
                    pass
                else:
                    print sites_score[x]
                    next
                temp.write(req1)
                with open('temp0', 'r') as file:
                    for line in file:
                        if 'href' in line or 'src' in line:
                            i = 0  
                            for i in range(len(line.split('"'))):
                                if 'name' in line.split('"')[i]:
                                    if line.split('"')[i+1] in dork_score:
                                        pass
                                    else:
                                        dork_score.append(line.split('"')[i+1])
                                        count2 += 1  
                                        print line.split('"')[i+1]
                                        temp2_save.write(line.split('"')[i+1])
                            new_line0 = line.split('"')
                            time.sleep(0.001)
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

        check(temp1_save, sites_score, site, count, count2, dork_score)
    except KeyboardInterrupt:
        print 'Exiting....'
        exit

with open('temp0', 'r') as file:
    for line in file:
        if 'href' in line or 'src' in line:
            i = 0  
            for i in range(len(line.split('"'))):
                if 'name' in line.split('"')[i]:
                    if line.split('"')[i+1] in dork_score:
                        pass
                    else:
                        dork_score.append(line.split('"')[i+1])
                        count2 += 1  
                        print line.split('"')
                        temp2_save.write(line.split('"')[i+1])
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
    check(temp1_save, sites_score, site, count, count2, dork_score)


temp0_save.close()
temp1_save.close()
temp2_save.close()
print "Done"
raw_input()
