# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import os
import requests
import time

def create_tables():
    counter = 0
    counter0 = 0
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    # open('out.txt', 'w')
    simbols = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9,-,_,.,$,%,^,&,*,+"
    for i in range(len(simbols.split(','))):
        #print(simbols.split(',')[i])
        for x in range(len(simbols.split(','))):
            for l in range(len(simbols.split(','))):
                # print(simbols.split(',')[i], simbols.split(',')[x], simbols.split(',')[l])
                symbol = simbols.split(',')[i] + simbols.split(',')[x] + simbols.split(',')[l]
                try:
                    with connection.cursor() as cursor:
                        # Create a new record
                        # sql = "INSERT INTO output_infos VALUES(''"+ str(unique_id) +"', '" + str(NICKNAME) + "', 'http:\\\\192.168.1.2\\uploads\\" + str(link) + "');"
                        sql =  "CREATE TABLE {0} (combos text);".format(symbol)
                        cursor.execute(sql)
                        result = cursor.fetchone()
                        # print(result)
                        connection.commit()
                        # time.sleep(0.1)
                        counter +=1
                        counter0 += 1
                        if counter0 == 10000:
                            print('[+]PUM PUM PURUM - 10000')
                            counter0 = 0
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass
    #            finally:
    #               connection.close()
    print('[0]TABLES' + [counter])

def base_adding():
    counter = 0 
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    base = input('bse plz -> ')
    base = base.replace('"', '').replace("'", "").replace(' ', '')
    with open(base, 'r') as file:
        for line in file:
            if '@' in line and ':' in line and '.' in line:
                bd_searcher = line[0] + line[1]
                bd_searcher = bd_searcher.lower()
                try:
                    with connection.cursor() as cursor:
    #                   print('12112')
                        #print(str(bd_searcher))
                        sql = "SELECT * FROM `{0}` WHERE `combos` LIKE '{1}'".format(bd_searcher, str(line).replace('\n', ''))
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        #print(len(rows))
                        if len(rows) > 0:
                            pass
                            counter += 1
                            print("[-] ALREADY = ", [counter])
                        else:     
                            sql = "INSERT IGNORE INTO `{0}` (`combos`) VALUES ('{1}')".format(bd_searcher, str(line).replace('\n', ''))
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            # print(result)
                            connection.commit()
                            counter += 1
                            print("[+] COUNTER = ", [counter])
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass
    print('Ready', [counter])
    connection.close()

def searching():
    quer = input('Y0ur query -> ')
    quer_bukv = quer[0] + quer[1]
    quer_bukv = quer_bukv.lower()
    print('------------------------')
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
        #   print('12112')
            #print(str(bd_searcher))
            sql = "SELECT * FROM `{0}` WHERE `combos` LIKE '%{1}%'".format(quer_bukv, quer)
            cursor.execute(sql)
            rows = cursor.fetchall()
            # print(len(rows))
            if len(rows) == 0:
                print('>:(')
            for row in rows:
                for i in range(len(str(row).split("'"))):
                    if ':' in str(row).split("'")[i] and '@' in str(row).split("'")[i] and '.' in str(row).split("'")[i]:
                        rr = str(row).split("'")[i]
                        print(rr)
            connection.commit()
            time.sleep(0.1)
    except pymysql.err.OperationalError:
        pass
    except pymysql.err.ProgrammingError:
        pass
    print('------------------------')


def base_sorting():
    counter0 = 0
    counter1 = 0
    while True:
        base = input('BSE PLZ RETARD FR SRT ->')
        base = base.replace('"', '').replace("'", "").replace(' ', '')
        with open(base, 'r') as file:
            try:
                for line in file:
                    try:
                        bkv = line[0] + line[1] + line[2]
                        bkv = bkv.lower()
                        open( 'sorting1\\' + bkv + '.txt', 'a+').write(line)
                        # counter0 += 1
                        # counter1 += 1
                        # if counter1 == 100000:
                        #     print(counter0)
                        #     counter1 = 0
                    except IndexError:
                        pass
                    except UnicodeDecodeError:
                        pass
                    except FileNotFoundError:
                        pass
            except UnicodeDecodeError:
                pass

def base_sorting_struct():
    while True:
        base = input('BSE PLZ RETARD FR SRT ->')
        base = base.replace('"', '').replace("'", "").replace(' ', '')
        with open(base, 'r') as file:
            for line in file:
                bkv = line[0] + line[1]
                bkv = bkv.lower()
                open( 'sorting\\' + bkv + '_struct.txt', 'a+').write("INSERT INTO `" + bkv + "`(`combos`) VALUES ('" + line.replace('\n', '') + "');\n")

def struct_adder():
    try:
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        counter = 0
        print('[+] ' + str(os.getcwd()))
        print('[+] ' + str(os.listdir(os.getcwd())))
        for i in range(len(os.listdir(os.getcwd()))):
            if '.' not in os.listdir(os.getcwd())[i]:
                folder = os.listdir(os.getcwd())[i]
        print('[+] ' + str(folder))
        for i in range(len(str(os.listdir(os.getcwd())) + '\\' + str(folder))):
            counter += 1
        print('[+] Counter -> ' + str(counter))
        counter = 0
        #print('[+] ' + str(os.listdir(os.getcwd() + '\\' + str(folder))))
        page = str(os.listdir(os.getcwd() + '\\' + str(folder)))
        for i in range(len(str(os.listdir(os.getcwd() + '\\' + str(folder))))):
            file = str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            # print(file)
            folder_file = os.getcwd() + '\\' + folder + '\\' + str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            with open(folder_file, 'r') as file:
                print('[+] ' + str(folder_file))
                for line in file:
                    try:
                        with connection.cursor() as cursor:
                            sql = line
                            cursor.execute(sql)
                            counter += 1
                            result = cursor.fetchone()
                            # print(result)
                            connection.commit()
                    except pymysql.err.OperationalError:
                        pass
                    except pymysql.err.ProgrammingError:
                        pass    
        print('Ready', [counter])
        connection.close()
    except IndexError:
        pass

def auto_struct_adder():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    counter = 0
    print('[+] ' + str(os.getcwd()))
    print('[+] ' + str(os.listdir(os.getcwd())))
    for i in range(len(os.listdir(os.getcwd()))):
        if '.' not in os.listdir(os.getcwd())[i]:
            folder = os.listdir(os.getcwd())[i]
    print('[+] ' + str(folder))
    for i in range(len(str(os.listdir(os.getcwd())) + '\\' + str(folder))):
        counter += 1
    print('[+] Counter -> ' + str(counter))
    print('[+] ' + str(os.listdir(os.getcwd() + '\\' + str(folder))))
    page = str(os.listdir(os.getcwd() + '\\' + str(folder)))
    counter = 0
    for i in range(len(str(os.listdir(os.getcwd() + '\\' + str(folder))))):
        try:
            file = str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            # print(file)
            counter += 1
            folder_file = os.getcwd() + '\\' + folder + '\\' + str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            with open(folder_file, 'r') as file:
                try:
                    with connection.cursor() as cursor:
                        cursor.execute(file.read())
                        result = cursor.fetchone()
                        connection.commit()
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass
                except pymysql.err.InterfaceError:
                    pass
        except IndexError:
            pass
    print('Ready', [counter])
    connection.close()

def single_auto_struct_adder():
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    base = input('bse plz -> ')
    base = base.replace('"', '').replace("'", "").replace(' ', '')
    with open(base, 'r') as file:
        try:
            with connection.cursor() as cursor:
                cursor.execute(file.read())
                result = cursor.fetchone()
                connection.commit()
        except pymysql.err.OperationalError:
            pass
        except pymysql.err.ProgrammingError:
            pass
    print('Ready')
    connection.close()

def load_data_infile():
    try:
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        counter = 0
        print('[+] ' + str(os.getcwd()))
        print('[+] ' + str(os.listdir(os.getcwd())))
        for i in range(len(os.listdir(os.getcwd()))):
            if '.' not in os.listdir(os.getcwd())[i]:
                folder = os.listdir(os.getcwd())[i]
        print('[+] ' + str(folder))
        for i in range(len(str(os.listdir(os.getcwd())) + '\\' + str(folder))):
            counter += 1
        print('[+] Counter -> ' + str(counter))
        #print('[+] ' + str(os.listdir(os.getcwd() + '\\' + str(folder))))
        page = str(os.listdir(os.getcwd() + '\\' + str(folder)))
        for i in range(len(str(os.listdir(os.getcwd() + '\\' + str(folder))))):
            file = str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            # print(file)
            quer_bukv = str(file)[0] + str(file)[1]
            quer_bukv = quer_bukv.lower()
            folder_file = os.getcwd() + '\\' + folder + '\\' + str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            try:
                with open(folder_file, 'r') as file:
                    with connection.cursor() as cursor:
                        try:
                            print(quer_bukv)
                            sql = "CREATE TABLE {0} (combos text);".format(str(quer_bukv))
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            connection.commit()
                        except pymysql.err.OperationalError:
                            pass
                        except pymysql.err.ProgrammingError:
                            pass
                        try:
                            sql = "LOAD DATA INFILE '{0}' IGNORE INTO TABLE {1} (combos);".format(str(folder_file.replace('\\', '\\\\')), str(quer_bukv))
                            print('[+] DATA LOADED ' + str(folder_file))
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            connection.commit()
                        except pymysql.err.OperationalError:
                            pass
                        except pymysql.err.ProgrammingError:
                            pass
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass
    except IndexError:
        pass

def load_data_infile_once():
    base = 'E:\\#2\\fullz\\base\\'
    counter2 = 0
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    counter = 0
    print('[+] ' + str(base))
    print('[+] ' + str(os.listdir(base)))
    for i in range(len(os.listdir(base))):
        if '.' not in os.listdir(base)[i]:
            folder = os.listdir(base)[i]
    print('[+] ' + str(folder))
    for i in range(len(str(os.listdir(base)) + str(folder))):
        counter += 1
    print('[+] Counter -> ' + str(counter))
    try:
        page = str(os.listdir(base + str(folder)))
        counter = 0
        for i in range(len(str(os.listdir(base  + str(folder))))):
            try:
                file = str(os.listdir(base  + str(folder))[i])
                # print(file)
                counter += 1
                folder_file = base + folder + '\\' + str(os.listdir(base + '\\' + str(folder))[i])
                try:
                    with open(folder_file, 'r') as file:
                        with connection.cursor() as cursor:
                            sql = "CREATE TABLE {0} (combos text);".format(str(quer_bukv))
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            connection.commit()
                            sql = "LOAD DATA INFILE '{0}' IGNORE INTO TABLE {1} (combos);".format(str(folder_file), str(quer_bukv))
                            print('[+] DATA LOADED ' + str(folder_file))
                            cursor.execute(sql)
                            result = cursor.fetchone()
                            connection.commit()
                except pymysql.err.OperationalError:
                    pass
                except pymysql.err.ProgrammingError:
                    pass
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass 
    except NotADirectoryError:
        pass   

def fullz_transfer():
    base = '\\media\\jazis\\nya\\#2\\fullz\\base\\'
    counter2 = 0
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='crew_db',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    counter = 0
    print('[+] ' + str(base))
    print('[+] ' + str(os.listdir(base)))
    for i in range(len(os.listdir(base))):
        if '.' not in os.listdir(base)[i]:
            folder = os.listdir(base)[i]
    print('[+] ' + str(folder))
    for i in range(len(str(os.listdir(base)) + str(folder))):
        counter += 1
    print('[+] Counter -> ' + str(counter))
    try:
        page = str(os.listdir(base + str(folder)))
        counter = 0
        for i in range(len(str(os.listdir(base  + str(folder))))):
            try:
                file = str(os.listdir(base  + str(folder))[i])
                # print(file)
                counter += 1
                folder_file = base + folder + '\\' + str(os.listdir(base + '\\' + str(folder))[i])
                with open(folder_file, 'r') as file:
                    base2 = base2.replace('"', '').replace("'", "").replace(' ', '')
                    with open(base2, 'r') as file:
                        for line in file:
                            bkv = line[0] + line[1] + line[2]
                            bkv = bkv.lower()
                            open( 'sorting\\' + bkv + '.txt', 'a+').write(line)
                            counter2 += 1
                            print('[+] COUNT ->' + str([counter2]))
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass 
    except NotADirectoryError:
        pass   

def base_separator():
    name = ''
    counter = 0
    counter0 = 0
    base = input('bse plz -> ')
    base = base.replace('"', '').replace("'", "").replace(' ', '')
    with open(base, 'r') as file:
        for line in file:
            if counter == 1000000:
                counter0 += 1
                counter = 0
                print("[+] " + str(counter0) + " +1kk")
                name = str(time.time())
            open('output\\base10kk' + str(name) + '.txt', 'a+').write(line)
            counter +=1


    


def sorting_merge():
    try:
        connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
        counter = 0
        print('[+] ' + str(os.getcwd()))
        print('[+] ' + str(os.listdir(os.getcwd())))
        for i in range(len(os.listdir(os.getcwd()))):
            if '.' not in os.listdir(os.getcwd())[i]:
                folder = os.listdir(os.getcwd())[i]
        print('[+] ' + str(folder))
        for i in range(len(str(os.listdir(os.getcwd())) + '\\' + str(folder))):
            counter += 1
        print('[+] Counter -> ' + str(counter))
        #print('[+] ' + str(os.listdir(os.getcwd() + '\\' + str(folder))))
        page = str(os.listdir(os.getcwd() + '\\' + str(folder)))
        for i in range(len(str(os.listdir(os.getcwd() + '\\' + str(folder))))):
            file = str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            # print(file)
            folder_file = os.getcwd() + '\\' + folder + '\\' + str(os.listdir(os.getcwd() + '\\' + str(folder))[i])
            with open(folder_file, 'r') as file:
                for line in file:
                    if '@' in line and ':' in line and '.' in line:
                        bd_searcher = line[0] + line[1]
                        bd_searcher = bd_searcher.lower()
                        try:
                            with connection.cursor() as cursor:
            #                   print('12112')
                                #print(str(bd_searcher))
                                sql = "SELECT * FROM `{0}` WHERE `combos` LIKE '{1}'".format(bd_searcher, str(line).replace('\n', ''))
                                cursor.execute(sql)
                                rows = cursor.fetchall()
                                #print(len(rows))
                                if len(rows) > 0:
                                    pass
                                    counter += 1
                                    print("[-] ALREADY = ", [counter])
                                else:     
                                    sql = "INSERT IGNORE INTO `{0}` (`combos`) VALUES ('{1}')".format(bd_searcher, str(line).replace('\n', ''))
                                    cursor.execute(sql)
                                    result = cursor.fetchone()
                                    # print(result)
                                    connection.commit()
                                    counter += 1
                                    print("[+] COUNTER = ", [counter])
                        except pymysql.err.OperationalError:
                            pass
                        except pymysql.err.ProgrammingError:
                            pass
        print('Ready', [counter])
        connection.close()
    except IndexError:
        pass

if __name__ == '__main__':
    selection = input(
        """
        [1] CREATE TABLE\n
        [2] Base adding\n
        [3] Searching\n
        [4] Base sorting\n
        [5] Sorting merge\n
        [6] Base sotring (struct)\n
        [7] Base adding (struct)\n
        [8] SINGLE AUTO FILE (struct)\n
        [9] AUTO FILES (struct)\n
        [10] LOAD DATA INFILE (\\SORTING) AUTOMATE | MULTI\n
        [11] LOAD DATA INFILE (\\SORTING) AUTOMATE | ONCE\n
        [12] DB SEPARATOR 1kk
        Your choice -> """)
    if selection == '1':
        create_tables()
    if selection == '2':
        base_adding()
    if selection == '3':       
        searching()
    if selection == '4':
        base_sorting()
    if selection == '5':
        sorting_merge()
    if selection == '6':
        base_sorting_struct()
    if selection == '7':
        struct_adder()
    if selection == '8':
        single_auto_struct_adder()
    if selection == '9':
        auto_struct_adder()
    if selection == '10':
        load_data_infile()
    if selection == '11':
        load_data_infile_once()
    if selection == '12':
        base_separator()
    if selection == '00':
        fullz_transfer()
    else:
        exit()