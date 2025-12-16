#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

# https://vk.com/search?c%5Bage_from%5D=17&c%5Bage_to%5D=17&c%5Bcity%5D=1925340&c%5Bcountry%5D=12&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bschool%5D=410008&c%5Bsection%5D=people&c%5Bsex%5D=1
# https://vk.com/search?c%5Bcity%5D=1925340&c%5Bcountry%5D=12&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bschool%5D=410008&c%5Bsection%5D=people

class temp():
    counter = 0

def worker(driver): # FRIENDS PARSING FUNC
    open('SECOND_STEP_PAGE_PARSING', 'w')
    open('SECOND_STEP_FRIEND_PARSING', 'w')
    base = raw_input('\n\tPLEASE GIMME FILE -> ')
    with open(base, "r") as backfile:
        lines = backfile.readlines() 
    for i in range(len(lines)):
        driver.get(lines[i])
        open('SECOND_STEP_PAGE_PARSING', 'a+').write('\n')
        # ----------------------------------------------------Link page parsing-------------------------
        driver.get(lines[i].split('\t')[0])
        time.sleep(0.1)
        page = []
        page.append(driver.page_source.split('"'))
        i = 0
        for i in range(len(page[0])):
            if 'page_name' in page[0][i] and '</h1>' in page[0][i+1]:
                open('SECOND_STEP_PAGE_PARSING', 'a+').write(lines[i] + '\t| ')
                open('SECOND_STEP_PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '') + '\t| ')
                print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
            if '/search?c[section]=people&c[bday]' in page[0][i]:
                open('SECOND_STEP_PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').replace('\n', '').replace('\t', '').replace('<div class=', '').replace('</div>', '').split('>')[1].split('<')[0] + '\t| ')
                print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
            if '/search?c[section]=people&amp;c[byear]' in page[0][i]:
                open('SECOND_STEP_PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').replace('\n', '').replace('\t', '').replace('<div class=', '').replace('</div>', '').split('>')[1].split('<')[0] + '\t| ')
                print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
            if '/search?c[name]=' in page[0][i]:
                open('SECOND_STEP_PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').replace('\n', '').replace('\t', '').replace('<div class=', '').replace('</div>', '').split('>')[1].split('<')[0] + '\t| ')
                print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
            if '/write' in page[0][i] and 'onclick=' in page[0][i+1] and 'href=' in page[0][i-1]:
                page_id = page[0][i]
                print page_id
        print '--------------------------------FRIENDS PARSING---------------------------------------'
        print 'Next step - https://vk.com/friends?id=' + str(page_id.replace('/write', '')) + '&section=all'
        driver.get('https://vk.com/friends?id=' + str(page_id.replace('/write', '')) + '&section=all')
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        # ------------------------------Friends parsing-------------------
        page = []
        i = 0
        page.append(driver.page_source.split('"'))
        driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        for i in range(len(page[0])):
            try:
                if 'friends_user_info' in page[0][i]:
                    open('SECOND_STEP_FRIEND_PARSING', 'a+').write('\n')
                    open('SECOND_STEP_FRIEND_PARSING', 'a+').write('https://vk.com' + page[0][i+4].encode('utf-8') + '\t| ' + page[0][i+5].encode('utf-8').split('>')[1].split('<')[0] + '\t | ')
                if 'friends_field' in page[0][i] and '>' in page[0][i+1] and '</div>' in page[0][i+1] and '<div class=' in page[0][i-1]:
                    open('SECOND_STEP_FRIEND_PARSING', 'a+').write(page[0][i+1].encode('utf-8').split('>')[1].split('<')[0] + '\t| ')
            except IndexError:
                pass

def main(driver):
    page = []
    try:
        selection = raw_input("""   \n\n\tLAST SCORE -> """ + str(temp.counter) + """
                                    \n\n\tYOUR CHOOSE
                                    \n\t[1]PARSE SEARCH RESULT
                                    \n\t[2]PARSE FRIENDS (USE AFTER FIRST STEP)
                                    \n\t[3]PARSE FRIENDS MANUAL
                                    \n\t[4]PARSE PAGE INFO
                                    \n\t-> """)
        if selection == '1':
            open('FIRST_STEP_IDS_PLUS_NAMES', 'w')
            temp.counter = 0
            page = []
            page.append(driver.page_source.split('"'))
            for i in range(len(page[0])):
                if 'info' in page[0][i] and '<div class=' in page[0][i-1] and 'labeled name' in page[0][i+2]:
                    # ФИО и ID
                    open('FIRST_STEP_IDS_PLUS_NAMES', 'a+').write('\n')
                    temp.counter += 1
                    open('FIRST_STEP_IDS_PLUS_NAMES', 'a+').write('https://vk.com' + page[0][i+4].encode('utf-8') + '\t| ' + page[0][i+7].encode('utf-8').split('>')[1].split('<')[0] + '\t | ')
                if 'labeled' in page[0][i] and '</div><div class=' in page[0][i-1]:
                    # Город и образовательное учреждение
                    open('FIRST_STEP_IDS_PLUS_NAMES', 'a+').write(page[0][i+1].encode('utf-8').split('>')[1].split('<')[0] + '\t | ')
            main(driver)
        if selection == '2':
            worker(driver)
        if selection == '3':
            open('MANUAL_FRIEND_PARSING', 'w')
            temp.counter = 0
            page = []
            i = 0
            page.append(driver.page_source.split('"'))
            for i in range(len(page[0])):
                try:
                    if 'friends_user_info' in page[0][i]:
                        temp.counter +=1
                        open('SECOND_STEP_FRIEND_PARSING', 'a+').write('\n')
                        open('SECOND_STEP_FRIEND_PARSING', 'a+').write('https://vk.com' + page[0][i+4].encode('utf-8') + '\t| ' + page[0][i+5].encode('utf-8').split('>')[1].split('<')[0] + '\t | ')
                    if 'friends_field' in page[0][i] and '>' in page[0][i+1] and '</div>' in page[0][i+1] and '<div class=' in page[0][i-1]:
                        open('SECOND_STEP_FRIEND_PARSING', 'a+').write(page[0][i+1].encode('utf-8').split('>')[1].split('<')[0] + '\t| ')
                except IndexError:
                    pass
            main(driver)
        if selection == '4':
            open('PAGE_PARSING', 'w+')
            print "----------------------------------------PAGE INFOS------------------------------------"
            page = []
            page.append(driver.page_source.split('"'))
            i = 0
            for i in range(len(page[0])):
                if 'page_name' in page[0][i] and '</h1>' in page[0][i+1]:
                    open('PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '') + '\t| ')
                    print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
                if '/search?c[section]=people&c[bday]' in page[0][i]:
                    open('PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').replace('\n', '').replace('\t', '').replace('<div class=', '').replace('</div>', '').split('>')[1].split('<')[0] + '\t| ')
                    print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
                if '/search?c[section]=people&amp;c[byear]' in page[0][i]:
                    open('PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').replace('\n', '').replace('\t', '').replace('<div class=', '').replace('</div>', '').split('>')[1].split('<')[0] + '\t| ')
                    print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
                if '/search?c[name]=' in page[0][i]:
                    open('PAGE_PARSING', 'a+').write(page[0][i+1].encode('utf-8').replace('\n', '').replace('\t', '').replace('<div class=', '').replace('</div>', '').split('>')[1].split('<')[0] + '\t| ')
                    print page[0][i+1].encode('utf-8').split('/')[0].replace('<', '').replace('>', '').replace('\n', '').replace('\t', '').replace('<div class=', '')
                if '/write' in page[0][i] and 'onclick=' in page[0][i+1] and 'href=' in page[0][i-1]:
                    page_id = page[0][i]
                    print page_id
            print "----------------------------------------PAGE INFOS END------------------------------------"
        main(driver)
    except IndexError:
        pass
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    chrome_path = 'chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://vk.com/')
    main(driver)