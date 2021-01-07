'''
fixture 带参数
'''
import pytest

url = "http://jy001:8081/futureloan/mvc/api/member/register"


# 登录功能的测试数据
@pytest.fixture(params=[{"mobilephone": 15006008111, "pwd": "","regname":""},
                        {"mobilephone": "", "pwd": 85846215,"regname":""},
                        {"mobilephone": "", "pwd": "","regname":""},
                        {"mobilephone": 18006007167, "pwd": "","regname":"丫丫"},
                        {"mobilephone": "", "pwd": "aaa58585","regname":"wawa"},
                        {"mobilephone": 15060715011, "pwd": "aaa55"},
                        {"mobilephone": 15060715012, "pwd": "abc"},
                        {"mobilephone": 15060715012, "pwd": "aaaaaa1952154126415"},
                        {"mobilephone": 1, "pwd": "abc1234"},
                        {"mobilephone": 136485, "pwd": "abc1234"},
                        {"mobilephone": 1234567890, "pwd": "abc1234"},
                        {"mobilephone": 12345678941012, "pwd": "abc1234"},
                        {"mobilephone": 11111111111, "pwd": "abc1234"},
                        {"mobilephone": 15006007018, "pwd": "abc1234"}])

def login_data(request):   # request 是pytest中的关键字，固定写法
    return request.param   # 通过request.param返回每一组数据，固定写法

# 登录功能的测试脚本
def test_login(login_data):
    # f 类似于格式化输出
    print(f"登录功能，测试数据为:{login_data}")
    print(f"手机号：{login_data['mobilephone']}")
    print(f"密码：{login_data['pwd']}")
