# -*- encoding=utf8 -*-

import json
import sys
import time
import hmac
import hashlib
import base64
import urllib.parse

import requests

# 测试
# access_token = "c813cb19aaae8ca0906d6c68777b2a4679b51f4ad3b80b7cec66c7ba88ed4459"
# secret_ = "SEC1ad5cffbaf336eb01105801d5e0061d934f3a6bc47ca7ed1addaa9d16289bfd2"

# 2楼群
access_token = "410c22d5d964222d1fa974c174c6af81806f271df33a2fc92e5cf050564e6fc5"
secret_ = "SEC172a09ac28192634085968c4e6095263e793bb9e6a68d9915413ffd2a440f97b"


def get_sign():
    timestamp = str(round(time.time() * 1000))
    secret = secret_
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return sign


def send_msg(msg):
    timestamp = str(round(time.time() * 1000))
    url = "https://oapi.dingtalk.com/robot/send?" \
          f"access_token={access_token}" \
          f"&timestamp={timestamp}" \
          f"&sign={get_sign()}"
    payload = json.dumps({
        "msgtype": "text",
        "text": {
            "content": msg
        }
    })
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    print(data)


if __name__ == '__main__':
    send_msg(sys.argv[1])
