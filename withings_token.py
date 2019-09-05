import requests
import config

def get_accesstoken(client_id, client_secret, code, redirect_uri):
    url = "https://account.withings.com/oauth2/token"

    payload = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret, # consumer secret
        "code": code, # authentication code
        "redirect_uri": redirect_uri
    }

    r = requests.post(url, data=payload)

    return r.json()


if __name__ == "__main__":
    client_id = config.client_id
    client_secret = config.client_secret
    code = config.authentication_code
    redirect_uri = config.redirect_uri

    results = get_accesstoken(client_id, client_secret, code, redirect_uri)
    print(results)
