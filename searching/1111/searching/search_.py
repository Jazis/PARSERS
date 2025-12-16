# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import os
import requests
import time

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='crew_db',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
files = os.listdir('C:\\Users\\Jazis\\Desktop\\searching\\sorting\\')
print(files)
for i in range(len(files)):
    quer_bukv = str(files[i][0]) + str(files[i][1])
    # print(quer_bukv)
    with open('C:\\Users\\Jazis\\Desktop\\searching\\sorting\\' + str(files[i]), 'r') as file:
        with connection.cursor() as cursor:
            try:
                sql = "CREATE TABLE {0} (combos text);".format(str(quer_bukv))
                cursor.execute(sql)
                result = cursor.fetchone()
                connection.commit()
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass
            except pymysql.err.InternalError:
                pass
            try:
                folder_file = 'C:/Users/Jazis/Desktop/searching/sorting/' + str(files[i])
                # print('' + str(files[i].replace('\\', '/')))
                sql = "LOAD DATA INFILE '{0}' IGNORE INTO TABLE {1} (combos);".format(str(folder_file), str(quer_bukv))
                print('[+] DATA LOADED ' + str(files[i]))
                cursor.execute(sql)
                result = cursor.fetchone()
                connection.commit()
            except pymysql.err.OperationalError:
                pass
            except pymysql.err.ProgrammingError:
                pass
            except pymysql.err.InternalError:
                pass
            