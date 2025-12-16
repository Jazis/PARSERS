#-*- coding: UTF-8 -*-
import os
import requests
import time
#print "Zapros"
#zapros = raw_input()
 #inurl:"cart.php" intext:"Warning"
count = 0
def start(zapros):
    temp = open('temp', 'w')
    save = open('output.txt', 'a')
    for i in range (5):
        req0 = requests.get('https://search.mysearch.com/web?q=' + str(zapros) + '&tpr=10&page=' + str(i) +'&ts=1566914725272').text.encode('utf-8')
        temp.write(req0.strip())
    temp.close()
    if 'did not match with any results' in req0:
        print 'Nothing else'
        next
    with open('temp', 'r') as file:
        for line in file:
            if '<a class="algo-title " href="' in line:
                save.write(line.split('"')[3] + '\n')
                print  line.split('"')[3]

    

save = open('output.txt', 'w')
print "Input file with dorks"
fil = raw_input()

with open(fil, 'r') as file:
    for line in file:
        count += 1
        zapros = "intext:'" + line.replace('\n', '') + "' filetype:'.xls''.txt''.db'"
        print str([count] + [zapros])
        start(zapros)

save.close()