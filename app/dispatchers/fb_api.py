import requests
import json


URL = 'https://graph.facebook.com/v6.0/'


def post(token, gid, message):
    body = {
        'message': message,
        'access_token': token
    }
    req = requests.post(URL + gid + '/feed', params=body)
    req = json.loads(req.text)
    try:
        return req['error']['message']
    except KeyError:
        return 'success'

def postPhoto(token, gid, message, paths):
    body = {
        'caption': message,
        'published': False,
        'access_token': token
    }
    attachments = []
    for f in paths:
        file = {'file': open(f, 'rb')}
        req = requests.post(URL + gid + '/photos', params=body, files=file)
        req = json.loads(req.text)
        print(req)
        try:
            attachments.append(req['id'])
        except KeyError:
            return req['error']['message']
    attachments = [{'media_fbid': el} for el in attachments]
    body = {
        'message': message,
        'access_token': token,
        'attached_media': json.dumps(attachments)
    }
    req = requests.post(URL + gid + '/feed', params=body)
    req = json.loads(req.text)
    try:
        return req['error']['message']
    except KeyError:
        return 'success'
