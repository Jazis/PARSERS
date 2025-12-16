from selenium import webdriver
import time

def parse(driver):
    count = 0
    email = []
    emails = []
    try:
        while True:
            try:
                page = []
                page.append(driver.page_source.split(' '))
                for i in range(len(page[0])):
                    try:
                        if '@' in page[0][i] and '.' in page[0][i]:
                            if page[0][i].encode('utf-8') in emails:
                                pass
                            else:
                                count += 1
                                emails.append(page[0][i].encode('utf-8'))
                                open('emails.txt', 'a+').write(page[0][i].encode('utf-8')+'\n')
                    except IndexError:
                        continue
                page = []
                print "emails - " + str(count)
            except KeyboardInterrupt:
                try:
                    def selection():
                        print "Waiting"
                        selection = raw_input("Ready? |no|exit|")
                        if selection == 'exit':
                            exit()
                        else:
                            pass
                    selection() 
                except KeyboardInterrupt:
                    main(driver)
    except KeyboardInterrupt:
        try:
            print "Waiting"
            extraction()
        except KeyboardInterrupt:
            main(driver)


def main(driver):
    raw_input('Press ENTER when yu ar ready')
    parse(driver)

if __name__ == '__main__':
    open('emails.txt', 'w+')
    open('extracted.txt', 'w+')
    chrome_path = 'chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    main(driver)
