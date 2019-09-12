import urllib.request
import json
import os

WEB_SERVICE_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
CITY_ID = 130010
SAVE_FILE_NAME = "tmp/weather.json"
OLD_FILE_NAME = "tmp/old_weather.json"


#今日、明日、明後日を設定
SEARCH_DATA_LABEL = '今日'

def download():
    if os.path.exists('tmp/weather.json'):
        os.rename('tmp/weather.json', 'tmp/old_weather.json')

    open_url = WEB_SERVICE_URL + str(CITY_ID)
    urllib.request.urlretrieve(open_url, SAVE_FILE_NAME)

def get_weather(data_label):
    weather = ''
    temp = []

    # 昨日の気温だけを取得
    with open(OLD_FILE_NAME, 'r') as f:
        JSONData = json.load(f)
        forecasts_list = JSONData['forecasts']
        for i in range(len(forecasts_list)):
            if forecasts_list[i]['dateLabel']  == data_label:
                temp.append(forecasts_list[i]['temperature']['max']['celsius'])
                break

    # 今日の天気と、気温を取得
    with open(SAVE_FILE_NAME, 'r') as f:
        JSONData = json.load(f)
        forecasts_list = JSONData['forecasts']
        for i in range(len(forecasts_list)):
            if forecasts_list[i]['dateLabel']  == data_label:
                weather = forecasts_list[i]['telop']
                temp.append(forecasts_list[i]['temperature']['max']['celsius'])
                break

    return weather, temp

if __name__ == "__main__":
    download()
    res = get_weather(SEARCH_DATA_LABEL)
    print(SEARCH_DATA_LABEL + 'の天気は' + res[0] + 'です')
    print(res[1])

