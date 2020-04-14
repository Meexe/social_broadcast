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

def postPhoto(token, gid, message, paths):
    body = {
        'group_id': gid[1:],
        'access_token': token,
        'v': 5.103
    }
    req = requests.post(URL + 'photos.getWallUploadServer', params=body)
    try:
        server = json.loads(req.text)['response']['upload_url']
        attachments = []
        for f in paths:
            file = {'file': open(f, 'rb')}
            req = requests.post(server, files=file)
            req = json.loads(req.text)
            body = {
                'server': req['server'],
                'hash': req['hash'],
                'photo': req['photo'],
                'group_id': gid[1:],
                'access_token': token,
                'v': 5.103
            }
            req = requests.post(URL + 'photos.saveWallPhoto', params=body)
            media = json.loads(req.text)['response'][0]
            attachments.append('photo' + str(media['owner_id']) + '_' + str(media['id']))
    except KeyError:
        return 'Error uploading file'
    body = {
        'owner_id': gid,
        'message': message,
        'attachments': ','.join(attachments),
        'access_token': token,
        'v': 5.103
    }
    req = requests.post(URL + 'wall.post', params=body)
    try:
        return json.loads(req.text)['error']['error_msg']
    except KeyError:
        return 'success'
