import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeXin:
    def setup_method(self):
        # option=Options()
        # option.debugger_address="127.0.0.1:9222"
        # self.driver=webdriver.Chrome(options=option)
        # 复用浏览器,命令行输入chrome --remote-debugging-port=9222

        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self):
        # self.driver.quit()
        pass


    def test_cookie0(self):
        #获取当前页面的cookies
        cookies=self.driver.get_cookies()
        print(cookies)


    def test_cookie(self):
        #获取当前页面的cookies
        # cookies=self.driver.get_cookies()
        # print(cookies)

        #打开微信index页面，这个时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(5)

        #带有登录信息的cookie
        cookies_text=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850362227452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'PPRToNWlsYj9mNQ2JvhFGR_Luc_0dmQmYRQeBBG_shj_e_skYryPcFUwgsUryGDl9p-6txdb87g29RV4IagCKzHc62cKWkr0Pl-7ySSUBbrnsClyelmjKmRs2UCcwZKGLBHyBoDmToyIFtpMRV04dinpvEU2PUmyN0vbPKJ5cAMRy9Zcz63zN86hI4tBZzCuBtWkQmPp_DIE3EHL9oGWWqmSjL70M5CfuO-IGupi7d0EGeBCO9ON1gBOGvtFrMPwJYGunt0BbfWVlK7dTsrJOw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850362227452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325055449531'}, {'domain': '.work.weixin.qq.com', 'expiry': 1652178223, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1620633689,1620642217'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1936125'}, {'domain': '.qq.com', 'expiry': 1620782428, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.896913972.1620633689'}, {'domain': 'work.weixin.qq.com', 'expiry': 1620727531, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '81fjrgo'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '26700707111196597'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'HHdtGSJEOiBkggj3kgd6IwAnNm68SvkPJzegZ6mkiKQqwFLj3msUYwdlty2460O6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1623288031, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'expiry': 1652178215, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1683768028, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1077972571.1616049202'}]

        for cookie in cookies_text:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 再次进入企业微信登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(10)

    def test_importcontact(self):
        # 打开微信index页面，这个时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # sleep(5)
        # 带有登录信息的cookie
        cookies_text = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850362227452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'PPRToNWlsYj9mNQ2JvhFGR_Luc_0dmQmYRQeBBG_shj_e_skYryPcFUwgsUryGDl9p-6txdb87g29RV4IagCKzHc62cKWkr0Pl-7ySSUBbrnsClyelmjKmRs2UCcwZKGLBHyBoDmToyIFtpMRV04dinpvEU2PUmyN0vbPKJ5cAMRy9Zcz63zN86hI4tBZzCuBtWkQmPp_DIE3EHL9oGWWqmSjL70M5CfuO-IGupi7d0EGeBCO9ON1gBOGvtFrMPwJYGunt0BbfWVlK7dTsrJOw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850362227452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325055449531'}, {'domain': '.work.weixin.qq.com', 'expiry': 1652178223, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1620633689,1620642217'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1936125'}, {'domain': '.qq.com', 'expiry': 1620782428, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.896913972.1620633689'}, {'domain': 'work.weixin.qq.com', 'expiry': 1620727531, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '81fjrgo'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '26700707111196597'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'HHdtGSJEOiBkggj3kgd6IwAnNm68SvkPJzegZ6mkiKQqwFLj3msUYwdlty2460O6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1623288031, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'expiry': 1652178215, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1683768028, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1077972571.1616049202'}]

        for cookie in cookies_text:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 再次进入企业微信登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
        # sleep(5)
        import_ele=self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)")
        import_ele.click()
        # sleep(5)
        self.driver.implicitly_wait(5)
        post_ele=self.driver.find_element(By.ID,"js_upload_file_input")
        post_ele.send_keys(r"F:\study\selenium_lubolianxi2\mydata.xlsx")
        self.driver.implicitly_wait(5)
        upload_name=self.driver.find_element(By.ID,"upload_file_name").text
        assert_name="mydata.xlsx"
        print("upload type:",type(upload_name))
        print("assert_name type:",type(assert_name))
        assert assert_name==upload_name

        sleep(5)

    def test_shelve_load(self):
        #shelve python 内置的模块，相当于小型数据库
        #导入cookie到shelve数据库里
        #实现 cookie 数据的持久化存储

        # 带有登录信息的cookie
        cookies_text = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850362227452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'PPRToNWlsYj9mNQ2JvhFGR_Luc_0dmQmYRQeBBG_shj_e_skYryPcFUwgsUryGDl9p-6txdb87g29RV4IagCKzHc62cKWkr0Pl-7ySSUBbrnsClyelmjKmRs2UCcwZKGLBHyBoDmToyIFtpMRV04dinpvEU2PUmyN0vbPKJ5cAMRy9Zcz63zN86hI4tBZzCuBtWkQmPp_DIE3EHL9oGWWqmSjL70M5CfuO-IGupi7d0EGeBCO9ON1gBOGvtFrMPwJYGunt0BbfWVlK7dTsrJOw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850362227452'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325055449531'}, {'domain': '.work.weixin.qq.com', 'expiry': 1652178223, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1620633689,1620642217'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1936125'}, {'domain': '.qq.com', 'expiry': 1620782428, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.896913972.1620633689'}, {'domain': 'work.weixin.qq.com', 'expiry': 1620727531, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '81fjrgo'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '26700707111196597'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'HHdtGSJEOiBkggj3kgd6IwAnNm68SvkPJzegZ6mkiKQqwFLj3msUYwdlty2460O6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1623288031, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'expiry': 1652178215, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1683768028, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1077972571.1616049202'}]

        db=shelve.open('./mydbs/cookies')
        db['cookie']=cookies_text
        db.close()

    def test_shelve(self):
        # shelve python 内置的模块，相当于小型数据库
        #使用shelve数据库，拿出数据信息
        db=shelve.open('./mydbs/cookies')
        print(db['cookie'])
        cookies=db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 再次进入企业微信-首页页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
        import_ele=self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)")
        import_ele.click()
        self.driver.implicitly_wait(5)
        contact_ele=self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts")
        print("contact_ele通讯录get_attribute-class:",contact_ele.get_attribute("class"))
        #frame_nav_item frame_nav_item_Curr
        contact_assert="frame_nav_item frame_nav_item_Curr"
        assert contact_assert==contact_ele.get_attribute("class")
        self.driver.implicitly_wait(5)
        post_ele=self.driver.find_element(By.ID,"js_upload_file_input")
        post_ele.send_keys(r"F:\study\selenium_lubolianxi2\mydata.xlsx")
        self.driver.implicitly_wait(5)
        upload_name=self.driver.find_element(By.ID,"upload_file_name").text
        assert_name="mydata.xlsx"
        print("upload type:",type(upload_name))
        print("assert_name type:",type(assert_name))
        assert assert_name==upload_name
        self.driver.implicitly_wait(5)
        upload_btn=self.driver.find_element(By.ID,"submit_csv")
        upload_btn.click()
        self.driver.implicitly_wait(5)
        upload_success=self.driver.find_element(By.CSS_SELECTOR,"#reloadContact").text
        print(f"upload_success:{upload_success},type:{type(upload_success)}")
        assert_success="前往查看"
        assert assert_success==upload_success

    @pytest.fixture()
    @pytest.mark.dependency()
    # @pytest.mark.xfail(reason='deliberate fail')
    def test_cookies(self):
        db=shelve.open("./mydbs/cookies")
        cookies=db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

    @pytest.fixture(scope="session")
    @pytest.mark.dependency(depends=['test_cookies'])
    def test_login(self,test_cookies):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(5)
        company_name=self.driver.find_element(By.CSS_SELECTOR,"a.index_info_name").text
        print("company_name:",company_name)
        assert "测试公司-c"==company_name
        sleep(5)
        pass

    # @pytest.fixture(scope="session")
    @pytest.mark.dependency(depends=['test_cookies','test_login'])
    def test_importcontact(self,test_cookies,test_login):
        import_ele = self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")
        import_ele.click()
        self.driver.implicitly_wait(5)
        post_ele = self.driver.find_element(By.ID, "js_upload_file_input")
        post_ele.send_keys(r"F:\study\selenium_lubolianxi2\mydata.xlsx")
        self.driver.implicitly_wait(5)
        upload_name = self.driver.find_element(By.ID, "upload_file_name").text
        assert_name = "mydata.xlsx"
        print("upload type:", type(upload_name))
        print("assert_name type:", type(assert_name))
        assert assert_name == upload_name
        pass

    def test_upload(self):
        pass







