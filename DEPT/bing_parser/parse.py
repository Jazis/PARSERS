#-*- coding: UTF-8 -*-
import os
import requests
import time

sql_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-2], 'settings') + 'sql.ini'
sql_words_dir = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'settings') + 'sql_words.ini'
temp2_save = os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'may_sql.txt'
save_file0 = open(os.path.abspath(__file__).replace(os.path.abspath(__file__).split('/')[-1],'output/') + 'sql_save_' + str(time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())) + '.txt', 'w')

#print "Zapros"
#zapros = raw_input()
 #inurl:"cart.php" intext:"Warning"
class checksum():
    count0 = 0 # good tries
    count1 = 0 # All tries
    site = ''
    new_line0 = ''.replace('\n', '')
    new_line1 = ''
    selection = 0
    mode_selection = 0

def not_bad(save_file0):
        checksum.count0+=1
        print str([checksum.count0]) + '- one more good link'
        save_file0.write(str(checksum.new_line0 + checksum.new_line1))
        save_file0.close()

sites = []

def first_function(new_line0, save_file0, sites):
    if new_line0.split('"')[3].split('/')[2] in sites:
        next
    elif new_line0.split('"')[3].split('/')[2] not in sites:
        sites.append(new_line0.split('"')[3])
        new_line1 = ''
        count0 = 0
        temp_0 = 'temp'
        temp_1 = open(temp_0, 'w')
        checksum.count1 += 1
        print str([checksum.count1]) + 'Lets check - ' + str([new_line0.split('"')[3]])
        try:
            req0 = requests.get(new_line0).text.encode('utf-8')
            if 'SQL syntax' in req0:
                print 'Good'
                not_bad(save_file0)
            else:
                count0+=1
                print 'BAD x' + str(count0)
            with open(sql_dir, 'r') as file:
                for line in file:
                    new_line1 = line 
                    with open(sql_words_dir, 'r') as file:
                        for line in file:
                            # print str([count1]) + '- tries'
                            # print '\t\t' + str([new_line1]) + str([line])
                            req0 = requests.get(new_line0 + new_line1).text.encode('utf-8')
                            temp_1.write(req0)
                            line_0 = line
                            checksum.new_line0 = new_line0
                            checksum.new_line1 = new_line1
                            with open(temp_0, 'r') as file:
                                for line in file:
                                    if 'SQL syntax' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'MySQL server ' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'You have an error in your SQL syntax' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'check the manual that corresponds to your MySQL server version for the right syntax to use near' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'mysql_fetch_array()' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'Warning: mysql_fetch_array()' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'Warning: mysql_' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'Database error' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'SELECT * FROM ' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'MySQL error' in line:
                                        print 'Good'
                                        not_bad(save_file0)
                                    if 'MySQL' and ':' and 'Warning' in line:
                                        print 'Good'
                                    # print 'Good job - ' + str(site) + str(line_0)
                                    # save_file0.write(str(new_line0 + new_line1) + '\n')
                                    pass
        except requests.exceptions.InvalidSchema:
            pass
        except KeyboardInterrupt:
            pass
    else:
        pass

def site_formatten(site):
    # if '/' not in site[-1]:
    #     site = site + '/'
    if '://' not in site[0-4]:
        site = 'http://' + site
        checksum.site = site
        print str(site) + " - has been formatted"

def selection_2(line):
    checksum.selection = 2
    ur_url = line
    site = ur_url
    # site_formatten(site)
    new_line0 = site
    first_function(new_line0, save_file0, sites)


def start(zapros):
    temp = open('temp', 'w')
    save = open('output.txt', 'a')
    for i in range (5):
        req0 = requests.get('https://search.mysearch.com/web?q=' + str(zapros) + '&tpr=10&page=' + str(i) +'&ts=1566914725272').text.encode('utf-8')
        temp.write(req0.strip())
    temp.close()
    with open('temp', 'r') as file:
        for line in file:
            if '<a class="algo-title " href="' in line:
                if '=' in line.split('"')[3]:
                    save.write(line.split('"')[3] + '\n')
                    print  line.split('"')[3]
                    selection_2(line)


    

save = open('output.txt', 'w')
print "Input file with dorks"
fil = raw_input()
fil = fil.replace('"', '').replace("'", "").replace(' ', '')


with open(fil, 'r') as file:
    for line in file:
        zapros = line
        start(zapros)

save.close()