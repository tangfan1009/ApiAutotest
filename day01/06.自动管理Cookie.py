'''
自动管理Cookie
requests中的Session类，能给自动获取和管理Cookie
'''

import requests

# 新建一个session
s = requests.session()

# 登录接口 login
loginData = {"access_type": "1", "loginType": "1",
             "emailLoginWay": "0",
             "account": "2780487875@qq.com",
             "password": "qq2780487875",
             "remindmeBox": "on", "remindme": "1"}
r = s.post("https://www.bagevent.com/user/login", data=loginData)
print(r.text)
print("登录之后的Cookie：", s.cookies)
# dashboard 接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)

# 退出登录 Logout
r = s.get("https://www.bagevent.com/user/login_out")
# print(r.text)
print("退出登录之后的Cookie：", s.cookies)
# RequestsCookieJar 转成字典
d = requests.utils.dict_from_cookiejar(s.cookies)
print(d)
