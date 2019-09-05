import urllib.request
import json

WEB_SERVICE_URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
CITY_ID = 130010
SAVE_FILE_NAME = "tmp/weather.json"

#今日、明日、明後日を設定
SEARCH_DATA_LABEL = '今日'

def download():
    open_url = WEB_SERVICE_URL + str(CITY_ID)
    urllib.request.urlretrieve(open_url, SAVE_FILE_NAME)

def get_weather(data_label):
    weather = ''
    with open(SAVE_FILE_NAME, 'r') as f:
        JSONData = json.load(f)
        forecasts_list = JSONData['forecasts']
        for i in range(len(forecasts_list)):
            if forecasts_list[i]['dateLabel']  == data_label:
                weather = forecasts_list[i]['telop']
                break
        return weather

if __name__ == "__main__":
    download()
    get_weather(SEARCH_DATA_LABEL)
    print(SEARCH_DATA_LABEL + 'の天気は' + get_weather(SEARCH_DATA_LABEL) + 'です')

