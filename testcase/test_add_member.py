import pytest

from test_selenium2.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
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

    @pytest.mark.parametrize("name",["女警2"])
    def test_add_memeber_fail(self,name):
        res=self.main.goto_add_member().add_member_fail(name).get_list()

    @pytest.mark.parametrize("name,member_id,member_phone", [["女警3","111333","13611112222"]])
    def test_add_member_2(self,name,member_id,member_phone):
        """
        用来测试通讯录页面添加成员功能
        :return:
        """
        res=self.main.goto_contact().goto_add_member().add_member_2(name,member_id,member_phone).get_list()
        assert name in res

    @pytest.mark.parametrize('depart_name',["113"])
    def test_add_department(self,depart_name):
        # res = self.main.goto_add_member().add_member(name).get_list()
        # res=self.main.goto_contact().goto_add_department().add_department().get_depart_list()
        res=self.main.goto_contact().goto_add_department().add_department(depart_name).get_depart_list()
        assert depart_name in res


