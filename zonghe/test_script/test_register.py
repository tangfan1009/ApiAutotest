'''
注册的测试脚本
'''

#  注册失败的测试脚本
import pytest
from zonghe.baw import Member, Db
from zonghe.caw import DataRead, Asserts


# pytest 数据驱动的方式
# 从yaml中读取测试数据源


@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param


def test_register_fail(url, baserequests, fail_data):
    # 下发注册的请求
    r = Member.register(url, baserequests, fail_data["data"])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # assert r.json()['status'] == fail_data['expect']['status']
    Asserts.check(r.json(), fail_data['expect'], "code,msg,status")

# 把注册成功的数据写到register_pass.yaml
# 注册成功的脚本，下发请求，断言响应的结果

@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def success_data(request):
    return request.param


def test_register_pass(url, baserequests, success_data, db):
    # 下发注册的请求
    mobilephone = str(success_data['data']['mobilephone'])
    # 初始化环境：删除注册的用户（数据库中可能有其他人测试的数据，与本用例冲突）
    Db.delete_user(db, mobilephone)
    r = Member.register(url, baserequests, success_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == success_data['expect1']['code']
    # assert r.json()['msg'] == success_data['expect1']['msg']
    # assert r.json()['status'] == success_data['expect1']['status']
    Asserts.check(r.json(), success_data['expect1'], "code,msg,status")

    #  调用查询的接口，在查询的结果中能找到本次注册的手机号
    h = Member.list(url, baserequests)
    assert mobilephone in h.text
    # 重复注册
    r = Member.register(url, baserequests, success_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == success_data['expect2']['code']
    # assert r.json()['msg'] == success_data['expect2']['msg']
    # assert r.json()['status'] == success_data['expect2']['status']
    Asserts.check(r.json(), success_data['expect2'], "code,msg,status")
    # 清理环境：删除注册的用户（在数据库中添加的数据，测试完成后清理掉）
    Db.delete_user(db, mobilephone)
