from time import sleep

from selenium.webdriver.common.by import By


from test_selenium2.page.base_page import BasePage


class ContactPage(BasePage):
    # 把元素定位封装成一个元组
    ele_add=(By.CSS_SELECTOR,".js_add_member:nth-child(2)")
    ele_list_locator=(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
    add_icon=(By.CSS_SELECTOR,".js_create_dropdown")
    add_depart=(By.CSS_SELECTOR,"a.js_create_party")
    def goto_add_member(self):
        sleep(5)
        self.driver.implicitly_wait(10)
        # ele_click=self.driver.find_elements(By.CSS_SELECTOR,".js_add_member:nth-child(2)")
        # ele_clicks=self.finds(self.ele_add)
        # print("添加新成员的列表：",ele_clicks[0].text)
        # ele_add=ele_clicks[0]
        # ele_add.click()
        self.finds(self.ele_add)[0].click()
        from test_selenium2.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)


    def get_list(self):
        sleep(5)
        self.driver.implicitly_wait(5)
        #获取通讯录里的全部名称元素
        # ele_list=self.driver.find_elements(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        # name_list=[]
        # for ele in ele_list:
        #     name_list.append(ele.text)
        # print(f"全部名称：{name_list}")
        # namelist = [ele.text for ele in ele_list]

        # ele_list=self.finds(self.ele_list_locator)
        # namelist=[ele.text for ele in ele_list]

        namelist=[ele.text for ele in self.finds(self.ele_list_locator)]
        print("成员名称：",namelist)
        return namelist


    def goto_add_department(self):
        sleep(5)
        self.driver.implicitly_wait(5)
        self.find(self.add_icon).click()
        sleep(3)
        self.find(self.add_depart).click()
        from test_selenium2.page.add_department_page import AddDepartmentPage
        return AddDepartmentPage(self.driver)

    def get_depart_list(self):
        sleep(5)
        self.driver.implicitly_wait(5)
        depart_names=self.finds((By.CSS_SELECTOR,".jstree-anchor"))
        name_list=[i.text for i in depart_names]
        print("部门名称：",name_list)
        return name_list










