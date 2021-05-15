from time import sleep

from selenium.webdriver.common.by import By

from test_selenium2.page.base_page import BasePage
from test_selenium2.page.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    #把元素定位封装成一个元组
    input_depart=(By.CSS_SELECTOR,"[name=name]")
    select_eles=(By.CSS_SELECTOR,"span.js_parent_party_name")
    # select_click=(By.XPATH,"//*[@id='1688850362227457_anchor']")
    select_click=(By.CSS_SELECTOR,"div.jstree:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(3)")
    save_click=(By.CSS_SELECTOR,"[d_ck=submit]")

    def add_department(self,depart_name):
        """
        添加部门操作方法
        :param depart_name:
        :return:
        """
        #查找部门名称输入框，并输入113
        sleep(5)
        # self.find(self.input_depart).send_keys("113")
        self.find(self.input_depart).send_keys(depart_name)
        #查找所属部门选择框，并点击
        self.driver.implicitly_wait(5)
        self.find(self.select_eles).click()
        sleep(5)
        #点击选择所属部门列表的选项
        self.driver.implicitly_wait(5)
        self.find(self.select_click).click()
        #点击保存操作
        self.driver.implicitly_wait(5)
        self.find(self.save_click).click()

        return ContactPage(self.driver)

    def goto_contact(self):
        pass
