'''
fixture 带参数
'''
import pytest
import requests


# 登录功能的测试数据
@pytest.fixture(params=[{"data": {"mobilephone": 15006008111, "pwd": "", "regname": ""},
                         "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
                        {"data": {"mobilephone": "", "pwd": "85846215", "regname": ""},
                         "expect": {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}},
                        {"data": {"mobilephone": "", "pwd": "", "regname": ""},
                         "expect": {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}},
                        {"data": {"mobilephone": 18006007167, "pwd": "", "regname": "丫丫"},
                         "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
                        {"data": {"mobilephone": "", "pwd": "aaa58585", "regname": "wawa"},
                         "expect": {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}},
                        {"data": {"mobilephone": 15060715011, "pwd": "aaa55", "regname": ""},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {"data": {"mobilephone": 15060715012, "pwd": "abc", "regname": ""},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {"data": {"mobilephone": 15060715012, "pwd": "aaaaaa1952154126415", "regname": ""},
                         "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},
                        {"data": {"mobilephone": 1, "pwd": "abc1234", "regname": ""},
                         "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {"data": {"mobilephone": 136485, "pwd": "abc1234", "regname": ""},
                         "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {"data": {"mobilephone": 1234567890, "pwd": "abc1234", "regname": ""},
                         "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {"data": {"mobilephone": 12345678941012, "pwd": "abc1234", "regname": ""},
                         "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {"data": {"mobilephone": 11111111111, "pwd": "abc1234", "regname": ""},
                         "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}},
                        {"data": {"mobilephone": 15006007018, "pwd": "abc1234", "regname": ""},
                         "expect": {"status": 0, "code": "20110", "data": None, "msg": "手机号码已被注册"}}])
def regsiter_data(request):  # request 是pytest中的关键字，固定写法
    return request.param  # 通过request.param返回每一组数据，固定写法


# 注册功能的测试脚本
def test_regsiter(regsiter_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为：{regsiter_data['data']}")
    r = requests.post(url, data=regsiter_data['data'])
    print(r.text)
    assert r.json()['code'] == regsiter_data['expect']['code']
    assert r.json()['status'] == regsiter_data['expect']['status']
    assert r.json()['msg'] == regsiter_data['expect']['msg']
