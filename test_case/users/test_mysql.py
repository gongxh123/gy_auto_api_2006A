import random

from tools.api import request_tool


def test_recharge(pub_data,db):
    res = db.select_execute("select `account_name` from `t_cst_account` where status = 0 and account_name is not null;")
    # pub_data["account_name"] = res[0][0]  #  取固定值
    pub_data["account_name"] = random.choice(res)[0]  #  取随机值
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": 10000
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)