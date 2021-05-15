import pytest

from test_selenium2.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        #实例化MainPage ,为了从主页开始进行操作
        self.main = MainPage()

    @pytest.mark.parametrize("name",["皮城女警"])
    def test_add_member(self,name):
        """
        用来测试添加成员功能
        :return:
        """
        # self.main=MainPage(),优化放在setup_class里面，只执行一次
        """
        1、goto_add_member：跳转到添加成员页面
        2、add_member：添加成员操作，点击保存
        3、get_list：=检查是否成功添加人员==获取成员列表，做断言验证
        """
        res=self.main.goto_add_member().add_member(name).get_list()
        assert name in res

    @pytest.mark.parametrize("name,member_id,member_phone",["测试人2","211333","13611112221"])
    def test_add_memeber_fail(self,name,member_id,member_phone):
        """
        用来测试添加已存在的成员的功能
        :param name:
        :return:
        """
        res=self.main.goto_add_member().add_member_fail(name,member_id,member_phone).get_list()
        #断言
        self.main.assert_not_in_like(name,res)

    @pytest.mark.parametrize("name,member_id,member_phone", [["测试人3","111333","13611112222"]])
    def test_add_member_2(self,name,member_id,member_phone):
        """
        用来测试在通讯录页面进行添加成员的功能
        :param name: 参数化 添加成员的名称
        :param member_id: 参数化 添加成员的账号id
        :param member_phone: 参数化 添加成员的手机号码
        :return:
        """
        res=self.main.goto_contact().goto_add_member().add_member_2(name,member_id,member_phone).get_list()
        # 断言
        self.main.assert_in_like(name,res)

    @pytest.mark.parametrize('depart_name',["113"])
    def test_add_department(self,depart_name):
        """
        测试在通行录页面进行添加部门的操作功能
        :param depart_name: 参数化 添加部门的名称
        :return:
        """
        res=self.main.goto_contact().goto_add_department().add_department(depart_name).get_depart_list()
        self.main.assert_in_like(depart_name,res)


