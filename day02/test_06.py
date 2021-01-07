'''
fixture作用域：类级别的

每个类，首次调用login的地方执行前置，类中用例执行完执行后置
'''

import pytest
@pytest.fixture(scope='class')
def login():
    print("前置：登录系统")
    yield
    print("后置：退出系统")


class TestQuery:
    def test_01(self):
        print("测试用例1")

    def test_02(self, login):   # 执行前置
        print("测试用例2")

    def test_03(self, login):
        print("测试用例3")

    def test_04(self, login):   # 执行后置
        print("测试用例4")


class TestAdd:
    def test_01(self):
        print("测试用例1")

    def test_02(self):
        print("测试用例2")

    def test_03(self, login):  # 执行前置
        print("测试用例3")

    def test_04(self):   # 执行后置
        print("测试用例4")
