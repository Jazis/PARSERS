from threading import Thread
import time

def func(qwe):
    try:
        bkv = qwe[0] + qwe[1] + qwe[2] + qwe[3]
        if qwe[0] == '8':
            qwe = qwe.replace(qwe[0], '7', 1)
            bkv = '7' + qwe[1] + qwe[2] + qwe[3]
        if qwe[0] == '9':
            qwe = qwe.replace(qwe[0], '79', 1)
            bkv = '79' + qwe[1] + qwe[2]
        # bkv = bkv.lower()
        open( 'sorting/' + bkv + '.txt', 'a+').write(qwe)
    except IndexError:
        pass
    except OSError:
        pass   

while True:
    base = input('BSE PLZ RETARD FR SRT ->')
    threads1 = []
    threads0 = []
    base = base.replace('"', '').replace("'", "").replace(' ', '')
    with open(base, 'r') as file:
        try:
            for line in file:
                try:
                    if len(threads0) >= 200:
                        time.sleep(0.1)
                        threads0 = []
                        threads1.append(line)
                        thread2 = Thread(target=func, args=(line, ))
                        thread2.start()
                    else:
                        try:
                            threads1 = []
                            threads0.append(line)
                            thread1 = Thread(target=func, args=(line, ))
                            thread1.start()
                        except RuntimeError:
                            pass
                except RuntimeError:
                    pass
        except UnicodeDecodeError:
            pass