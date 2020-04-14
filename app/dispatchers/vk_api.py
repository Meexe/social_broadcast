import requests
import json


URL = 'https://api.vk.com/method/wall.post'


def post(token, gid, message):
    body = {
        'owner_id': gid,
        'access_token': token,
        'from_group': 1,
        'message': message,
        'v': 5.103
    }
    req = requests.post(URL, params=body)
    res = json.loads(req.text)
    try:
        return res['error']['error_msg']
    except KeyError:
        return 'success'
