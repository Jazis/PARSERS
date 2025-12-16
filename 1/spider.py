import requests
import os

sites = []

print "Input site:"
site = 'http://fa.ru/'

temp0 = open('temp0', 'w')
temp1 = open('urls', 'w+')
req0 = requests.get(site).text.encode('utf-8')
temp0.write(req0)


class temp():
    cc = 0
    x = 0

def sitess():
    temp.cc = len(sites)
    check(temp1)

def check(temp1):
    try:
        print sites[temp.x]
        print temp.x
        for temp.x in range(temp.cc):
            temp0 = open('temp0', 'w')
            req0 = requests.get(sites[temp.x]).text.encode('utf-8')
            temp0.write(req0)
            with open('temp0', 'r') as file:
                for line in file:
                    if 'href' in line:
                        line1 = line.split('"')
                        for i in range(len(line1)):
                            if 'http' in line1[i]:
                                print line1[i].replace('&#58;',':')
                                temp1.write(line1[i].replace('&#58;',':')+ '\n')
                                if line1[i].replace('&#58;',':') not in sites:
                                    sites.append(line1[i].replace('&#58;',':'))
                                else:
                                    pass
        temp.x += 1
        sitess()
    except requests.exceptions.InvalidSchema:
        temp.x += 1
        sitess()


with open('temp0', 'r') as file:
    for line in file:
        if 'href' in line:
            line1 = line.split('"')
            for i in range(len(line1)):
                if 'http' in line1[i]:
                    print line1[i].replace('&#58;',':')
                    temp1.write(line1[i].replace('&#58;',':')+ '\n')
                    if line1[i].replace('&#58;',':') not in sites:
                        sites.append(line1[i].replace('&#58;',':'))
                    else:
                        pass
sitess()