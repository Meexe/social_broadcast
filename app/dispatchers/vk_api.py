import requests
import json


URL = 'https://api.vk.com/method/'


def post(token, gid, message):
    body = {
        'owner_id': gid,
        'access_token': token,
        'from_group': 1,
        'message': message,
        'v': 5.103
    }
    req = requests.post(URL + 'wall.post', params=body)
    res = json.loads(req.text)
    try:
        return res['error']['error_msg']
    except KeyError:
        return 'success'


def postPhoto(token, gid, message, file):
    body = {
        'group_id': gid[1:],
        'access_token': token,
        'v': 5.103
    }
    req = requests.post(URL + 'photos.getWallUploadServer', params=body)
    try:
        server = json.loads(req.text)['response']['upload_url']
        file = {
            'photo': open(file, 'rb')
        }
        req = requests.post(server, files=file)
        body = json.loads(req.text)

        body = {
            'server': body['server'],
            'hash': body['hash'],
            'photo': body['photo'],
            'group_id': gid[1:],
            'access_token': token,
            'v': 5.103
        }
        req = requests.post(URL + 'photos.saveWallPhoto', params=body)
        media_id = json.loads(req.text)['response'][0]['id']
        print(req.text)
        print(media_id)
    except KeyError:
        return 'Error uploading file'
    body = {
        'owner_id': gid,
        'message': message,
        'attachments': 'photo' + gid + '_' + str(media_id),
        'access_token': token,
        'v': 5.103
    }
    req = requests.post(URL + 'wall.post', params=body)
    print(req.text)
    try:
        return json.loads(req.text)['error']['error_msg']
    except KeyError:
        return 'success'
