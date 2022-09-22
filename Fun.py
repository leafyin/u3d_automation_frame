# -*- encoding=utf8 -*-

import json

import requests

# 下面是你需要修改的参数
user_id = "200002180"
area_id = "21"
username = "yinye"
cookie = "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22178d4d353beb96-0eba4521051369-3f356b-2073600-178d4d353bf556%22%2C%22%24device_id%22%3A%22178d4d353beb96-0eba4521051369-3f356b-2073600-178d4d353bf556%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D"
num = "10000000"
status = "add"


def items():
    url = "http://test-console.mop.com:8091/managementServer/userManagement/findUserItem"
    payload = '{"userId":"' + user_id + '","areaId":' + area_id + '}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '34',
        'Content-Type': 'application/json',
        'Cookie': cookie,
        'Host': 'test-console.mop.com',
        'Origin': 'http://system.mop.com',
        'Referer': 'http://system.mop.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'token': '123456',
        'username': username
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    data = json.loads(response.text)
    return data["data"]["data"]


def make_account_strong():
    url = "http://test-console.mop.com:8091/managementServer/userManagement/operationUserItem"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '34',
        'Content-Type': 'application/json',
        'Cookie': cookie,
        'Host': 'test-console.mop.com',
        'Origin': 'http://system.mop.com',
        'Referer': 'http://system.mop.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'token': '123456',
        'username': username
    }
    for i in items():
        item_id = i["itemId"]
        payload = '{"userId":"' + user_id + '","item":"' + str(item_id) + '|' + num + '","areaId":' + area_id + ',"operation":"' + status + '"}'
        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        print(result)


make_account_strong()
