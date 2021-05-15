from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium2.page.base_page import BasePage
from test_selenium2.page.contact_page import ContactPage


class AddMemberPage(BasePage):

    # 把元素定位封装成一个元组
    username=(By.ID,"username")
    memberAdd_acctid=(By.ID, "memberAdd_acctid")
    memberAdd_phone=(By.ID, "memberAdd_phone")
    #点击保存元素
    save_member=(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save")

    def add_member(self,name):
        #将重复的初始化操作放在basepage页面
        # # 使用浏览器复用模式，cmd输入Chrome --remote-debugging-port=9222
        # chrome_arg = webdriver.ChromeOptions()
        # # 加入调试地址
        # chrome_arg.debugger_address = "127.0.0.1:9222"
        # # 实例化driver对象
        # self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        self.driver.implicitly_wait(5)


        #添加姓名、账号、手机号
        self.driver.find_element(By.ID,"username").send_keys(name)
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("111")
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("13987654321")



        #点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()

        return ContactPage(self.driver)

    def add_member_fail(self,name,member_id,member_phone):
        self.driver.implicitly_wait(5)
        # 添加姓名、账号、手机号
        self.driver.find_element(By.ID, "username").send_keys(name)
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member_id)
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(member_phone)

        self.driver.implicitly_wait(5)
        # 点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save").click()
        self.driver.implicitly_wait(5)
        # 获取报错信息组
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        err_txt = [ele.text for ele in ele_list]
        print(f"err_txt报错信息组：{err_txt}")

        return ContactPage(self.driver)

    def add_member_2(self,name,memberID,memberPhone):
        """
        :param name: 成员姓名
        :param memberID: 成员的账号id
        :param memberPhone: 成员的手机号码
        :return:
        """
        self.driver.implicitly_wait(5)

        #添加姓名、账号、手机号
        # self.driver.find_element(By.ID,"username").send_keys(name)
        # self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("111333")
        # self.driver.find_element(By.ID,"memberAdd_phone").send_keys("13611112222")
        self.find(self.username).send_keys(name)
        # self.find(self.memberAdd_acctid).send_keys("111333")
        self.find(self.memberAdd_acctid).send_keys(memberID)
        # self.find(self.memberAdd_phone).send_keys("13611112222")
        self.find(self.memberAdd_phone).send_keys(memberPhone)

        #点击保存按钮
        # self.driver.find_element(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()
        self.find(self.save_member).click()

        return ContactPage(self.driver)

    def goto_contact(self):

        pass





