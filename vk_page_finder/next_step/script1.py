#coding=utf-8
from selenium import webdriver
import time
import requests
from openpyxl import Workbook

def profile_parse():
    # wb = Workbook()
    # sheet = wb.active
    # sheet.title = 'data'
    row = 1
    page = []
    infos = []
    chrome_path = 'chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://vk.com/')
    open('saved_infos.txt', 'w')
    # sheet['A'+str(row)] = 'Name'
    # sheet['B'+str(row)] = 'Bith'
    # sheet['C'+str(row)] = 'Status'
    # sheet['D'+str(row)] = 'Phone'
    # sheet['E'+str(row)] = 'DPhone'
    # sheet['F'+str(row)] = 'Skype'
    raw_input('\n\n\n\t\t\tPress ENTER after log in\n\n\n')
    pages_file = raw_input('Input file with pages -> ')
    with open(pages_file, 'r') as file:
        for line in file:
            driver.get(str(line))
            page.append(driver.page_source.split('"'))
            for i in range(len(page[0])):
                if 'label fl_l' in page[0][i]:
                    infos.append(page[0][i+1].split('>')[1].split('<')[0])
                if '/search?c' in page[0][i]:
                    infos.append(page[0][i+1].split('>')[1].split('<')[0])
            print len(infos)
            open('saved_infos.txt', 'a+').write(str(line) + '\n' + str(infos) + '\n\n')
            infos = []
            page = []


def main():
    wb = Workbook()
    sheet = wb.active
    sheet.title = 'data'
    row = 1
    sheet['A'+str(row)] = 'Page_ID'
    sheet['B'+str(row)] = 'Name'
    count = 0
    page = []
    logins = []
    chrome_path = 'chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://vk.com/')
    while True:
        selection = raw_input('\n\n\n\t\t\tPress ENTER after log in\n\n\n')
        if selection == 'parse':
            profile_parse(driver)
        page.append(driver.page_source.split('"'))
        # print page
        for i in range(len(page[0])):
            try:
                if 'friends_field friends_field_title' in page[0][i]:
                    if page[0][i+5] in logins:
                        pass
                    else:
                        logins.append(page[0][i+5])
                        count += 1
                        # print page[0][i+5]
                        if 'friend[2]' in page[0][i+2].encode('utf-8') or 'friend[2]' in page[0][i+5].encode('utf-8'):
                            pass
                        else:
                            row += 1
                            sheet['A'+str(row)] = 'https://vk.com' + page[0][i+2].encode('utf-8')
                            if '</a>' in page[0][i+5].encode('utf-8'):
                                pass
                            else:
                                sheet['B'+str(row)] = page[0][i+2].encode('utf-8').replace('>','').split('<')[0]
                            sheet['B'+str(row)] = page[0][i+5].encode('utf-8').replace('>','').split('<')[0]
                            # open('link.txt', 'a+').write('https://vk.com' + page[0][i+2].encode('utf-8') + '\t|\t' + page[0][i+5].encode('utf-8').replace('>','').split('<')[0] +'\n')
                            wb.save('data.xlsx')
            except IndexError:
                continue
        page = []
        print "Logins - " + str(count)


if __name__ == '__main__':
    profile_parse()