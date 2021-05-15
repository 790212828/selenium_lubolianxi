import time

from selenium import webdriver


class BasePage:

    """
    封装页面通用方法，比如driver的实例化操作
    """
    def __init__(self,base_driver=None):
        """

        :param base_driver: 传入driver实例对象
        """
        #如果base_driver 是初始值None，那么就会实例化driver
        if base_driver is not None:
            self.driver=base_driver
        else:
            # 使用浏览器复用模式，cmd输入Chrome --remote-debugging-port=9222
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = "127.0.0.1:9222"
            # 实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，会在每次find操作的时候轮循查找该元素，超时报错
            self.driver.implicitly_wait(5)
            time.sleep(1)

    def find(self,locator):
        #解元组的操作，把元素定位方法封装成一个方法
        return  self.driver.find_element(*locator)

    def finds(self,locator):
    # 解元组的操作，把元素定位方法封装成一个方法
        return  self.driver.find_elements(*locator)

    def assert_in_like(self,result,a):
        """
        断言功能 判断预期结果是否在实际结果的列表中
        :param result: 确定的结果
        :param a: 导入判断的变量结果
        :return:
        """
        assert result in a

    def assert_not_in_like(self,resualt,a):
        """
        断言功能 判断预期结果是否 不在 实际结果的列表中
        :param resualt: 预期结果
        :param a: 实际结果
        :return:
        """
        assert resualt not in a


    def demo(self):
        """
        解元组展示
        :return:
        """
        a=(1,2)
        self.demo2(*a)#demo2(1,2)

    def demo2(self,a,b):
        print()
