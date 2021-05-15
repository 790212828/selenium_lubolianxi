from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium2.page.add_member_page import AddMemberPage
from test_selenium2.page.base_page import BasePage
from test_selenium2.page.contact_page import ContactPage


class MainPage(BasePage):
    #把元素定位封装成一个元组
    add_member_ele=(By.CSS_SELECTOR,".ww_indexImg_AddMember")
    def goto_add_member(self):
        self.driver.implicitly_wait(5)
        # self.driver.find_element(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()
        # self.find((By.CSS_SELECTOR,".ww_indexImg_AddMember")).click()
        self.find(self.add_member_ele).click()
        return AddMemberPage(self.driver)


    def goto_contact(self):
        self.driver.implicitly_wait(5)
        self.find((By.ID,"menu_contacts")).click()
        return ContactPage(self.driver)








