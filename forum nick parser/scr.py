# -*- coding: utf-8 -*-
import os
import requests
import time
import random


i = random.randint(100000000, 900000000)

temp_file0 = open('temp_dont_touch.txt', 'w')

for i in range(1000000000):
    req0 = requests.get('http://www.woman.ru/user/'+ str(i) +'/').text
    if '<h3 class="profile-title">' in req0:
        print 'Good ' + str([i])
        temp_file0.write(req0.encode('utf-8'))
    else:
        print 'Bad ' + str([i])

temp_file0.close()
