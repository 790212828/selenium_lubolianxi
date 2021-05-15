import pytest

from test_selenium2.page.main_page import MainPage


class TestAddMember2:
    def setup_class(self):
        self.main = MainPage()
    def test_add_member_2(self):
        """
        用来测试通讯录页面添加成员功能
        :return:
        """
        # res = self.main.goto_contact().goto_add_member().add_member("女警3").get_list()
        res = self.main.goto_contact().goto_add_member().add_member_2("女警3").get_list()
        assert "女警3" in res