#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 
driver = webdriver.Chrome()
driver.get('https://vk.com/')

base = raw_input('\n\tPLEASE GIMME FILE -> ')
with open(base, "r") as backfile:
    lines = backfile.readlines() 
    print lines[1]
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