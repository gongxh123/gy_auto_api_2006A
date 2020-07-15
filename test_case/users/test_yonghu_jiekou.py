import pytest

from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
@pytest.mark.xiugai
#   修改密码验证
def test_denglu_sign(pub_data):
    pub_data['username'] = '自动生成 字符串 2,4 数字 shhgfg'
    pub_data['phone'] = '自动生成 手机号'
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-登录"  # allure报告中一级分类
    story = '用户注册登录'  # allure报告中二级分类
    title = "用户注册登录_全字段正常流_1"  # allure报告中用例名字
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
    # json_path = [{"cstId": '$.data.cstId'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_changepwd_changepwd(pub_data):
    header = {"token":pub_data["token"]}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-登录"  # allure报告中一级分类
    story = '修改密码'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/user/changepwd"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "newPwd": "a1234567",
  "oldPwd": "a123456",
  "reNewPwd": "a1234567",
  "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)

@pytest.mark.xiugai
def test_changepwd_yanzheng(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-登录"  # allure报告中一级分类
    story = '登录验证'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "a1234567",
  "userName": "${username}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)






