#   账户可以正常使用充值提现
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

def test_sign(pub_data):
    pub_data['username'] = '自动生成 字符串 2,4 数字 shhgfg'
    pub_data['phone'] = '自动生成 手机号'
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
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
# json path，参数类型为列表 根据jsonpath提取响应正文中的数据



def test_chongzhi_1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "充值_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "changeMoney": 10000000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_chaxunzhanghu_1(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    accountName = {"accountName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=accountName,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_koukuan_1(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '扣款'  # allure报告中二级分类
    title = "扣款_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "changeMoney": 10000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_zhanghuliushui(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '查询单个用户账户流水'  # allure报告中二级分类
    title = "查询单个用户账户流水_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getBills"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    accountName = {"accountName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码acc/accLock
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=accountName,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


def test_tixian_1(pub_data):
    pub_data['cardNo'] = '自动生成 字符串 10 数字 62'
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "提现_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "cardNo": "${cardNo}",
  "changeMoney": 10000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_chaxunzhanghu_2(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/getAccInfo"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    accountName = {"accountName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码acc/accLock
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=accountName,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_dongjie(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '冻结用户'  # allure报告中二级分类
    title = "冻结用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accLock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"accountName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_chongzhi_2(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '冻结充值'  # allure报告中二级分类
    title = "冻结充值_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "changeMoney": 10000000
}
    '''
    status_code = 200  # 响应状态码
    expect = "9999"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_koukuan_2(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '冻结扣款'  # allure报告中二级分类
    title = "冻结扣款_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/charge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "changeMoney": 10000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


def test_jiedong(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '解冻用户'  # allure报告中二级分类
    title = "解冻用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/accUnLock"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"accountName":'${username}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

def test_chongzhi_3(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "充值_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "changeMoney": 10000000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)

def test_tixian(pub_data):
    pub_data['cardNo'] = '自动生成 字符串 10 数字 62'
    method = "POST"  #请求方法，全部大写
    feature = "用户模块-正常使用充值提现"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "提现_全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${username}",
  "cardNo": "${cardNo}",
  "changeMoney": 10000
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)