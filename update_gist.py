import requests
import json

token='github_token'
gist_id="gist_id"


def update(content):
    payload={
        "description":"GIST created by python code",
        "public":True,
        "files":{
        "envs":{"content":content}}}
    headers = {'Authorization': f'token {token}'}
    r = requests.patch('https://api.github.com/gists/' + gist_id, data=json.dumps(payload),headers=headers) 
    return r.json()
