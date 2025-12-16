import os
import string
import time
import requests
import random
i = 0
token = ''

class schet():
    count0 = 0

print "><"
kol0 = input()
my_file0 = open('temp.txt','w')
my_file1 = open('log.txt','w')

def id_generator(token):
    token = ''.join(random.choice(string.ascii_lowercase + string.digits + string.uppercase) for x in range(10))
    try_connect(token)

def try_connect(token):
    schet.count0 += 1
    print str([schet.count0]) + 'Trying : ' + str([token])
    req0 = requests.get('https://anonfiles.com/' + token).text.encode('utf-8')
    my_file0.write(req0)
    with open('temp.txt', 'rb') as file:
        for line in file:
            if 'The file you are looking for does not exist!' in line:
                print 'Huita\t' + str(schet.count0)
            if '<h1 class="text-center text-wordwrap">' in line:
                print line.replace('<h1 class="text-center text-wordwrap">', '').replace('</h1>', ''), token
                my_file1.write(line.replace('<h1 class="text-center text-wordwrap">', '').replace('</h1>', ''), token)
    open("temp.txt","w").close()
    
for i in range(kol0):
    id_generator(token)

my_file0.close()
my_file1.close()