from selenium import webdriver
import time

def main():
    open('links.txt', 'w')
    count = 0
    friends_tab =[]
    chrome_path = 'chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://vk.com/')
    while True:
        raw_input("Press ENTER on friends tab page")
        if 'friends_tabs_wrap' in driver.page_source:
            friends_tab.append(driver.page_source.split('"'))
            for i in range(len(friends_tab[0])):
                if 'friends_field friends_field_title' in friends_tab[0][i]:
                    print friends_tab[0][i+5]

if __name__ == '__main__':
    main()