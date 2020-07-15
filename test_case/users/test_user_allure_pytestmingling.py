import random

import allure
import requests

from config.conf import API_URL
from test_case.conftest import pub_data

@allure.feature("用户模块")
@allure.story("充值提现模块")
@allure.title("扣款余额不足验证")
def test_chongzhi_1(db):
    with allure.step("第一步，执行sql语句"):
        res = db.select_execute("select `account_name` from `t_cst_account` where status = 0 and account_name is not null;")
    with allure.step("第二步，从查询结果随机抽取一条数据"):
        account_name = random.choice(res)[0]
    with allure.step("第三步，准备请求数据"):
        data ={
      "accountName": account_name,
      "changeMoney": 10000
    }
    with allure.step("第四步，发送请求"):
        r = requests.post(API_URL+"/acc/recharge",json=data)
    with allure.step("第五步，获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url, "请求地址", allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers), "请求头", allure.attachment_type.TEXT)
        allure.attach(r.request.body, "请求正文", allure.attachment_type.TEXT)
        # print(r.request.url)
        # print(r.request.body)
    with allure.step("第六步，获取响应内容"):
        allure.attach(str(r.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(r.headers), "响应头", allure.attachment_type.TEXT)
        allure.attach(r.text, "响应正文", allure.attachment_type.TEXT)
        # print(r.text)
    with allure.step("第七步，断言"):
        allure.attach(r.text, "实际结果", allure.attachment_type.TEXT)
        allure.attach("充值成功", "预期结果", allure.attachment_type.TEXT)
        # assert "充值成功" in r.text


#  pytest test_case/users/test_user_allure_pytestmingling.py --alluredir=reports/xml   #  pytest allure  命令创建reports/xml
#  allure generate reports/xml -o reports/html   #  pytest allure  命令创建reports/html