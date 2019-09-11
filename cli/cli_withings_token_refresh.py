import requests
import json
import config

def refresh_accesstoken(client_id, client_secret, refresh_token):
    url = "https://account.withings.com/oauth2/token"

    payload = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token
    }

    r = requests.post(url, data=payload)

    return r.json()

if __name__ == "__main__":
    SAVE_FILE_NAME = "tmp/withings_token.json"

    client_id = config.client_id
    client_secret = config.client_secret

    # リフレッシュトークンをjsonファイルから読み込み
    with open(SAVE_FILE_NAME, "r") as f:
        _json = json.load(f)
        refresh_token = _json["refresh_token"]

    results = refresh_accesstoken(client_id, client_secret, refresh_token)
    print(results["access_token"])

    # 更新したアクセストークン、リフレッシュトークンをjsonファイルに保存
    fw = open(SAVE_FILE_NAME,'w')
    json.dump(results,fw,indent=4)
