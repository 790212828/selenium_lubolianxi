…or create a new repository on the command line
echo "# pytest_practices1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/790212828/pytest_practices1.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/790212828/pytest_practices1.git
git branch -M main
git push -u origin main



"""
生成allure-report命令：
cmd:cd .py文件路径下
pytest --clean --alluredir=./result/2/ test_homework.py
allure generate ./result/2/ -o ./report/2/
allure open -h 127.0.0.1 -p 8090 ./report/2/
"""

"""
1、selenium基础学习知识，元素定位
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.quit()
2、复用当前浏览器
#复用浏览器之前,cmd终端的命令行输入chrome --remote-debugging-port=9222，开启指定地址服务
option=Options()
option.debugger_address="127.0.0.1:9222"
self.driver = webdriver.Chrome(options=option)

3、get_attribute()获取定位元素的属性下的值，即class="aa",获取到"aa"
self.driver.find_element(By.LINK_TEXT,"所有分类")get_attribute("class")

4、获取登录缓存信息==cookies
cookies=self.driver.get_cookies()
print(cookies)

5、shelve用法， 
shelve python 内置的模块，相当于小型数据库
导入cookie到shelve数据库里
实现 cookie 数据的持久化存储

将cookie json数据存储成shelve数据库
def shelve_load_cookies(self,cookies):
    #输入cookies字典数据，把cookies数据存入shelve 类型 的小型数据库中
    db=shelve.open("./mydbs/cookies")
    db["cookie"]=cookies
    db.close()
    
7、将cookie 数据加载使用
    def import_cookies(self):
        db=shelve.open("目录")
        cookies=db['cookie']
        self.driver.get("url")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("url地址")
        sleep(3)
        
8、CSS_SELECTOR元素定位方法学习
https://www.w3school.com.cn/cssref/css_selectors.asp
chrome浏览器打开F12，定位查看元素的class、id等属性值
"F12，打开console控制台，输入$('.class属性值')或者$('#id属性值')
回车检查是否能定义的到元素"



"""