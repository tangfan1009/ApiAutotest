import requests

# 验证用户使用合法的手机号、密码，昵称为空，注册成功
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15006007018, "pwd": "123456", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '10001'
assert r.json()['status'] == 1

# 验证用户使用合法的手机号、密码、昵称，注册成功
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15006007018, "pwd": "123456", "regname": "haha"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '10001'
assert r.json()['status'] == 1

# 验证用户使用合法的手机号码，昵称、密码为空，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15006008111, "pwd": "", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20103'
assert r.json()['status'] == 0

# 验证用户手机号码、昵称为空，密码合法，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": "", "pwd": "85846215", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20103'
assert r.json()['status'] == 0

# 验证用户手机号码、密码、昵称为空，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": "", "pwd": "", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20103'
assert r.json()['status'] == 0

# 验证用户使用合法的手机号码、昵称，密码为空，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 18006007167, "pwd": "", "regname": "丫丫"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20103'
assert r.json()['status'] == 0

# 验证用户手机号码为空，密码、昵称合法，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": "", "pwd": "aaa58585", "regname": "wawa"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20103'
assert r.json()['status'] == 0

# 验证用户使用合法的手机号码，密码输入5位，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15060715011, "pwd": "aaa55"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20108'
assert r.json()['status'] == 0

# 验证用户使用合法的手机号码，密码输入3位，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15060715012, "pwd": "abc"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20108'
assert r.json()['status'] == 0

# 验证用户使用合法的手机号码，密码输入19位，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15060715012, "pwd": "aaaaaa1952154126415"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20108'
assert r.json()['status'] == 0

# 验证用户使用长度为1的手机号码，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 1, "pwd": "abc1234"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20109'
assert r.json()['status'] == 0

# 验证用户使用长度为6的手机号码，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 136485, "pwd": "abc1234"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20109'
assert r.json()['status'] == 0

# 验证用户使用长度为10的手机号码，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 1234567890, "pwd": "abc1234"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20109'
assert r.json()['status'] == 0

# 验证用户使用长度为12的手机号码，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 12345678941012, "pwd": "abc1234"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20109'
assert r.json()['status'] == 0

# 验证用户使用长度为11的不合法手机号码，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 11111111111, "pwd": "abc1234"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20109'
assert r.json()['status'] == 0

# 验证用户使用已注册的手机号码，注册失败
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": 15006007018, "pwd": "abc1234"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['code'] == '20110'
assert r.json()['status'] == 0
