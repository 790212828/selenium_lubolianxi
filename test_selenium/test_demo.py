
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        #复用浏览器,命令行输入chrome --remote-debugging-port=9222
        option=Options()
        option.debugger_address="127.0.0.1:9222"
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(options=option)
        # self.driver=webdriver.Firefox(executable_path="E:\driver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo0(self):
        # self.driver.get("https://ceshiren.com/")
        # self.driver.set_window_size(1616, 876)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        categoryle=self.driver.find_element(By.LINK_TEXT,"所有分类")
        print("categoryle:",categoryle.get_attribute("class"))
        assert 'active' == categoryle.get_attribute("class")





