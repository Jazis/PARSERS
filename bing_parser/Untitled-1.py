#-*- coding: UTF-8 -*-
import os
import requests
import time
import threading


THREADS = 50



class temp():
    threads = []
    sites = []

class counters():
    counter0 = 0
    counter1 = 0

def start(zapros, k):
    try:
        for i in range (5):
            req0 = requests.get("https://search.mysearch.com/web?q="+ str(zapros) +"&tpr=10&page="+ str(i) +"&&ts=1602334586987&ssrt=165").text.encode('utf-8')
            for j in range(len(str(req0).split("\""))):
                if "http" in str(req0).split("\"")[j] and "/" in str(req0).split("\"")[j] and "mysearch" not in str(req0).split("\"")[j]:
                    if "?" in str(req0).split("\"")[j] and "=" in str(req0).split("\"")[j] and "." in str(req0).split("\"")[j]:
                        counters.counter1 += 1
                        open('may_sql.txt', 'a+').write(str(req0).split("\"")[j].split("<")[0] + '\n')
                    open('output.txt', 'a+').write(str(req0).split("\"")[j].split("<")[0] + '\n')
                    counters.counter0 += 1
                    print(
                        "Sites in arr ->" + str(counters.counter0) + 
                        " | " + str(counters.counter1) + 
                        " | Threads -> " + str(len(temp.threads)) + 
                        ""
                        )
        temp.threads.remove(f"thread_{str(k)}")
    except:
        temp.threads.remove(f"thread_{str(k)}")


save0 = open('output.txt', 'w')
save1 = open('may_sql.txt', 'w')

fil = input("Input file with dorks")

i = 0
with open(fil, 'r') as file:
    for line in file:
        i+=1
        while len(temp.threads) >= THREADS:
            time.sleep(1)
        else:
            time.sleep(1)
            thread_name = f"thread_{str(i)}"
            temp.threads.append(thread_name)
            thread0 = threading.Thread(name = thread_name,target = start, args = (line, i))
            thread0.start()

save.close()