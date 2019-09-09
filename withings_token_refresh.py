import requests
import json
import config

class Token_refresh:
    def __init__(self):
        self.SAVE_FILE_NAME = "tmp/withings_token.json"
        self.client_id = config.client_id
        self.client_secret = config.client_secret

        # リフレッシュトークンをjsonファイルから読み込み
        with open(self.SAVE_FILE_NAME, "r") as f:
            _json = json.load(f)
            self.refresh_token = _json["refresh_token"]


    def refresh_accesstoken(self,client_id, client_secret, refresh_token):
            url = "https://account.withings.com/oauth2/token"

            payload = {
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token
            }

            r = requests.post(url, data=payload)

            return r.json()

    def run(self):
        results = self.refresh_accesstoken(self.client_id, self.client_secret, self.refresh_token)

        # 更新したアクセストークン、リフレッシュトークンをjsonファイルに保存
        fw = open(self.SAVE_FILE_NAME,'w')
        json.dump(results,fw,indent=4)
