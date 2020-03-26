import requests
import json

def dingTalk(msg):

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": "腾顺--%s"%msg
        },
        "at": {
            "atMobiles": [],
            "isAtAll": "false"
        }
    }

    json_data = json.dumps(data)
    requests.post(
        url='https://oapi.dingtalk.com/robot/send?access_token=0d4a6061efd77b130f6d28d5984ed55a4ac3e7b9357197d32c1001acff7054da',
        data=json_data, headers=headers)
