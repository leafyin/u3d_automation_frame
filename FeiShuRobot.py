# -*- encoding=utf8 -*-

import json
import time
import hmac
import hashlib
import base64
import urllib.parse

import requests

# 测试
access_token = "64c8ab6c-8fa3-41ce-8264-139f34c31c64"
secret = "d2dgKoiNAz0OJhxxzGsMAg"

# 生成sign
timestamp = str(round(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret).encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

# 消息类型
# 纯文本
text = {
    "timestamp": timestamp,
    "sign": sign,
    "msg_type": "text",
    "content": {
        "text": "这是一条纯文本消息"
    }
}

# 富文本
post = {
    "timestamp": timestamp,
    "sign": sign,
    "msg_type": "post",
    "content": {
        "post": {
            "zh_cn": {
                "title": "富文本消息",
                "content": [
                    [
                        {
                            "tag": "text",
                            "text": "描述"
                        },
                        {
                            "tag": "a",
                            "text": "百度一下",
                            "href": "http://www.baidu.com/"
                        },
                    ]
                ]
            }
        }
    }
}

# 卡片消息
card = {
    "timestamp": timestamp,
    "sign": sign,
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True,
            "enable_forward": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": "今日推荐"
            }
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "content": "**baidu**，是一个网站",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {
                            "content": "百度",
                            "tag": "lark_md"
                        },
                        "url": "https://www.baidu.com",
                        "type": "default",
                        "value": {}
                    }
                ]
            }
        ]
    }
}


def send_msg():
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{access_token}"
    payload = json.dumps(card)
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    print(data)


if __name__ == '__main__':
    send_msg()
