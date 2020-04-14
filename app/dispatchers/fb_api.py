import requests
import json


URL = 'https://graph.facebook.com/v6.0/'


def post(token, gid, message):
    body = {
        'message': message,
        'access_token': token
    }
    req = requests.post(URL + gid + '/feed', params=body)
    res = json.loads(req.text)
    try:
        return 'Success! New post id - ' + str(res['id'])
    except KeyError:
        return res['error']['message']
