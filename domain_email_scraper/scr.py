import os
import time
import requests

i=0
print "Input domain:"
domain = '@fa.ru' #raw_input()
temp = open('temp', 'w')
save = open('emails.txt', 'w')
print "Input you link:"
link = 'http://www.old.fa.ru/university/rectorate/Pages/rector.aspx' #raw_input()
req0 = requests.get(link).text.encode('utf-8').strip()
temp.write(req0)
with open('temp', 'rb') as file:
    for line in file:
        if domain and 'mailto:' in line:
            x = len(line.strip())
            for i in range(x):
                if domain in line.strip()[i]:
                    save.write(line.strip()[i])
                    i += 1
                else:
                    i += 1

save.close()
temp.close()