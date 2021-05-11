import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeiXinWork:
    def getcookies(self):
        #获取当前页面的cookies
        cookies=self.driver.get_cookies()
        print(cookies)
        return cookies
    def shelve_load_cookies(self,cookies):
        #输入cookies字典数据，把cookies数据存入shelve 类型 的小型数据库中
        db=shelve.open("./mydbs/cookies")
        db["cookie"]=cookies
        db.close()
    def import_cookies(self):
        db=shelve.open("./mydbs/cookies")
        cookies=db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def setup_class(self):
        print("setup----------class")
        #复用浏览器,命令行输入chrome --remote-debugging-port=9222
        #获取复用浏览器里面 已登录企业微信的 cookies 信息
        option=Options()
        option.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=option)
        cookies = self.driver.get_cookies()
        print(cookies)
        db = shelve.open("./mydbs/cookies")
        db["cookie"] = cookies
        db.close()
        # db = shelve.open("./mydbs/cookies")
        # cookies = db['cookie']
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # for cookie in cookies:
        #     if "expiry" in cookie.keys():
        #         cookie.pop("expiry")
        #     self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(10)


    def setup_method(self):
        #每个测试都重新打开一个
        print("setup-------method")
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        print("teardown_-------method")
        sleep(3)
        print("sleep 10s")
        self.driver.quit()
    def teardown_class(self):
        sleep(10)
        print("sleep 10s")
        # self.driver.quit()

    # @pytest.fixture()
    def test_getcookie(self):
        print("test_getcookie")
        self.import_cookies()

    def test_login(self):
        self.test_getcookie()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
        company_name = self.driver.find_element(By.CSS_SELECTOR, "a.index_info_name").text
        print("company_name:", company_name)
        assert "测试公司-c" == company_name
        sleep(5)
    def test_goto_importcontact(self):
        self.test_login()
        self.driver.implicitly_wait(5)
        import_ele = self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")
        import_ele.click()
        self.driver.implicitly_wait(5)
        contact_ele = self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts")
        print("contact_ele通讯录get_attribute-class:", contact_ele.get_attribute("class"))
        # frame_nav_item frame_nav_item_Curr
        contact_assert = "frame_nav_item frame_nav_item_Curr"
        assert contact_assert == contact_ele.get_attribute("class")

    def test_importcontact(self):
        self.test_goto_importcontact()
        self.driver.implicitly_wait(5)
        post_ele = self.driver.find_element(By.ID, "js_upload_file_input")
        post_ele.send_keys(r"F:\study\selenium_lubolianxi2\mydata.xlsx")
        self.driver.implicitly_wait(5)
        upload_name = self.driver.find_element(By.ID, "upload_file_name").text
        assert_name = "mydata.xlsx"
        print("upload type:", type(upload_name))
        print("assert_name type:", type(assert_name))
        assert assert_name == upload_name
    def test_upload_importcontactfile(self):
        self.test_importcontact()
        self.driver.implicitly_wait(5)
        upload_btn = self.driver.find_element(By.ID, "submit_csv")
        upload_btn.click()
        self.driver.implicitly_wait(5)
        upload_success = self.driver.find_element(By.CSS_SELECTOR, "#reloadContact").text
        print(f"upload_success:{upload_success},type:{type(upload_success)}")
        assert_success = "前往查看"
        assert assert_success == upload_success













