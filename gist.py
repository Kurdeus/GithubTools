import requests
import json




class GitHub_Gist:
    def __init__(self, token=None):
        self.token = token

    def delete_gist(self,gist_id):
        headers = {'Authorization': f'token {self.token}'}
        params={'scope':'gist'}
        r = requests.delete(f"https://api.github.com/gists/{gist_id}",params=params, headers=headers)
        return {'status':True} if str(r.status_code) == '204' else {'status':False}

    def create_gist(self,content, gist_title = 'title'):
        payload={
            "description":"GIST created by python code",
            "public":False,
            "files":{
            gist_title:{"content":f"{content}"}}}
        headers = {'Authorization': f'token {self.token}'}
        params={'scope':'gist'}
        r = requests.post("https://api.github.com/gists",headers=headers,params=params,data=json.dumps(payload))
        return r.json()
    
    def edit_gist(self,gist_id, content, gist_title='title'):
        payload={
            "description":"GIST created by python code",
            "public":False,
            "files":{
            gist_title:{"content":content}}}
        headers = {'Authorization': f'token {self.token}'}
        r = requests.patch('https://api.github.com/gists/' + gist_id, data=json.dumps(payload),headers=headers) 
        return r.json()
    
    def get_all_gist(self):
        headers = {'Authorization': f'token {self.token}'}
        params={"per_page": 100}
        r = requests.get("https://api.github.com/gists",headers=headers,params=params)
        return r.json()


#response = GitHub_Gist(token='YOUR_TOKEN') do it yourself
