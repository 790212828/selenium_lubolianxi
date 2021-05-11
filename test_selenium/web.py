from time import sleep

from selenium import webdriver

if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get("http://www.baidu.com")
    sleep(10)
    driver.quit()