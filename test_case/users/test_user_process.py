import pytest

from tools.api import request_tool
from tools.data import excel_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''

data = excel_tool.get_test_case("test_case/users/充值测试(1).xls")

@pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])
def test_sign(pub_data,account_name,money,expect):
    pub_data[account_name] = account_name
    pub_data[money] = money
    pub_data[expect] = expect
    # pub_data['username'] = '自动生成 字符串 2,4 数字 shhgfg'
    # pub_data['phone'] = '自动生成 手机号'
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "phone": "${phone}",
  "pwd": "a123456",
  "rePwd": "a123456",
  "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"cstId": '$.data.cstId'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,json_path=json_path)


def test_cst_realname(pub_data):
    header = {"token":pub_data["token"]}
    pub_data["certno"] = '自动生成 身份证号'
    pub_data["cstName"] = '自动生成 姓名'
    pub_data["email"] = '自动生成 邮箱'
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '实名认证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/realname2"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''{
  "cstId": "${cstId}",
  "customerInfo": {
    "birthday": "2020-01-01",
    "certno": "${certno}",
    "city": "上海市区",
    "cstName": "${cstName}",
    "email": "${email}",
    "province": "上海市",
    "sex": 1
  }
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)
